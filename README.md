# ST21-Door — Public Entry

**Public API endpoint:** `https://shishuanglu21.com/door/check`

**Get trial access (self-service, no approval):** <https://shishuanglu21.com/door/trial>

**First time here?** Start with the [Quick Start](QUICKSTART.md) before using the API.

ST21-Door is a judgement door. A caller submits one triple — the material a
decision rests on, the task being asked, and the model output that answers it —
and the Door returns exactly one verdict.

This repository is the public entry and showcase layer for that service. It
documents the public call contract and nothing else.

---

## What problem does ST21-Door solve?

When an AI agent or chatbot answers from source material — a policy, a
document, a case file, a retrieval result — its output can quietly claim
more than the material supports: a restriction becomes a shutdown, a
single ruling becomes binding precedent, a possibility becomes a fact.

ST21-Door is designed to help identify these cases. It is an independent check that
sits between a model's output and the outside world and answers one
question: **did this output stay inside what its material actually
supports?**

## Who is it for?

- Teams wiring LLMs or agents into customer-facing answers, summaries,
  or decisions, who need an output check that is independent of the
  model that produced the answer.
- Researchers and auditors studying real-world AI output failures —
  the public audits in this repository publish their full triples for resubmission and comparison.
- Agent builders who want an external boundary check an agent can call
  over HTTP, through an interface that accepts no caller-identity fields.

ST21-Door is an independent research project. It is not affiliated with
any model provider.

---

## Why a Door?

A model can sound perfectly confident while saying something its own material never supported. That gap — between what the material establishes and what the output claims — is the only thing ST21-Door watches.

The Door does not judge whether an answer is clever, well-written, or correct in some absolute sense. It judges one relationship: did the output stay inside the boundary of what the supplied material actually supports?

Anyone wiring a model into decisions, summaries, or customer-facing answers can put the Door between the model's output and the world: A caller can use the Door’s verdict to decide whether an output should proceed.

### What crossing the boundary looks like

**Case 1 — upgrading a decision into a precedent → `BLOCK`**  
Material: an online small-claims tribunal held an airline liable for its chatbot's misstatement and awarded CA$812. Decisions of this kind are not binding precedent.  
Output: "the ruling sets a binding precedent: airlines are liable for chatbot statements."

**Case 2 — upgrading a restriction into a shutdown → `BLOCK`**  
Material: after flawed answers surfaced, Google restricted the AI Overviews feature in some scenarios.  
Output: "Google has shut the feature down entirely."

**Case 3 — staying inside the material → `ALLOW`**  
Material: in 2006 the Philippine Supreme Court found no evidence of PepsiCo's negligence; PepsiCo won.  
Output: "the court found no evidence of negligence; PepsiCo won."

Three fields in, one verdict out. No scores, no explanations, no grading the model's arithmetic. The Door is a boundary judge, not an answer judge: it does not decide what is true, it decides whether the output overstepped its evidence.

---

## Verdicts

The public verdict set is closed. Exactly three values can ever be returned:

| Verdict | Meaning |
| --- | --- |
| `ALLOW` | The supplied model output holds up against the supplied material and task, as assessed by the Door. |
| `BLOCK` | The supplied model output does not hold up against the supplied material and task. |
| `NEEDS_EVIDENCE` | The Door ran and could not form `ALLOW` or `BLOCK` from what was supplied. More or better evidence is needed — this is an ordinary verdict, not a failure. |

`NEEDS_EVIDENCE` is never an error. A verdict and a service error are strictly
different layers, and a service failure is never dressed up as a verdict.

---

## Request

```
POST https://shishuanglu21.com/door/check
Content-Type: application/json
```

The body is an object with **exactly three string fields**:

```json
{
  "material": "...",
  "task": "...",
  "model_output": "..."
}
```

* All three fields are required, and each must be a JSON string.
* Unknown fields are **refused, not ignored**. Identity-bearing fields
  (provider, model, agent, client) are rejected by design, so no caller identity forms part of a valid request.
* The Door service does not write request bodies to its application logs or return them in responses. Host-side verification found no evidence of request bodies in the inspected nginx access/error logs, service journals, or runs.jsonl. This verification does not cover the remote model endpoint or all infrastructure-level and transient storage.

### Response

On success the Door answers `HTTP 200` with exactly one key:

```json
{ "verdict": "ALLOW" }
```

The verdict and nothing else. No reason, rule name, score, confidence, detail,
matched pattern, model name, runtime trace or debug field is ever returned, and
no response ever restates the material, task or model output.

---

## Minimal example

`examples/check-request.json` holds the request body;
`examples/check.sh` is a minimal caller:

```bash
ENDPOINT="https://shishuanglu21.com/door/check"

curl -sS -m 300 \
  -X POST "$ENDPOINT" \
  -H 'Content-Type: application/json' \
  -H "$ST21_TRIAL_HEADER" \
  --data @examples/check-request.json
```

```json
{ "verdict": "ALLOW" }
```

The verdict above is the shape of a successful answer, not a promise about any
particular request: which verdict comes back is the Door's judgement of the
triple you send.

---

## Access

Requests must carry a valid **Trial header** — an `X-ST21-Door-Trial` request
header whose *value* is issued to you by the service itself. A request without
a valid trial header is refused at the edge, before any judgement is made.

### Get Trial Access

Trial access is self-service. Nothing is requested from the maintainer, no one
approves anything, and nothing is asked of you in return.

* **[Get a Trial Header](https://shishuanglu21.com/door/trial)**

1. Open <https://shishuanglu21.com/door/trial> in a browser.
2. Click **Get a Trial Header**. A trial header is issued immediately and shown
   once, on that page.
3. Use it as an ordinary request header, as in
   [`examples/check.sh`](examples/check.sh):

   ```bash
   export ST21_TRIAL_HEADER='X-ST21-Door-Trial: <the value you were just issued>'
   ./examples/check.sh
   ```

4. The call itself is unchanged: `POST https://shishuanglu21.com/door/check`
   with the three-field body.

Trial access is deliberately short-lived and bounded. Each trial header expires
after about 24 hours and allows a limited number of requests (currently 100),
whichever comes first. When it expires or runs out it is refused at the edge
with `HTTP 403`, and you can simply visit the same page again to get a new one.

No GitHub account, issue, e-mail, sign-up, password, API key or message to the
maintainer is needed — and none of them is part of the flow. Nothing identifies
you: the trial layer stores an anonymised record of issued headers, their
expiry and how many requests they have used, and nothing else.

Trial header *values* are never published: not in this repository, not in a
release, not in an issue, and not in the server's logs. Only the header *name*
(`X-ST21-Door-Trial`) is public. The value is shown once, to you, when it is
issued.

> A trial header is a door key, not an account: low-privilege, short-lived and
> disposable. It buys one thing only — the right to send triples to the Door.

---

## For Agents

ST21-Door is designed to be callable by agents that can make HTTP POST requests.

The Door judges the full `material` / `task` / `model_output` triple. The verdict is not determined from the material and model output alone.

To try the Door with a Trial credential:

1. Obtain a Trial credential from `GET /door/trial?issue=1`. The endpoint returns an HTML page; extract the Trial header value from `X-ST21-Door-Trial: [A-Za-z0-9_-]+`.
2. Submit the `material`, `task`, and `model_output` fields to `POST /door/check`.
3. Include the Trial credential in the `X-ST21-Door-Trial` request header.
4. Read the returned verdict: `ALLOW`, `BLOCK`, or `NEEDS_EVIDENCE`.

**Note:** The first request after a period of inactivity may take longer while the backing model starts. Agents should allow a longer request timeout for the first call.

This makes the Door directly testable by API-capable agents and computer-use agents: give an agent a material/task/output triple and let it try to cross the boundary.

The Door does not decide whether an answer is correct in the abstract. It judges whether the output stayed within the boundary established by the supplied material and task.

---

## Errors

Errors never look like verdicts.

| Status | Body | Meaning |
| --- | --- | --- |
| `400` | `{"error":"invalid_body"}` | body is not a JSON object, is unreadable, or is too large |
| `400` | `{"error":"missing_fields","missing":[...]}` | one or more of the three fields is absent |
| `400` | `{"error":"unknown_fields","unknown":[...]}` | the body carried fields outside the three-field contract |
| `400` | `{"error":"fields_must_be_strings"}` | a field was present but was not a string |
| `403` | *(edge refusal)* | no valid trial header — see [Access](#access) |
| `404` | `{"error":"not_found"}` | wrong path |
| `503` | `{"error":"door_unavailable"}` | the service did not run. This is a failure of the service, not a verdict — retry later |

---

## Public Audits

Reproducible audits using publicly available AI outputs — 13 cases so far. Each case publishes the `material`, `task`, `model_output`, and Door verdict, so anyone can resubmit the same triple and compare the returned verdict with the recorded result. Verdicts may vary across runs.

See [`audits/001-public-ai-incidents.md`](audits/001-public-ai-incidents.md).

---

## Adversarial Testing

The Door has been subjected to adversarial testing from 14 different large
model sources, including DeepSeek, Claude, GPT, Gemini, Grok, MiniMax, Qwen,
GLM and Kimi. Testers attempt to craft material/task/output triples that
cross the Door's boundary without being blocked.

No confirmed breakthrough has been recorded to date.

Known limitations (observed 2026-10-14): the same triple can occasionally
return different verdicts across runs (verdict drift at boundaries); and the
verdict is sensitive to how the material is worded — the Door judges whether
the output exceeded the boundary described by the supplied material, not
whether the underlying claim is objectively true.

This list grows as new models are tested.

---

## Frequently asked questions

### How do I check whether an AI agent's output went beyond its source material?

Send the Door one triple — the material the answer rests on, the task,
and the model output — and it returns one verdict: `ALLOW`, `BLOCK`, or
`NEEDS_EVIDENCE`. The Door is designed to assess whether the output claims more than the material supports — that is what `BLOCK` is for; where the supplied material cannot settle the question, the verdict is `NEEDS_EVIDENCE`, and verdicts may occasionally vary across runs. You can try this now with a self-service
[trial header](https://shishuanglu21.com/door/trial); no account is
needed.

### Does ST21-Door decide whether an answer is true or correct?

No. The Door is a boundary judge, not an answer judge. It does not grade
answers, check arithmetic, or decide what is true in the abstract. It
judges one relationship: whether the output stayed inside the boundary
of what the supplied material supports.

### How is this different from a content filter or a typical guardrail?

Content filters screen for disallowed topics or phrasing. ST21-Door focuses on whether an output exceeds what the supplied material and task support, rather than serving as a topic-based content filter. An output fails when it overstates, upgrades, or invents beyond its material — even if every sentence is politely written and
individually plausible.

### What does the Door need from me, and what does it keep?

Exactly three string fields (`material`, `task`, `model_output`) and a
trial header. Identity-bearing fields are refused at the request-contract level, so caller identity is not part of what the Door accepts. The Door service does not write request bodies to its application logs or return them in responses. Host-side verification found no evidence of request bodies in the inspected nginx access/error logs, service journals, or runs.jsonl. This verification does not cover the remote model endpoint or all infrastructure-level and transient storage.

### Can I reproduce the published audits?

Yes. Every case in
[`audits/001-public-ai-incidents.md`](audits/001-public-ai-incidents.md)
publishes its full triple and the Door's verdict, so anyone can resend the same triple and compare the returned verdict with the recorded audit result. Results may vary across runs.

---

## 中文说明

**ST21-Door 是什么？**
一个独立的 AI 输出边界判定服务。你提交一组三元组——依据材料
(material)、任务 (task)、模型输出 (model_output)——它只返回一个
判定：`ALLOW`（未越界）、`BLOCK`（越界）或 `NEEDS_EVIDENCE`
（证据不足）。

**它解决什么问题？**
大模型和智能体在依据材料作答时，常常会悄悄说过头：把"限制使用"
说成"全面关停"，把一个个案判决说成"有约束力的先例"，把可能性
说成事实。ST21-Door 判的就是这一件事：**输出有没有超出材料实际
支持的范围。**

**它判对错吗？**
不判。ST21-Door 是边界裁判，不是答案裁判：它不给答案打分，不查
算术，也不裁定抽象意义上的真假，只判输出与其依据之间的关系是否
越界。

**怎么试用？**
自助领取试用凭证（trial header），无需注册、无需审批：
<https://shishuanglu21.com/door/trial> 。接口为
`POST https://shishuanglu21.com/door/check`，请求体只有上面三个
字符串字段。

**有没有公开案例？**
有。本仓库 `audits/` 收录了 13 个公开审计案例的完整三元组与判定
结果，任何人都可以按原文重新提交，并与记录的判定比对（不同运行的结果可能不同）。ST21-Door 是独立研究项目，
与任何模型厂商无关。

---

## What this repository is, and is not

It is the public entry: project introduction, the public call contract, the
verdict set, and a minimal example.

It is **not** a source release and holds no private material. The Door's
internal condition set, its private evaluation material and its runtime logs are
kept off GitHub entirely and are never mirrored, quoted or summarised here.
This repository will never contain credentials, tokens, keys, trial values,
request or response logs, or server and network configuration.
