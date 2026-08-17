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
  if ! cp -R "$source_dir/." "$staging/"; then
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
