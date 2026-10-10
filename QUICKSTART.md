# ST21-Door — Quick Start

This page is for someone who has never used ST21-Door before.

**Try it:** [Get a trial header](https://shishuanglu21.com/door/trial)  
**API:** `POST https://shishuanglu21.com/door/check`  
**Full contract and examples:** [README](README.md)  
**Public case records:** [Nine-case audit](audits/001-public-ai-incidents.md)

## What you send

ST21-Door receives exactly three strings:

- `material` — the material the answer is supposed to rely on.
- `task` — what the model was asked to do with that material.
- `model_output` — the model actual answer.

It returns exactly one verdict: `ALLOW`, `BLOCK`, or `NEEDS_EVIDENCE`.

The Door checks the relationship between the supplied material, task, and output. It is not a general fact-checker and does not decide whether a statement is true in the abstract. `NEEDS_EVIDENCE` is a verdict, not a service error.

## 1. Get temporary access

1. Open [the trial page](https://shishuanglu21.com/door/trial).
2. Select **Get a Trial Header**.
3. Copy the issued header value for your own use. It is shown once.
4. Keep it private. Do not post it in an issue, screenshot, or public example.

Trial access currently expires after about 24 hours or 100 requests, whichever comes first. If it expires or runs out, return to the trial page to get another one. No account or approval is required.

## 2. Make your first request

Use this example triple:

```json
{
  "material": "The office has twelve desks. Nine of them are occupied and three are free.",
  "task": "State how many desks in the office are free.",
  "model_output": "Three desks in the office are free."
}
```

### macOS / Linux / Git Bash

From a clone of this repository, set the environment variable to the complete header line issued by the trial page, then run the example:

```bash
export ST21_TRIAL_HEADER='X-ST21-Door-Trial: <your-issued-value>'
./examples/check.sh
```

Replace the placeholder with your own value. Do not commit it to a file.

### Windows PowerShell

Paste your own issued value when prompted:

```powershell
$trialValue = Read-Host "Paste your trial header value"
$headers = @{ "X-ST21-Door-Trial" = $trialValue }
$body = @{
  material = "The office has twelve desks. Nine of them are occupied and three are free."
  task = "State how many desks in the office are free."
  model_output = "Three desks in the office are free."
} | ConvertTo-Json
Invoke-RestMethod -Method Post `
  -Uri "https://shishuanglu21.com/door/check" `
  -Headers $headers `
  -ContentType "application/json" `
  -Body $body `
  -TimeoutSec 300
```

The response contains the verdict, for example:

```json
{ "verdict": "ALLOW" }
```

That is an example of the response shape, not a guarantee that every request receives `ALLOW`.

The first request after inactivity may take longer while the service starts. Allow up to five minutes for the initial call.

## 3. Try a public case

Open the [public audit](audits/001-public-ai-incidents.md), choose a case, and submit its exact `material`, `task`, and `model_output` triple. Preserve the task exactly: the verdict depends on all three fields.

The DPD case is an intentional contrast case with a `NEEDS_EVIDENCE` verdict. Do not relabel it as `BLOCK` or describe that verdict as a service failure.

## If something goes wrong

- **HTTP 403:** the trial header is missing, invalid, expired, or out of requests. Get a new one from the trial page and retry.
- **HTTP 400:** check that the body is a JSON object containing exactly the three required string fields. Unknown fields are rejected.
- **HTTP 503:** the service did not run. This is not a Door verdict; retry later.
- **Slow first request:** allow more time for model startup before deciding the service has failed.

See the [README full error table](README.md#errors) for the public contract.

## Important boundary

Do not treat a verdict as a guarantee of absolute truth or as a replacement for human judgement. The Door evaluates only the submitted material, task, and output. For public demonstrations, use the published cases or non-sensitive test material.
