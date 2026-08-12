# Finance Top-Journal Writing Skills

面向 *The Journal of Finance*（JF）、*Journal of Financial Economics*（JFE）和 *The Review of Financial Studies*（RFS）的可安装写作 skill 栈。

它不是“顶刊句式库”，也不会把三本期刊想象成三种固定文风。它把近期已发表论文中可复核的论证结构、章节功能和版式惯例，与不同研究设计真正需要回答的问题结合起来，帮助 Codex/ChatGPT 起草、重构和审校金融论文。

> Independent, evidence-informed, and non-official. This project is not endorsed by the American Finance Association, Elsevier, Oxford University Press, the Society for Financial Studies, or the three journals.

## 为什么只有 5 个 skills

拆得太细会造成触发冲突、规则重复和上下文浪费。这里采用“一个全论文核心 + 四种证据逻辑专项”的结构；五个 skill 都明确覆盖 JF、JFE 和 RFS。

| Skill | 适用任务 | 典型关键词 |
|---|---|---|
| [`finance-top-journal-writing`](skills/finance-top-journal-writing/) | 全文或任一章节；默认入口 | title, abstract, introduction, literature, data, design, results, robustness, mechanism, conclusion, tables, appendix |
| [`finance-asset-pricing-writing`](skills/finance-asset-pricing-writing/) | 资产定价与投资 | expected returns, factors, SDF, anomalies, portfolio tests, predictability, fund performance |
| [`finance-causal-empirical-writing`](skills/finance-causal-empirical-writing/) | 以识别为中心的实证金融 | DID, event study, IV, RDD, natural experiment, policy shock, RCT |
| [`finance-intermediation-markets-writing`](skills/finance-intermediation-markets-writing/) | 金融中介与市场机制 | banks, credit supply, balance sheets, liquidity, dealers, price discovery, market design |
| [`finance-theory-structural-writing`](skills/finance-theory-structural-writing/) | 理论、结构估计与定量模型 | propositions, equilibrium, structural identification, calibration, counterfactual, welfare |

公司金融、家庭金融、国际金融、行为金融、FinTech 等不再机械增加目录，而是按核心证据路由。例如，公司债券收益预测进入资产定价；并购自然实验进入因果实证；银行挤兑模型进入理论/结构；描述性现金持有事实只需核心 skill。

## 覆盖哪些章节

核心 skill 对以下部分逐一给出工作流与质量门：

- title 与 abstract；
- introduction、research question、gap 和 contribution；
- literature positioning、theory、hypotheses 与 institutional background；
- data、sample、variable construction、measurement 与 research design；
- main results、economic magnitude、robustness、alternative explanations；
- mechanism、heterogeneity、discussion、limitations 与 conclusion；
- tables、figures、Internet/online appendix 和全文 reverse outline。

专项 skill 在此基础上增加领域特有的风险检查。例如资产定价会检查前视偏差、微盘股、数据挖掘、交易成本与样本外证据；因果实证会把每项稳健性检验对应到具体识别威胁；理论/结构会区分模型拟合、外部验证和反事实识别。

## 快速使用

### 1. 安装整个仓库

```bash
git clone https://github.com/yxyuan-joy/Finance-top-journal-writing-skills.git
mkdir -p ~/.codex/skills
cp -R Finance-top-journal-writing-skills/skills/* ~/.codex/skills/
```

也可以只复制所需的一个 skill 文件夹。每个 skill 自包含，不依赖仓库中的共享相对路径。

### 2. 显式调用

```text
Use $finance-top-journal-writing to rewrite my JF introduction.
Use $finance-asset-pricing-writing to audit the abstract and results framing of this RFS return-predictability paper.
Use $finance-causal-empirical-writing to restructure the identification and robustness sections of this JFE paper.
```

中文同样可以：

```text
请用 $finance-top-journal-writing，根据我给出的结果重写 JF 风格的摘要和引言；不要补造文献或数值。
请用 $finance-intermediation-markets-writing，审查这篇 RFS 银行信贷供给论文是否区分了供给、需求和借款人选择。
```

### 3. 给足最小输入

效果最好的输入至少包括：目标期刊、论文类型、研究问题、核心设计/模型、数据与样本、主结果及量级、识别边界、最接近文献、希望处理的章节。缺失信息可以留空；skill 会使用显式占位符，而不是猜测。

## 期刊适配是“证据层”，不是刻板印象

写作方法不由随机抽样决定。本项目先对 2020–2025 正式普通投稿样本的 2,065 篇论文做全量结构普查（JF 452、JFE 896、RFS 717，MinerU Markdown 覆盖 100%），再从全量清单中按“教学清晰度、可迁移性、证据边界和类型覆盖”定向建立候选池，人工精读后选出 36 篇教学范例（每刊 12 篇）。每篇范例都绑定具体的教学功能和不可照搬之处；另留一组未参与规则形成的强论文用于泛化测试。全量普查可稳定观察到：

- JF 452/452 有显式 Abstract 标题，0/452 有显式 Introduction 标题；
- JFE 862/896（96.2%）有显式 Introduction 标题；其 Abstract 前置块受版式/OCR 影响，不用 heading 计数推断摘要是否存在；
- RFS 仅 14/717（2.0%）有显式 Introduction 标题，0/717 有显式 Abstract 标题；
- 独立 literature/related-work 标题只出现在 JF 83/452、JFE 169/896、RFS 111/717；多数论文把定位嵌入引言或模型/制度讨论。

这些是已发表 PDF 的 production patterns，不是永恒的投稿规则。skill 会先服从用户模板和当前官方说明；不会仅因目标期刊不同而改变论文事实、识别强度或核心论证。策展漏斗、入选 DOI、教学功能、迁移边界和 held-out 候选均可审计：见 [`evidence/curation-report.md`](evidence/curation-report.md) 与 [`evidence/curated-exemplars.csv`](evidence/curated-exemplars.csv)。完整方法、样本与聚合结果见 [`evidence/README.md`](evidence/README.md)。

## 关键安全门

所有 skills 共享以下不可妥协规则：

1. 不编造数据、系数、样本量、制度细节、引用、DOI 或审稿要求。
2. 相关性、预测、因果、结构参数与均衡反事实使用不同强度的措辞。
3. Robustness 必须对应明确威胁，不能只是规格清单。
4. Mechanism、heterogeneity、mediation 和排除替代解释不得混写。
5. 结论不引入正文未展示的新结果。
6. 不复制或近似改写语料中的长段落；示例均为原创或合成。

## 仓库结构

```text
skills/                 # 5 个可独立安装的 skills
evidence/               # 全量普查、人工策展、held-out 与来源方法；不含论文全文
evals/                  # 路由案例、对抗性案例和评分表
scripts/                # 仓库验证与可复现语料审计
.github/workflows/      # 自动结构验证
```

发布前还用三个隔离任务对资产定价、银行因果识别和结构反事实做 forward test；测试代理只看到 skill 与合成事实，不看到预期答案或精选论文。结果见 [`evals/forward-test-results.md`](evals/forward-test-results.md)。

skill 的目录遵循当前 Agent Skills/Codex 约定：`SKILL.md` 是必需入口，`agents/openai.yaml` 提供界面元数据，详细规则放在按需读取的 `references/` 中。设计依据见 [OpenAI 官方 Build skills 文档](https://learn.chatgpt.com/docs/build-skills)。

## 本地验证

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

核心 skill 还附带一个保守的草稿检查器：

```bash
python3 skills/finance-top-journal-writing/scripts/lint_finance_draft.py paper.md
```

它只标记占位符、潜在过度因果措辞、章节缺口和明显的不一致风险，不会把近年已发表论文的长度或标题习惯误当作投稿硬门槛。

## 证据、版权与更新

- 本仓库不分发本地 PDF、MinerU JSON/Markdown 或论文正文。
- 公开证据只包含书目元数据、聚合计数、原创归纳和合成示例。
- `article-index.csv` 与 `heading-frequencies.csv` 是 2,065 篇全量普查产物；`curated-exemplars.csv` 是人工选择，二者用途不混同。
- `source-folder year` 与 final publication year 分开保存；跨年 early-view/relocated 记录不会被静默混用。
- 投稿格式会变化。涉及字数、文件、匿名化、数据政策或收费时，必须重新核对三刊当前官方页面，不能从本仓库的历史语料推断。

参考项目只用于架构比较，未复制其文本或模板：Auto-Empirical-Research-Skills、nature-skills、Business-Academic-Skill 和 AER-Skills。详见 [`evidence/source-register.md`](evidence/source-register.md)。

## License

原创代码与 skill 文本采用 [MIT License](LICENSE)。第三方论文、期刊名称和外部项目仍归各自权利人所有。
