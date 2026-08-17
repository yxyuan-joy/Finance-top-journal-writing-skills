#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
if [[ -n "${CODEX_HOME:-}" ]]; then
  target_root="$CODEX_HOME/skills"
else
  target_root="$HOME/.agents/skills"
fi
replace=0
dry_run=0

all_skills=(
  finance-top-journal-writing
  finance-asset-pricing-writing
  finance-causal-empirical-writing
  finance-intermediation-markets-writing
  finance-theory-structural-writing
)
selected=()

usage() {
  cat <<'EOF'
Install Finance Top-Journal Writing Skills.

Usage:
  ./scripts/install.sh [options] [skill ...]

Options:
  --target PATH  Install into PATH instead of the detected user skill directory.
  --replace      Back up an existing skill, then install this release.
  --dry-run      Print planned actions without changing files.
  --list         List the five available skills.
  -h, --help     Show this help.

With no skill names, all five skills are installed.
EOF
}

is_known_skill() {
  local candidate=$1
  local known
  for known in "${all_skills[@]}"; do
    if [[ "$candidate" == "$known" ]]; then
      return 0
    fi
  done
  return 1
}

git_tracks_repo_root() {
  local git_root
  if ! command -v git >/dev/null 2>&1; then
    return 1
  fi
  if ! git_root=$(git -C "$repo_root" rev-parse --show-toplevel 2>/dev/null); then
    return 1
  fi
  [[ "$(cd "$git_root" && pwd -P)" == "$(cd "$repo_root" && pwd -P)" ]]
}

copy_payload_file() {
  local source_file=$1
  local destination_file=$2
  if ! mkdir -p "$(dirname "$destination_file")"; then
    return 1
  fi
  cp -pP "$source_file" "$destination_file"
}

copy_tracked_skill() {
  local skill=$1
  local staging=$2
  local prefix="skills/$skill"
  local manifest="$staging/.tracked-files"
  local tracked relative
  local copied=0

  if ! git -C "$repo_root" ls-files -z -- "$prefix" > "$manifest"; then
    rm -f "$manifest"
    return 1
  fi

  while IFS= read -r -d '' tracked; do
    relative=${tracked#"$prefix/"}
    if [[ "$relative" == "$tracked" || -z "$relative" ]]; then
      rm -f "$manifest"
      return 1
    fi
    if [[ ! -e "$repo_root/$tracked" && ! -L "$repo_root/$tracked" ]]; then
      echo "error: tracked source file is missing: $tracked" >&2
      rm -f "$manifest"
      return 1
    fi
    if ! copy_payload_file "$repo_root/$tracked" "$staging/$relative"; then
      rm -f "$manifest"
      return 1
    fi
    copied=$((copied + 1))
  done < "$manifest"
  rm -f "$manifest"

  ((copied > 0)) && [[ -f "$staging/SKILL.md" ]]
}

is_fallback_junk() {
  local relative=$1
  local basename=${relative##*/}
  case "/$relative/" in
    */__pycache__/*|*/.git/*|*/.svn/*|*/node_modules/*|*/.*/*)
      return 0
      ;;
  esac
  case "$basename" in
    .*|*.pyc|*.pyo|*.tmp|*.temp|*.bak|*.orig|*.rej|*.swp|*.swo|*~|\#*\#|Thumbs.db)
      return 0
      ;;
  esac
  return 1
}

copy_release_skill() {
  local skill=$1
  local staging=$2
  local source_dir="$repo_root/skills/$skill"
  local component source_file relative
  local copied=0

  if ! copy_payload_file "$source_dir/SKILL.md" "$staging/SKILL.md"; then
    return 1
  fi
  copied=1

  # Release archives have no Git index. Limit their payload to the standard
  # Skill resource directories and filter generated/editor artifacts anywhere
  # inside those directories. Root-level auxiliary files are intentionally not
  # installed.
  for component in agents references assets scripts; do
    [[ -d "$source_dir/$component" ]] || continue
    while IFS= read -r -d '' source_file; do
      relative=${source_file#"$source_dir/"}
      if is_fallback_junk "$relative"; then
        continue
      fi
      if ! copy_payload_file "$source_file" "$staging/$relative"; then
        return 1
      fi
      copied=$((copied + 1))
    done < <(find "$source_dir/$component" \( -type f -o -type l \) -print0)
  done

  ((copied > 0)) && [[ -f "$staging/SKILL.md" ]]
}

copy_skill_payload() {
  local skill=$1
  local staging=$2
  if git_tracks_repo_root; then
    copy_tracked_skill "$skill" "$staging"
  else
    copy_release_skill "$skill" "$staging"
  fi
}

while (($#)); do
  case "$1" in
    --target)
      if (($# < 2)); then
        echo "error: --target requires a path" >&2
        exit 2
      fi
      target_root=$2
      shift 2
      ;;
    --replace)
      replace=1
      shift
      ;;
    --dry-run)
      dry_run=1
      shift
      ;;
    --list)
      printf '%s\n' "${all_skills[@]}"
      exit 0
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --*)
      echo "error: unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      selected+=("$1")
      shift
      ;;
  esac
done

if ((${#selected[@]} == 0)); then
  selected=("${all_skills[@]}")
fi

for skill in "${selected[@]}"; do
  if ! is_known_skill "$skill"; then
    echo "error: unknown skill: $skill" >&2
    echo "Run ./scripts/install.sh --list to see valid names." >&2
    exit 2
  fi
  if [[ ! -f "$repo_root/skills/$skill/SKILL.md" ]]; then
    echo "error: source skill is incomplete: $skill" >&2
    exit 1
  fi
done

if ((dry_run == 0)); then
  mkdir -p "$target_root"
fi

status=0
stamp=$(date '+%Y%m%d-%H%M%S')
backup_root="${target_root}.backups"
staging_root="${target_root}.staging"
for skill in "${selected[@]}"; do
  source_dir="$repo_root/skills/$skill"
  destination="$target_root/$skill"

  if [[ -e "$destination" && $replace -eq 0 ]]; then
    echo "exists: $destination (use --replace to back up and replace)" >&2
    status=1
    continue
  fi

  if ((dry_run)); then
    if [[ -e "$destination" ]]; then
      echo "would back up: $destination -> $backup_root/${skill}.${stamp}"
    fi
    echo "would install: $skill -> $destination"
    continue
  fi

  mkdir -p "$staging_root"
  staging=$(mktemp -d "$staging_root/${skill}.XXXXXX")
  if ! copy_skill_payload "$skill" "$staging"; then
    rm -rf "$staging"
    rmdir "$staging_root" 2>/dev/null || true
    echo "error: failed to stage $skill; existing installation was not changed" >&2
    status=1
    continue
  fi

  backup=""
  if [[ -e "$destination" ]]; then
    mkdir -p "$backup_root"
    backup="$backup_root/${skill}.${stamp}"
    suffix=1
    while [[ -e "$backup" ]]; do
      backup="$backup_root/${skill}.${stamp}.${suffix}"
      suffix=$((suffix + 1))
    done
    mv "$destination" "$backup"
    echo "backed up: $destination -> $backup"
  fi

  if mv "$staging" "$destination"; then
    echo "installed: $skill -> $destination"
  else
    echo "error: failed to activate $skill" >&2
    if [[ -n "$backup" && ! -e "$destination" ]]; then
      mv "$backup" "$destination"
      echo "restored: $destination" >&2
    fi
    rm -rf "$staging"
    status=1
  fi
  rmdir "$staging_root" 2>/dev/null || true
done

if ((status != 0)); then
  exit "$status"
fi

if ((dry_run)); then
  echo "Dry run complete. No files were changed."
else
  echo "Installation complete. Restart Codex if the skills do not appear immediately."
fi
