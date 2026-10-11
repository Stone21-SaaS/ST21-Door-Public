---
id: P-YYYY-NNN
author: <署名>
content_sha256: <按 README 第 8 节 R-a 算法算出：64 位十六进制>
claim: <一句话说清预测什么>
probability: <两位小数，如 0.45>
deadline_utc: <YYYY-MM-DDTHH:MM:SSZ>
criterion: TRUE = <什么情况算命中>；FALSE = <什么情况算不命中>。排除：<明确不算命中的情形>
criterion_source: <去哪里看：官方页 / 正式文件 / 原始数据>
resolver: <到期由谁查证>
status: OPEN
---

发布时间（T_publish）以 `index.md` 的发布记录表为准（服务端时间 + commit SHA）；文件内不预填。

<!--
填写须知（本注释不参与哈希，可删）：
1. 值一律写到行尾、不折行 —— 折行会让 content_sha256 对不上。
2. probability 写两位小数字符串（0.45、0.60），不要写成 .45 或 45%。
3. criterion 必须二分、指向外部来源；"排除什么"要写清楚。
4. 结算时：status 改 TRUE / FALSE；若无法核验，改 VOID 并在正文加一行
   `VOID原因：<为什么无法核验>`。
5. 错了不删不改；要改判断，另发一条新预测。
-->
