# ST21-Door — Public Entry

**Public API endpoint:** `https://shishuanglu21.com/door/check`

**Get trial access (self-service, no approval):** <https://shishuanglu21.com/door/trial>

ST21-Door is a judgement door. A caller submits one triple — the material a
decision rests on, the task being asked, and the model output that answers it —
and the Door returns exactly one verdict.

This repository is the public entry and showcase layer for that service. It
documents the public call contract and nothing else.

---

## Why a Door?

A model can sound perfectly confident while saying something its own material never supported. That gap — between what the material establishes and what the output claims — is the only thing ST21-Door watches.

The Door does not judge whether an answer is clever, well-written, or correct in some absolute sense. It judges one relationship: did the output stay inside the boundary of what the supplied material actually supports?

Anyone wiring a model into decisions, summaries, or customer-facing answers can put the Door between the model's output and the world: if the output overreaches its material, it does not go out.

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
  (provider, model, agent, client) are rejected by design, so no caller
  identity can enter the service at all.
* The request body is never stored or echoed back anywhere.

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

1. Obtain a Trial credential from `GET /door/trial?issue=1`.
2. Submit the `material`, `task`, and `model_output` fields to `POST /door/check`.
3. Include the Trial credential in the request header.
4. Read the returned verdict: `ALLOW`, `BLOCK`, or `NEEDS_EVIDENCE`.

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

## What this repository is, and is not

It is the public entry: project introduction, the public call contract, the
verdict set, and a minimal example.

It is **not** a source release and holds no private material. The Door's
internal condition set, its private evaluation material and its runtime logs are
kept off GitHub entirely and are never mirrored, quoted or summarised here.
This repository will never contain credentials, tokens, keys, trial values,
request or response logs, or server and network configuration.
