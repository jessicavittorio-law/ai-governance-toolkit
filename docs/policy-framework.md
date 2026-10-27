# AI Governance Policy Framework (Template)

> Educational template, not legal advice. Replace everything in [brackets], delete what doesn't fit, and have qualified counsel review before adopting. Keep it short enough that people will read it.

**Organization:** [Company name]
**Policy owner:** [Title, e.g., General Counsel or Chief Risk Officer]
**Approved by:** [Executive sponsor / Board committee]
**Effective date:** [Date] **Next review:** [Date, at least annually]

## 1. Purpose

This policy sets how [Company] decides whether and how to build, buy, and use AI. Its goals are to (a) capture the benefits of AI, (b) prevent harm to people, customers, employees, and the company, and (c) meet legal and contractual obligations, including those under the EU AI Act, privacy laws, and customer commitments.

## 2. Scope

This policy applies to all AI systems that [Company] develops, procures, embeds in its products, or uses internally, including generative AI tools, machine-learning models, and AI features supplied by vendors. It applies to employees, contractors, and third parties acting on our behalf. [Optional: exclude personal, non-work use.]

**Definition.** An "AI system" is a machine-based system that infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. [Align with your regulators' definitions.]

## 3. Principles

1. **Accountable:** every AI system has a named business owner and technical owner.
2. **Risk-based:** controls scale with the potential impact on people.
3. **Human-centered:** people can understand, challenge, and override consequential AI outputs.
4. **Fair and non-discriminatory:** we test for and address unjustified bias.
5. **Transparent:** we tell people when they interact with AI or when AI materially affects them.
6. **Secure and private:** we protect data, models, and prompts, and we use personal data only for legitimate purposes.
7. **Reliable:** we test before launch and monitor after.

## 4. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| **Executive sponsor** | Owns AI risk appetite; reports to the Board or committee; resolves escalations |
| **AI governance committee** | Cross-functional group (Legal, Privacy, Security, Risk, Product, Engineering, HR) that approves high-risk use cases, reviews incidents, and updates this policy |
| **Policy owner** | Maintains the policy, the inventory, and the assessment process |
| **Business owner** | Accountable for the use case's purpose, outcomes, and compliance with this policy |
| **Technical owner** | Accountable for design, testing, monitoring, and documentation |
| **Legal and Privacy** | Classify regulatory risk, review contracts and notices, run DPIAs |
| **Security** | Assess vendors and threats (prompt injection, data leakage, model theft) |
| **All personnel** | Use approved tools only; report incidents; complete required training |

## 5. Inventory

All AI systems must be recorded in the AI inventory ([template](../templates/model-inventory.csv)) **before** pilot or purchase. The policy owner reviews the inventory [quarterly]. Unregistered AI use ("shadow AI") is a policy violation that should be reported without fear of retaliation so it can be brought into scope.

## 6. Risk assessment and tiering

Each use case completes the [risk assessment questionnaire](../templates/ai-risk-assessment-questionnaire.md). The result places it in a tier. Tiers follow the EU AI Act structure so one assessment serves both internal and external needs.

| Tier | Meaning | Approval authority |
|---|---|---|
| **Prohibited** | A banned practice. Not allowed. | Not approvable; escalate to Legal |
| **High-risk** | Annex I or Annex III use, or profiling in a sensitive area | AI governance committee |
| **Exemption claimed** | Annex III area, narrow-task exemption claimed | Legal sign-off, with a written assessment on file |
| **Transparency** | Interacts with people or generates synthetic content | Business owner and Legal |
| **Minimal** | No specific AI Act obligations | Business owner |

The screening script gives a preliminary tier. A named person confirms the final tier and records the rationale.

## 7. Lifecycle controls

| Gate | Prohibited | High-risk | Exemption claimed | Transparency | Minimal |
|---|---|---|---|---|---|
| Registered in inventory | n/a | Required | Required | Required | Required |
| Written purpose and success measures | n/a | Required | Required | Required | Recommended |
| Data governance review (quality, provenance, rights) | n/a | Required | Required | Required if personal data | Recommended |
| Privacy review / DPIA | n/a | Required | Required | If personal data | If personal data |
| Bias and accuracy testing before launch | n/a | Required, documented | Required | Recommended | Recommended |
| Human oversight design | n/a | Required | Required | As appropriate | Not required |
| User and affected-person disclosures | n/a | Required | Required | Required | Not required |
| Logging and record-keeping | n/a | Required | Recommended | Recommended | Optional |
| Security review | n/a | Required | Required | Required | Required |
| Ongoing monitoring (drift, errors, complaints) | n/a | Required, at least [quarterly] | [Semiannual] | [Annual] | [Annual] |
| Re-assessment on material change | n/a | Required | Required | Required | Required |

## 8. Third-party and vendor AI

Before buying or embedding third-party AI:

- Complete a vendor due-diligence review (security, privacy, model documentation, data use, sub-processors, incident notification).
- Confirm what the vendor does with our prompts, inputs, and outputs (for example, training on our data).
- Contract for: the vendor's compliance with applicable law; documentation we need to meet our own obligations (including GPAI provider documentation); audit and information rights; incident notice within [X] hours; IP and indemnity for outputs where available; data-processing terms; and the ability to exit.
- Record the vendor and underlying model in the inventory.

## 9. Generative AI acceptable use

- Use only approved tools. [List approved tools.]
- Never enter confidential, privileged, regulated, or personal data into unapproved tools.
- A human reviews AI-generated content before external use or reliance, and is responsible for it.
- Do not present AI-generated content as human-created where disclosure is required.
- Check outputs for accuracy, bias, and copyright risk. AI can fabricate sources.

## 10. Transparency and disclosure

Follow the disclosure rules triggered by the use-case tier (for example, informing people they are interacting with AI, marking synthetic content, and informing workers about AI used in employment decisions). Maintain plain-language notices and an escalation path to a human.

## 11. Incidents and issues

An AI incident is any event where an AI system causes or may cause harm, a legal breach, a significant error, a discriminatory outcome, a data leak, or a safety issue.

1. Report to [channel/email] within [24 hours].
2. The technical owner contains the issue (pause, roll back, or disable).
3. Legal and Privacy assess notification duties (regulators, customers, affected people).
4. The AI governance committee reviews root cause and fixes.
5. Record the incident and lessons learned in the inventory.

## 12. Training and AI literacy

All personnel who build, buy, approve, or use AI complete role-appropriate training within [30 days] of onboarding and [annually] after. Content should cover this policy, approved tools, data handling, bias, and when to escalate. Keep training records.

## 13. Exceptions

Exceptions need written approval from the policy owner and the executive sponsor, a stated duration, and compensating controls. High-risk exceptions go to the AI governance committee.

## 14. Enforcement

Violations may lead to disciplinary action up to and including termination, and contract remedies for third parties, subject to local law.

## 15. Review

The policy owner reviews this policy at least annually and when laws, regulatory guidance, or the organization's use of AI materially change.

## Appendix A. Quick decision guide

1. Is it AI? If yes, register it.
2. Fill in the questionnaire.
3. Prohibited? Stop and call Legal.
4. High-risk? Committee review.
5. Talks to people or makes synthetic content? Add disclosures.
6. Otherwise, apply baseline controls and monitor.

## Appendix B. Related documents

[Information security policy] · [Privacy policy and DPIA procedure] · [Acceptable use policy] · [Third-party risk policy] · [Incident response plan] · [Code of conduct]
