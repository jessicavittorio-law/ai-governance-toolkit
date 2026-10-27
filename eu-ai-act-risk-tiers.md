# EU AI Act Risk Tiers: A Practical Guide

> Educational summary, not legal advice. Dates and details were checked against public sources in October 2026. Confirm against the official text and current guidance before relying on this.

## The big picture

The EU AI Act (Regulation (EU) 2024/1689) regulates AI systems by the risk they pose. The same company can have use cases in several tiers. It applies to providers and deployers of AI that is placed on the EU market or whose output is used in the EU, so it can reach organizations outside Europe.

Two roles matter throughout:

- **Provider:** develops an AI system or model, or has one developed, and places it on the market under its own name.
- **Deployer:** uses an AI system under its own authority (other than for personal, non-professional use).

You can be both. A company that fine-tunes a vendor model and sells the result is likely a provider of that system.

## The tiers

| Tier | What it means | Examples (illustrative) |
|---|---|---|
| **Prohibited** | Banned practices (Article 5) | Social scoring; manipulative techniques that cause harm; emotion recognition in the workplace or schools (with narrow exceptions) |
| **High-risk** | Heavy obligations: risk management, data governance, documentation, human oversight, accuracy and robustness, conformity assessment | AI used for hiring or worker management; creditworthiness scoring; access to essential services; certain biometric uses |
| **Transparency (limited risk)** | Disclosure duties (Article 50) | Chatbots; AI-generated or manipulated media; emotion recognition and biometric categorisation (disclosure to people exposed) |
| **General-purpose AI (GPAI) models** | Separate obligations for model providers (Articles 51 to 55), with extra duties for models with systemic risk | Foundation models and large language models |
| **Minimal risk** | No specific obligations under the Act (voluntary codes encouraged) | Spam filters; many inventory-forecasting or recommendation tools |

### Prohibited practices (Article 5)

Applied since **2 February 2025**. They include AI that uses subliminal or manipulative techniques to materially distort behavior and cause significant harm; exploits vulnerabilities due to age, disability, or social or economic situation; performs social scoring leading to unjustified detrimental treatment; predicts criminal offences solely from profiling; scrapes facial images from the internet or CCTV to build recognition databases; infers emotions in workplaces and educational institutions (except for medical or safety reasons); categorises people biometrically to infer sensitive characteristics; and, with narrow exceptions, uses real-time remote biometric identification in publicly accessible spaces for law enforcement.

The Digital Omnibus added two new prohibitions, applying from **2 December 2026**: AI systems that generate realistic non-consensual intimate imagery, and AI systems that generate child sexual abuse material.

### High-risk systems (Article 6, Annexes I and III)

A system is high-risk if it is (a) a safety component of a product covered by the EU product-safety laws in **Annex I**, or is itself such a product, and requires third-party conformity assessment; or (b) used in one of the areas listed in **Annex III**: biometrics, critical infrastructure, education and vocational training, employment and worker management, access to essential private and public services (including credit scoring), law enforcement, migration and border control, and administration of justice and democratic processes.

There is a filter: an Annex III system is not high-risk if it does not pose a significant risk to health, safety, or fundamental rights, for example because it performs a narrow procedural task or only prepares information for a human decision. But a system that performs **profiling of natural persons** is always treated as high-risk. If you rely on the exemption, document the assessment and be ready to show it to a regulator.

Core provider obligations include a risk management system, data and data governance, technical documentation, record-keeping and logging, transparency to deployers, human oversight, accuracy, robustness and cybersecurity, a quality management system, and conformity assessment. Deployers have their own duties, including using the system according to instructions, assigning competent human oversight, monitoring, keeping logs, and informing workers' representatives and affected people where required.

### Transparency obligations (Article 50)

Started applying on **2 August 2026**:

- **Providers** must make sure systems that interact directly with people tell them they are dealing with AI (unless obvious), and must mark synthetic audio, image, video, and text output in a machine-readable, detectable format.
- **Deployers** must inform people exposed to emotion recognition or biometric categorisation systems, disclose deepfakes, and label AI-generated or manipulated text published to inform the public on matters of public interest (unless it has had human review or editorial control).

Grace period: providers of generative AI systems already on the market before 2 August 2026 have until **2 December 2026** to meet the machine-readable marking duty in Article 50(2). Deployer duties were not postponed.

### General-purpose AI models (Articles 51 to 55)

Obligations for GPAI model providers began applying on **2 August 2025**. They include technical documentation, information for downstream providers, a copyright-compliance policy, and a summary of training data. Models with systemic risk face additional duties, such as evaluation, risk mitigation, incident reporting, and cybersecurity. If you build products on top of someone else's model, you are usually a downstream provider or deployer, and you should ask your model vendor for the documentation it owes you.

### AI literacy (Article 4)

Organizations that provide or deploy AI are expected to take measures to ensure a sufficient level of AI literacy among staff and others using AI on their behalf. It has applied since **2 February 2025**. The Digital Omnibus discussions addressed this provision, so check the current text for who carries the duty.

## Key dates (verified October 2026)

| Date | What applies |
|---|---|
| 2 Feb 2025 | Prohibited practices; AI literacy |
| 2 Aug 2025 | GPAI model obligations; governance and penalty provisions |
| 2 Aug 2026 | Article 50 transparency obligations |
| 2 Dec 2026 | Grace period ends for Article 50(2) marking (pre-existing generative systems); two new prohibitions apply |
| 2 Dec 2027 | Annex III high-risk obligations (moved from 2 Aug 2026 by the Digital Omnibus) |
| 2 Aug 2028 | Annex I (product-embedded) high-risk obligations |
| 2 Aug 2030 | Extended date for certain high-risk systems of providers and deployers that are public authorities |

Under the Omnibus, Annex III systems already on the market before 2 December 2027 are generally caught only if they are substantially modified after that date.

## Penalties

Fines are tiered. For the most serious breaches, the Act sets maximums of up to EUR 35 million or 7% of worldwide annual turnover (whichever is higher) for prohibited practices; up to EUR 15 million or 3% for most other obligations; and up to EUR 7.5 million or 1% for supplying incorrect information to authorities. The Omnibus extended simplified measures and tailored penalty caps to "small mid-cap" companies.

## A retail and technology lens

Examples of how common retail and technology use cases may map. These are illustrative screening prompts, not conclusions. The answer turns on the specific facts.

| Use case | Likely starting point | Why to look closer |
|---|---|---|
| Demand forecasting, dynamic pricing, inventory optimization | Minimal risk | Check consumer-protection and competition law; confirm no personal profiling |
| Customer-facing chatbot or shopping assistant | Transparency | Must tell users they are talking to AI unless obvious |
| Product-description or marketing content generation | Transparency (for synthetic content marking) | Marking duties for providers; deployer disclosure rules for deepfakes and public-interest text |
| Recruiting, résumé screening, scheduling or performance tools for store staff | Potentially **high-risk** (employment) | Annex III covers recruitment and worker management, including allocating tasks and monitoring behavior |
| Emotion detection on employees or in-store cameras | Potentially **prohibited** (workplace) or transparency | Emotion recognition in the workplace is banned in most cases; in other settings, disclosure is required |
| Facial recognition for access or loss prevention | Potentially **high-risk** or **prohibited** | Biometric identification is heavily restricted; also triggers GDPR special-category rules |
| Credit or "buy now, pay later" decisioning | Potentially **high-risk** (creditworthiness) | Annex III covers credit scoring of natural persons |
| In-store IoT and computer vision counting foot traffic (no identification) | Often minimal, but verify | Confirm the system does not identify or profile individuals; check GDPR |

## Not a stand-alone analysis

The AI Act sits alongside GDPR, consumer-protection law, product-safety law, intellectual-property law, employment law, and sector rules. A tier result tells you which AI Act obligations to examine first. It does not tell you whether a use case is lawful.

## Sources

- [Regulation (EU) 2024/1689 (the AI Act), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [High-level summary of the AI Act](https://artificialintelligenceact.eu/high-level-summary/)
- [European Commission FAQ on Article 50 transparency obligations](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act)
- [Orrick, "EU AI Act Update: Digital Omnibus Finalizes 8 Compliance Changes" (July 2026)](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes)
- [Morgan Lewis, "EU AI Act's Transparency Rules: What Went Into Effect on 2 August?" (August 2026)](https://www.morganlewis.com/blogs/sourcingatmorganlewis/2026/08/eu-ai-acts-transparency-rules-what-went-into-effect-on-2-august)
