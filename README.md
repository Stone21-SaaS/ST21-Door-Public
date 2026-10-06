# ST21-Door — Public Entry

**Public API endpoint:** `https://shishuanglu21.com/door/check`

ST21-Door is a judgement door. A caller submits one triple — the material a
decision rests on, the task being asked, and the model output that answers it —
and the Door returns exactly one verdict.

This repository is the public entry and showcase layer for that service. It
documents the public call contract and nothing else.

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

Requests must carry a valid **Trial header**, issued separately with your trial
access. The header name and its value are kept private on the server side and
are deliberately **not** published in this repository. A request without a
valid trial header is refused at the edge, before any judgement is made.

---

## Errors

Errors never look like verdicts.

| Status | Body | Meaning |
| --- | --- | --- |
| `400` | `{"error":"invalid_body"}` | body is not a JSON object, is unreadable, or is too large |
| `400` | `{"error":"missing_fields","missing":[...]}` | one or more of the three fields is absent |
| `400` | `{"error":"unknown_fields","unknown":[...]}` | the body carried fields outside the three-field contract |
| `400` | `{"error":"fields_must_be_strings"}` | a field was present but was not a string |
| `403` | *(edge refusal)* | no valid trial header |
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
