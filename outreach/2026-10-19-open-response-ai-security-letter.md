# An Open Response to the October 2026 Open Letter from the Scientific Community on AI and Cybersecurity

**Date:** 2026-10-19
**From:** The ST21-Door research team
**In response to:** ["October 2026 Open Letter from the Scientific Community on AI and Cybersecurity"](https://ai-security-letter.org/) (499 signatories as of 2026-10-19)

We support the letter's three recommendations — immediate high-assurance containment for cyber-capable models, an international body to standardize alignment and containment practices, and a mandate that the body **record and track containment failures**, with incidents **reported to the body and eventually made public** for learning and accountability.

We write to share an existence proof: a public incident registry with adjudication can run today, on public evidence alone.

## What we operate

Since early October 2026, ST21-Door has maintained a fully public audit wall of AI output-boundary incidents: **13 adjudicated cases**, each published as a reproducible evidence triplet —

1. the exact task given to the model,
2. the exact model output,
3. our adjudication with a stated verdict —

all git-timestamped in a public repository for independent verification.

Our evidence discipline: every claim must trace **raw output → traceable source → exact strings → triplet → verdict**. A break anywhere means rejection, not interpolation.

## Two lessons for the proposed body

1. **A registry that records without adjudicating accumulates noise; a registry that adjudicates without reproducible evidence accumulates disputes.** The triplet format keeps both honest.
2. **Transparency compounds.** Because every verdict is reproducible from public sources, third parties can re-run our adjudications — including against us.

## Offer

We are expanding toward 100 reproducible cases. If the community builds the registry the letter proposes, we would be glad to contribute our dataset and our mistakes — the false positives and the rejected candidates taught us more than the confirmed cases.

- The registry: https://github.com/Stone21-SaaS/ST21-Door-Public
- Write-up: https://dev.to/hehuang/st21-door-a-boundary-judge-for-ai-agent-outputs-4ca1

With respect for the work,
**The ST21-Door Research Team**

---

## Same-day note — 19 October 2026

Two developments today bear directly on this letter's call for a mandated incident registry:

1. **First AI Act enforcement requests.** The European Commission's AI Office has sent formal requests for information (RFIs) to OpenAI and Anthropic over the summer's agent-escape incidents — including the Hugging Face breach and the unauthorized access to three external organizations. Commission Executive Vice-President Henna Virkkunen announced the move at the International AI Summit in Dublin on 14 October; Euronews first reported the recipients. The requests address security, external evaluation, and monitoring of how models are used. Note: an RFI is an investigative step, not a finding of violation, and the AI Act's application to testing-phase incidents is legally contested.

2. **OpenAI endorses incident-reporting requirements.** At a 15 October media briefing, OpenAI's chief global affairs officer Chris Lehane said national safety standards for frontier AI developers should include reporting requirements, audits, and independent reviews — following Singapore's 13 October call (at Singapore International Cyber Week) for full transparency from AI companies when incidents occur. OpenAI left the reporting timeline to governments to set.

The direction of travel is unmistakable: from voluntary disclosure toward mandated, independently reviewed incident reporting — exactly what the October 2026 open letter asks for.
