# 公开 AI 测试资料 · 精选证据清单（v1.1）

**版本**：v1.1 ｜ **编制日期**：2026-10-15（Asia/Shanghai）

**用途**：从公开可访问的官方来源中，筛选出可直接引用的证据条目，供报告、尽调或讨论直接引用。每一条目均附官方链接、原文短引、适用范围与引用限制。

**筛选口径**：只收录同时满足四项条件的条目——①可在公开来源中直接定位原文；②原文明确支持所述结论；③结论范围清楚；④不存在尚未解决的数值或表述冲突。

**工作边界**：只读公开来源；未执行任何论文或工具代码；未调用任何测试接口；未对模型开展新的测试；未与任何机构联系。本清单不代表任何机构对任何产品、系统或项目的认证、认可或背书。

---

## 一、精选证据（7 项）

### 1. AI Verify 测试框架的 11 项原则与适用覆盖面

- **推荐等级**：优先引用
- **一句话结论**：AI Verify 测试框架以 11 项国际公认的 AI 治理原则为评估基准，覆盖传统 AI 与生成式 AI；官方页面称，该框架与 ASEAN、欧盟、OECD 和美国等相关国际框架对齐。
- **公开来源**：AI Verify Foundation《AI Verify Testing Framework》页面（访问日 2026-10-15）— https://aiverifyfoundation.sg/tools/ai-verify-testing-framework/
- **原文定位**：页面「What is the AI Verify Testing Framework?」要点区 + 11 项原则清单（Transparency / Explainability / Reproducibility / Safety / Security / Robustness / Fairness / Data Governance / Accountability / Human Agency & Oversight / Inclusive Growth, Societal And Environmental Well-being）。
- **证据依据**：原文短引（保留英文关键词）：“assess the responsible implementation of their AI system against **11 internationally recognised AI governance principles**”；“**Covers both Traditional and Generative AI**”；“**Aligned with other international frameworks** such as those from ASEAN, European Union, OECD and US”。
- **适用范围**：可支持「框架以 11 项原则为基准、覆盖传统与生成式 AI；官方页面称其与相关国际框架对齐」。
- **引用限制**：各原则下的「检查项数」（如 Safety 0 of 17 checks）是**页面呈现**，非规范性强制要求；“对齐/一致”**不等于**认证、官方认可或背书。
- **推荐理由**：一条即概述框架的评估基准与覆盖范围，来源为官方页面且逐字可核；主题属「框架适用范围」，与其他条目不重复。

### 2. 框架与他国/国际文件的交叉映射

- **推荐等级**：可引用
- **一句话结论**：AI Verify 测试框架已与 4 份国际/他国文件建立映射：US NIST AI RMF、US NIST AI RMF–GenAI Profile、Hiroshima Process CoC、ISO/IEC 42001:2023。
- **公开来源**：AI Verify Foundation《AI Verify Testing Framework》页面（访问日 2026-10-15）— https://aiverifyfoundation.sg/tools/ai-verify-testing-framework/
- **原文定位**：页面「The Framework Is Mapped to Other Frameworks, Including:」区，四条映射及其标注日期。
- **证据依据**：原文短引：“US NIST AI RMF … **13 Oct 2023**”；“US NIST AI RMF – Gen AI Profile … **29 May 2025**”；“Hiroshima Process CoC … **29 May 2025**”；“ISO/IEC 42001: 2023 … **21 July 2025**”。
- **适用范围**：可支持「框架与这 4 份文件做了交叉映射」。
- **引用限制**：**映射 ≠ 认证或官方认可**；须注明 **29 May 2025 有两个不同条目**（NIST GenAI Profile 与 Hiroshima Process CoC），不可混为一条。
- **推荐理由**：给出可核验的映射对象与日期，帮助读者理解框架与国际标准的对接关系；信息密度高、无推断。

### 3. Project Moonshot 的定位

- **推荐等级**：优先引用
- **一句话结论**：Project Moonshot 是开源的测试工具包，通过基准测试与红队评估大语言模型/应用（LLM/apps）的安全性与可靠性。
- **公开来源**：AI Verify Foundation《Project Moonshot》页面（访问日 2026-10-15）— https://aiverifyfoundation.sg/tools/moonshot/
- **原文定位**：页面「What is Project Moonshot?」段。
- **证据依据**：原文短引：“Project Moonshot is an **open-source testing toolkit** that assesses the safety and reliability of **Large Language Models/Applications (LLM/apps)** through **benchmark testing and red teaming**.”
- **适用范围**：可支持「Moonshot 面向 LLM/LLM 应用，采用基准测试 + 红队方法，且为开源」。
- **引用限制**：该页**未给出上线日期**，不得据此断定首发时间；不得将其表述为认证或合规工具。
- **推荐理由**：官方对工具定位的单句原文，关键词齐全、无歧义；主题（工具定位）与其他条目互补。

### 4. AI Verify 测试工具包对传统 ML 的三类技术测试

- **推荐等级**：可引用
- **一句话结论**：AI Verify 测试工具包为传统机器学习模型提供公平性（Fairness）、可解释性（Explainability）与鲁棒性（Robustness）三类技术测试。
- **公开来源**：AI Verify Foundation《AI Verify Testing Toolkit》页面（访问日 2026-10-15）— https://aiverifyfoundation.sg/tools/ai-verify-toolkit/
- **原文定位**：页面「What is the AI Verify Testing Toolkit?」要点区「Comprehensive Technical Tests」项。
- **证据依据**：原文短引：“Provide technical tests for **Fairness, Explainability, and Robustness** for **traditional ML models**.”；同页：“The Toolkit **implements the AI Verify Testing Framework**.”
- **适用范围**：可支持「该工具包面向传统 ML 模型的三类技术测试，并实现该框架」。
- **引用限制**：本条仅支持对页面明确列出的传统 ML 技术测试能力作出陈述；如需说明 LLM/GenAI 测试的工具定位，应另引 Project Moonshot 的官方说明，不据本条单独推断工具包所有功能的排除范围；不得写成「覆盖全部测试类型」。
- **推荐理由**：一句界定工具能力边界，避免读者误以为其覆盖 GenAI；属「测试方法/工具能力」主题。

### 5. Starter Kit 的性质、版本与页数

- **推荐等级**：优先引用
- **一句话结论**：IMDA《Starter Kit for Testing LLM-Based Applications for Safety and Reliability》（Version 1.0，January 2026）是一套**自愿性指南**，汇总测试 LLM 应用安全与可靠性的新兴最佳实践。
- **公开来源**：IMDA《Starter Kit for Testing LLM-Based Applications for Safety and Reliability》PDF（IMDA，Version 1.0，January 2026）— https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/large-language-model-starter-kit.pdf （另见 AI Verify Foundation《Starter Kit》页面：https://aiverifyfoundation.sg/resources/starter-kit/ ）
- **原文定位**：PDF 封面（Version 1.0 / January 2026）、前言与免责声明（印刷 p.1）。**页数口径**：本次核验的 PDF 文件共 **109 个物理页面**（PDF 页对象数）；其前 5 页为封面/说明/目录，无印刷页码，正文可见印刷页码自 06 起 —— **印刷页码与 PDF 物理页数并不相同**，引用页码时须注明所用口径。（另有按「非空文本块」计得的数量，那是文本块数，不是 PDF 页数。）
- **证据依据**：原文短引：“**Version 1.0 / January 2026**”；“This Starter Kit is **a set of voluntary guidelines** that consolidates **emerging best practices and methodologies** for testing LLM-based applications for safety and reliability.”
- **适用范围**：可支持「该文件为自愿性指南、版本 1.0、2026 年 1 月、面向 LLM 应用」。
- **引用限制**：**不得写成普遍强制标准或认证要求**；版本时效以官方页面为准（官方建议使用者自行核查最新版）。
- **推荐理由**：任何引用该指南前必须先确立其「自愿性」性质与版本，本条是防止误引的**前置限定**，价值最高。

### 6. 无通用基线：阈值须各组织自定

- **推荐等级**：优先引用
- **一句话结论**：不存在适用于所有应用的通用安全基线；每个组织必须自行确定其应用的安全阈值或基线。
- **公开来源**：IMDA《Starter Kit for Testing LLM-Based Applications for Safety and Reliability》PDF（Version 1.0, January 2026）— https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/large-language-model-starter-kit.pdf
- **原文定位**：§1.2.1「What is Baseline Safety and Reliability」，印刷 p.11。
- **证据依据**：原文短引：“Can a universal baseline apply to all apps? **The simple answer is no.**”；“Ultimately, **each organisation must determine its own safety threshold or baseline**.”
- **适用范围**：可支持「阈值/基线高度依赖具体情境，须由各组织自定，无统一值」。
- **引用限制**：**不得引申为「因此无法测试」**；原文语境是「须自定阈值」，而非「不可测」。
- **推荐理由**：一句话点明该指南最关键的方法学前提，官方原文短且无争议；页码精确定位到印刷 p.11。

### 7. 「Not Applicable」的准确含义：未推荐公共基准（≠不可测）

- **推荐等级**：优先引用
- **一句话结论**：在 Starter Kit 的核心基准表中，偏见（Bias）与数据泄露（Data Leakage）标为「Not Applicable」，含义是**未推荐通用公共基准**（因高度依赖情境），但两风险仍可用公开资源自建基准并测试。
- **公开来源**：IMDA《Starter Kit for Testing LLM-Based Applications for Safety and Reliability》PDF（Version 1.0, January 2026）— https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/large-language-model-starter-kit.pdf
- **原文定位**：§1.2.2「What are Core Benchmarks?」的核心基准表（Benchmark 列）。**该表位于印刷 p.12；该节标题起于印刷 p.11** —— 引用时不要把章节起始页与表格所在页混为一谈。
- **证据依据**：原文短引：Bias 行“**Not Applicable.** Testing for bias in decision making is highly context-dependent.”；Data Leakage 行“…**which generic public benchmarks will not cover.** However, there are public resources (e.g. academic benchmarks, off-the-shelf tools) … **which can help you design your own benchmarks**.”
- **适用范围**：可支持「这两类风险在核心基准表**未推荐公共基准**，但可借公开资源自建基准」。
- **引用限制**：**不得写成「该风险不可测」**；须保留「未推荐公共基准」限定语。相关风险章节（§3.3 Bias 印刷 p.52 起、§3.5 Data Leakage 印刷 p.73 起）仍给出完整测试方法。
- **推荐理由**：这是最容易被误读成「不可测」的条目，本条把限定语一并固化，属于防止误引的高价值证据。

---

## 二、筛选方法说明

本清单在筛选时，对下列情形**不作为确定性证据**收录（方法论说明，不列举具体条目）：

- **来源内部数值不一致**：同一来源的不同表格或正文对同一指标给出不同数值，差异尚未解决；
- **可访问但正文未渲染**：链接返回成功，但正文内容无法逐字定位；
- **缺少官方逐字出处**：仅有转述或概括，或缺官方原文日期/出处；
- **存档通道抓取失败**：公开存档服务抓取失败 —— 这属于检索手段限制，**不代表来源不存在或不可用**。

未收录**不代表**相关资料不存在、无效或不适用；它只表示在当前核验条件下，该说法不足以支撑确定引用。本清单名额有限（7 项），未收录的可引用条目并非质量不足，而是为控制主题分布与来源分散度。

---

## 三、汇总表

| # | 主题 | 来源（版本/日期） | 核验状态 |
|---|---|---|---|
| 1 | 框架 11 项原则与覆盖范围 | AI Verify Foundation《AI Verify Testing Framework》页面（访问 2026-10-15） | 已核验（逐字复核） |
| 2 | 框架与国际/他国文件映射 | 同上页面（访问 2026-10-15） | 已核验（逐字复核） |
| 3 | Project Moonshot 定位 | AI Verify Foundation《Project Moonshot》页面（访问 2026-10-15） | 已核验（逐字复核） |
| 4 | 工具包对传统 ML 的三类技术测试 | AI Verify Foundation《AI Verify Testing Toolkit》页面（访问 2026-10-15） | 已核验（逐字复核） |
| 5 | Starter Kit 的性质、版本与页数 | IMDA Starter Kit PDF（Version 1.0，2026-01） | 已核验（逐字复核） |
| 6 | 无通用基线，阈值须各组织自定 | 同上 PDF，§1.2.1，印刷 p.11 | 已核验（逐字复核） |
| 7 | 「Not Applicable」= 未推荐公共基准 | 同上 PDF，§1.2.2 核心基准表，印刷 p.12 | 已核验（逐字复核） |

**入选数量：7 项。**

---

## 四、核验说明与自检

**本次核验（2026-10-15）对全部 7 个来源做了重新访问与逐字复核：**

- 三个官方网页（AI Verify Testing Framework / Project Moonshot / AI Verify Testing Toolkit）：均 HTTP 200、正文完整，逐字复核通过。
- IMDA Starter Kit PDF：HTTP 200，实测 **3,163,154 字节**、PDF 1.7、**109 个物理页面**、文件内 `CreationDate` 为 2026-01-19；封面为 `Version 1.0 / January 2026`；§1.2.1 在印刷 p.11；§1.2.2 核心基准表在印刷 p.12。文件 SHA-256：`C1F20BD18EA8446A47436005D6463E2D7D46FAD4AC1665DA3CB767576E39B7E5`。

**记录到的一处来源可用性差异**：新加坡 PDPC 的 AI 治理指引页（https://www.pdpc.gov.sg/organisations/resources/guidance-by-topic/singapores-approach-to-ai-governance ）在本次核验中页面可访问（HTTP 200），但**正文未渲染**，仅取得页面外壳（含 “Published on 03 Nov 2023”）。因此本清单**未以该页作为任何条目的定位来源**。此项属**核验手段限制**，**不代表该来源不存在或其内容不可用**。

**仍需谨慎引用的项目（即使已入选）：**

- 第 5 项：版本时效须以官方页面为准；不得写成强制标准。
- 第 6 项：不得引申为「无法测试」，必须保留「须自定阈值」原意。
- 第 7 项：必须保留「未推荐公共基准」限定语，不得写成「该风险不可测」。
- 第 2 项：映射 ≠ 认证/背书；须区分 29 May 2025 的两个条目。

**自检结果：**

- ✅ 每项均附可直接打开的公开来源链接。
- ✅ 原文短引、页码/定位与结论相互对应（Starter Kit 相关项均标印刷页码）。
- ✅ 无将推测写成事实；所有「适用范围」均对应原文短引。
- ✅ 每项均写明引用限制。
- ✅ 全文自足：读者无需任何其他文件或编号体系，即可理解每项证据与引用限制。
- ✅ 未收录任何存在未解数值冲突或尚未核实的条目。
- ✅ 未将任何官方来源表述为对任何产品、系统或项目的认证、认可或背书。

—— 2026-10-15
