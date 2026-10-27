# AI Governance Toolkit

A practical, open starter kit for teams that build, buy, or deploy AI and need a governance program that product, engineering, and legal can actually use.

> **Educational use only. Not legal advice.** This toolkit is built from public sources and generic templates. It does not create an attorney-client relationship, and it does not come from any employer or client. Have qualified counsel review anything you adopt. See [DISCLAIMER](#disclaimer).

## Who this is for

- Legal, compliance, and risk leaders setting up an AI governance program for the first time
- Product and engineering teams who need a clear, lightweight way to flag AI risk early
- Founders and small teams preparing for customer security reviews and AI due diligence
- Anyone mapping their AI use cases to the EU AI Act risk tiers

## What's inside

| Path | What it is |
|---|---|
| [`docs/eu-ai-act-risk-tiers.md`](docs/eu-ai-act-risk-tiers.md) | Plain-language guide to the EU AI Act risk tiers, key dates, and a retail and technology lens |
| [`docs/policy-framework.md`](docs/policy-framework.md) | Fill-in-the-blanks AI governance policy: roles, lifecycle gates, vendors, incidents, training |
| [`docs/framework-crosswalk.md`](docs/framework-crosswalk.md) | How the toolkit maps to the NIST AI RMF and ISO/IEC 42001 |
| [`templates/ai-risk-assessment-questionnaire.md`](templates/ai-risk-assessment-questionnaire.md) | Intake questionnaire for any new AI use case |
| [`templates/model-inventory.csv`](templates/model-inventory.csv) | Inventory template for AI systems, models, and vendors |
| [`tools/classify.py`](tools/classify.py) | Small Python script that gives a **preliminary** EU AI Act tier from questionnaire answers |
| [`examples/`](examples/) | Two fictional use cases (a shift scheduler and a chatbot) with their screening output |
| [`tests/`](tests/) | Unit tests for the script. Run `python3 -m unittest discover -s tests` |

## Quick start

1. **Inventory first.** Copy `templates/model-inventory.csv` and list every AI system your organization builds, buys, or embeds. You can't govern what you haven't found.
2. **Assess each use case.** For every entry, complete the [questionnaire](templates/ai-risk-assessment-questionnaire.md).
3. **Get a preliminary tier.** Put the answers in a JSON file (see [`examples/example-answers.json`](examples/example-answers.json)) and run:

   ```bash
   python3 tools/classify.py examples/example-answers.json
   ```

4. **Apply the policy.** Adapt [`docs/policy-framework.md`](docs/policy-framework.md) to your organization and use the tier to decide which approvals, testing, and monitoring each use case needs.
5. **Have a person confirm.** The script is a screening aid. A qualified person must make the final classification.

No dependencies are required beyond Python 3.8 or newer.

## How the tiers work, in one paragraph

The EU AI Act sorts AI systems by risk: **prohibited** practices are banned; **high-risk** systems face the heaviest obligations; certain systems carry **transparency** duties; **general-purpose AI** models have their own rules; and everything else is **minimal risk**. Dates have moved recently. The Digital Omnibus on AI (Regulation (EU) 2026/1744) pushed most high-risk obligations to December 2027 and August 2028, while the Article 50 transparency rules started applying on 2 August 2026. The [tier guide](docs/eu-ai-act-risk-tiers.md) explains each one and lists the sources.

## Design principles

- **Start small.** One inventory and one intake form beat a 60-page policy nobody follows.
- **Risk-based.** Effort should scale with impact. Low-risk use cases get a light touch.
- **Built for builders.** Questions are written so a product manager can answer them without a lawyer in the room.
- **Honest about limits.** The script flags; people decide.

## Roadmap

- [ ] Example inventory for a retail technology company (fictional)
- [ ] Vendor due-diligence questionnaire for third-party AI
- [ ] Incident response playbook for AI failures
- [ ] Short guide on writing AI clauses in customer and vendor contracts
- [ ] Support for the U.S. state AI laws (e.g., Colorado)

Suggestions and corrections are welcome. Please open an issue.

## Contributing

Pull requests that fix errors, update dates, or improve clarity are welcome. Please cite a public source for any legal or regulatory statement, and do not submit confidential or employer-owned material.

## Keeping this current

AI regulation is moving quickly. Dates and requirements in this repo were checked against public sources in **October 2026**. Re-verify against the official text before relying on anything here.

## Disclaimer

The materials in this repository are provided for educational purposes only and do not constitute legal advice or create an attorney-client relationship. Laws differ by jurisdiction and change often. Consult qualified counsel about your situation. The maintainer's views are her own and do not represent any employer or client.

## License

[MIT](LICENSE). Use it, adapt it, and share improvements.

---

Built by [Jessica Vittorio](https://www.linkedin.com/in/jvittorio).
