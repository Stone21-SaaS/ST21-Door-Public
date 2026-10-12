# 2026 年德国「AI 搜索输出责任」结构化汇编（司法 + 行政两套程序）

**编制日期**：2026-10-12
**覆盖范围**：德国法院与媒体监管机关就 AI 搜索/聊天机器人输出责任作出的公开决定（本轮截止 2026-10-12）
**收录标准**：判决/处分文书本身，或官方公告、或至少一家权威机构（大学法评/官方监管机关）的具名分析；**只用公开信息，不补、不猜、不改写**
**共收录**：2 个条目（慕尼黑临时禁令 1 件、ZAK 行政处分 1 件）+ **1 个未收录缺口（见「未收录说明」）**，另附同一条判例线上的 3 件旁证
**复核**：**未经独立复核**（本汇编由核编制，待清岚复核）

> ⚠️ **本汇编严格分编**：**第一编为司法程序（法院）**，**第二编为行政程序（监管机关）**。
> **两套程序不得混为一谈** —— 这是任务单的明确要求，也是本次编制的结构原则。

---

## 第一编 · 司法程序（法院）

### 案例一：LG München I，Az. 26 O 869/26（2026-05-28）—— Google 对 AI Overviews 的虚假陈述承担直接责任

- **事实摘要**：慕尼黑第一地区法院就 Google 的 **AI Overviews**（Übersicht mit KI）作出裁定。某出版社在 AI 概览中被错误描述为**经营订阅诈骗、并不断更换名称**。法院**准予临时禁令**（interim injunction）。
- **核心说理（本汇编最要紧的一段）**：德国法区分 **mittelbare Störerhaftung**（间接干扰者责任，传统搜索引擎适用）与 **unmittelbare Störerhaftung**（直接干扰者责任）。法院把 Google 归入**后者**，理由是——
  > **"An AI overview does not list results. It composes them: it affirms the query, restructures the underlying sources into a new narrative, and produces assertions found nowhere in the cited pages. That is authorship rather than retrieval."**
  > （AI 概览不*列出*结果，它*编造*结果……**那是作者身份，不是检索**。）
  据此认定 Google **Zu-Eigen-Machen**（将内容据为己有），须为其生成的内容负责。
- **对搜索引擎特权的处理**：旧判例给予搜索运营者宽泛的监测豁免，理由是"没有它们互联网无法使用"。法院指出 **AI 概览并无这种必要性** —— 链接已使数据洪流可导航，而概览是**用户并不需要、也难以复核**的"精选答案"；**必要性一旦消失，特权随之消失**。
- **驳回的抗辩**：① 用户负有核实义务 —— 法院驳回：概览读起来像**自足的答案**，**没有任何可见的不可靠提示**，仅"可以交叉核对"不足以免责；② 将禁令限于德国境内 —— 法院**拒绝**，援引 **Brussels Ia 条例**的跨境效力。
- **法律适用**：认定 **AI Act 于本案事实不适用**，但仍认定 Google 属 **第 3 条意义上的 provider**。
- **状态**：**临时禁令（可上诉）**。⚠️ 本次所用来源**未载明慕尼黑本案是否已提上诉**，故**不下结论**。
- **来源**：https://blogs.law.ox.ac.uk/oblb/blog-post/2026/07/who-speaks-when-algorithm-speaks-german-ruling-ai-overviews （牛津大学法学院 Oxford Business Law Blog，具名作者 Giovanni Vetrugno，2026-07-16）

### 同一条判例线上的旁证（同一来源，供对照）

| 法院 | 案号 | 日期 | 口径 |
|---|---|---|---|
| LG Frankfurt am Main | 2-06 O 271/25 | 2025-09-10 | 竞争法上**原则性承认**此类责任 |
| LG Hamburg | 324 O 461/25 | 2025-09-23 | 以**人格权**处理聊天机器人的虚构 |
| **OLG Hamm** | **4 UKl 3/25** | **2026-05-12** | 从不正当竞争法推出平行义务；**已准上诉至联邦最高法院（BGH）** |

> 注：**OLG Hamm 4 UKl 3/25 正是公开审计案卷 Case 12 所依据的判决**（Aesthetify GmbH 一案）—— 两条线在此交汇。

### 未收录说明（缺口，如实列出）

- **LG Berlin，Az. 52 O 62/26（2026-06-01）** —— 任务单列为"反向观点，必须并列呈现"，但**未给出任何来源链接**；
  本机**无检索能力**（DuckDuckGo/Jina 线路不通，Mojeek 0 结果，Bing 无实质结果），**故不收录**。
  未收录而非猜测：**宁缺毋滥**。
- **未收录**：见本节；**待小曜提供来源后可补入第一编**。

---

## 第二编 · 行政程序（监管机关）

### 案例二：ZAK 决定 02/2026（2026-07-14）—— 德国媒体法首次适用于 AI 搜索与 AI 聊天机器人

- **作出机关**：**ZAK**（Kommission für Zulassung und Aufsicht，各州媒体管理局的许可与监督委员会）
- **案由**：两案分别由 **MA HSH**（汉堡-石勒苏益格-荷尔斯泰因州媒体管理局）与 **mabb**（柏林-勃兰登堡州媒体管理局）办理，对象为 **Google 的 AI Overviews** 与 **Perplexity**（带 AI 新闻页的 AI 聊天机器人）。
- **决定**：**"ZAK erlässt erstmalig Bescheide gegen KI-Angebote von Google und Perplexity"** —— **首次**针对 Google 与 Perplexity 的 KI 服务**作出行政处分**；并**首次认定德国媒体法适用于 AI 搜索与 AI 聊天机器人**。
- **核心口径（ZAK 暨 DLM 主席 Dr. Thorsten Schmiege 逐字）**：
  > **"KI-Suchmaschinen und -Chatbots sind Inhalteanbieter – und wir wenden deutsches Medienrecht ab sofort konsequent auf sie an. Unser aktuelles Rechtsgutachten stellt klar: KI-Antworten sind eigene Inhalte der Anbieter, das Haftungsprivileg des DSA greift hier nicht."**
  > （AI 搜索与聊天机器人**是内容提供者** —— 我们即日起持续对其适用德国媒体法。我们的最新法律意见明确：**KI 回答是厂商自己的内容**，**DSA 的责任豁免在此不适用**。）
- **说理要点**：使用 AI Overviews 时，KI 回答作为结果的重要部分被**显著、突出地展示**，使**经典链接列表的可发现性相对变差** —— 构成 **"in unzulässiger Weise diskriminiert"（以不被允许的方式受到歧视）**；若 AI 聊天机器人把第三方内容作为"来源""延伸阅读"或整份链接列表附于其生成答案之后，它**同样在决定第三方内容的可发现性**，从而满足相关要件。
- **程序性质**：**行政程序（Bescheide／处分）** —— **不是**法院判决。
- **状态（截至编制日）**：行政处分**已作出**；来源未载明后续救济或期限，**故不补**。
- **来源**：https://www.die-medienanstalten.de/presse/pressemitteilungen/zak-bescheide-ki-angebote-google-perplexity/ （**官方**，die medienanstalten 新闻稿 02/2026，2026-07-14）

---

## 两套程序的对照（本汇编的重点）

| | 第一编 · 司法 | 第二编 · 行政 |
|---|---|---|
| 主体 | LG München I（法院） | ZAK（监管机关） |
| 程序 | 民事**临时禁令** | **行政处分**（Bescheid） |
| 结论口径 | AI 概览是 **authorship rather than retrieval**（作者身份而非检索）→ **Zu-Eigen-Machen** | KI 回答是 **eigene Inhalte der Anbieter**（厂商自己的内容） |
| 责任效果 | **unmittelbare Störerhaftung**（直接干扰者责任） | 适用德国媒体法；**DSA 责任豁免不适用** |
| 状态 | 临时禁令（是否已上诉**未载明**） | 已作出（后续**未载明**） |

> **共同落点**：**两套程序、两套法域，得出同一个方向 —— 把生成系统放在自己与公众之间的公司，就"拥有"了该系统所说的话。**
> 这与公开审计文件的判断同源：**门判的是输出与其依据之间的关系**，而不是替厂商编理由。

---

## 线索核验说明（如实列明）

- **已核对**：慕尼黑案号/日期/程序类型/核心说理/救济 —— 牛津 OBLB 具名分析；ZAK 案号（02/2026）/日期/机关/逐字口径/说理 —— **监管机关自身公告**。
- **未取得**：LoC 的 Germany 条目（**HTTP 403**）；Reuters 报道（未尝试，付费墙风险）；**LG Berlin 52 O 62/26**（任务单未给来源，本机无检索）。
- **未下结论**：慕尼黑案是否已上诉；ZAK 后续救济期限；当事人具名（ZAK 稿未具名，慕尼黑案仅称"一家出版社"）。

---

## English summary

**Two German tracks, one direction:** German authorities are now assigning *authorship* to AI-generated answers.

1. **Judicial (civil).** LG München I, 26 O 869/26 (28 May 2026) granted an interim injunction against Google over false statements in its **AI Overviews**, moving Google from *indirect* to *direct* interferer liability: an AI overview does not list results but **composes** them — "authorship rather than retrieval" — so the output is Google's own (*Zu-Eigen-Machen*). The court rejected the search-engine privilege (no indispensability), the "users must verify" defence, and a Germany-only scope (Brussels Ia); it held the AI Act inapplicable but Google a provider under Article 3. Sibling rulings: LG Frankfurt 2-06 O 271/25 (2025-09-10), LG Hamburg 324 O 461/25 (2025-09-23), and **OLG Hamm 4 UKl 3/25 (2026-05-12, appeal admitted to the Federal Court of Justice)** — the same judgment underlying audit Case 12.
2. **Administrative.** The **ZAK** issued its first decisions (ref. 02/2026, 14 July 2026) against the AI offerings of **Google** and **Perplexity**, holding for the first time that German media law applies to AI search and AI chatbots: "**KI-Antworten sind eigene Inhalte der Anbieter, das Haftungsprivileg des DSA greift hier nicht**" — AI answers are the providers' own content and the DSA liability privilege does not apply, because prominently placed AI answers unlawfully worsen the findability of classic link lists.

**Disclosed gap:** LG Berlin 52 O 62/26 (2026-06-01) — no source was supplied with the task, and this machine has no web search; deliberately omitted rather than guessed.

---

**编制**：核（Cline 侧），2026-10-12 · **复核**：待清岚

