# Framework Crosswalk

> Educational summary, not legal advice. This is a high-level orientation, not a formal compliance mapping. Check the source standards for exact requirements.

Most organizations use more than one AI framework. This page shows where the toolkit's pieces support three common ones.

## NIST AI Risk Management Framework (AI RMF 1.0)

The NIST AI RMF is voluntary U.S. guidance organized around four functions: **Govern**, **Map**, **Measure**, and **Manage**.

| NIST function | What it covers | Where the toolkit helps |
|---|---|---|
| **Govern** | Policies, accountability, culture, oversight, third-party risk | [Policy framework](policy-framework.md) sections 3 to 8, 12 to 15 |
| **Map** | Understanding context, purpose, stakeholders, and risks for each system | [Inventory](../templates/model-inventory.csv) and [questionnaire](../templates/ai-risk-assessment-questionnaire.md) |
| **Measure** | Testing, evaluation, and tracking of risks and trustworthiness | Policy lifecycle controls (bias, accuracy, monitoring) in section 7 |
| **Manage** | Prioritizing and responding to risks; incidents; improvement | Tiering, approvals, incident process (sections 6, 7, 11) |

## ISO/IEC 42001 (AI management system)

ISO/IEC 42001 is a certifiable management-system standard for AI. Like other ISO management standards, it follows a plan, do, check, act structure: understanding context, leadership and policy, planning and risk assessment, support and competence, operational controls, performance evaluation, and continual improvement.

| ISO 42001 theme | Where the toolkit helps |
|---|---|
| Context and scope | Policy sections 1 and 2; inventory |
| Leadership, roles, and AI policy | Policy sections 3 and 4 |
| Risk and impact assessment | Questionnaire; tiering |
| Resources, competence, and awareness | Policy section 12 |
| Operational controls and lifecycle | Policy sections 7 to 10 |
| Performance evaluation and audit | Inventory reviews; monitoring controls |
| Improvement and corrective action | Incident process; annual review |

The toolkit is a starting point. Certification requires a full management system with documented evidence, internal audit, and management review.

## EU AI Act

| AI Act element | Where the toolkit helps |
|---|---|
| Risk tiers (prohibited, high-risk, transparency, minimal) | [Tier guide](eu-ai-act-risk-tiers.md); `tools/classify.py` |
| Provider and deployer duties | Role fields in the questionnaire and inventory |
| Transparency (Art. 50) | Questionnaire Part 4; policy section 10 |
| General-purpose AI model duties | Questionnaire Part 5; vendor terms in policy section 8 |
| AI literacy (Art. 4) | Policy section 12 |
| Record-keeping and human oversight | Policy section 7 |

## Using them together

A pragmatic approach: use the AI Act tiers to decide how much control each use case needs, use the NIST AI RMF to structure how your teams think about and measure risk, and use ISO/IEC 42001 as the target if customers or regulators expect a certified management system.

## Sources

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)
- [EU AI Act high-level summary](https://artificialintelligenceact.eu/high-level-summary/)
