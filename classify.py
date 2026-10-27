#!/usr/bin/env python3
"""Preliminary EU AI Act risk-tier screening.

Reads a JSON file of yes/no answers (see examples/) and prints a preliminary
tier plus the questions that drove the result.

This is an educational screening aid, not legal advice. It does not make a
legal determination. A qualified person must make the final classification.
Rules were checked against public sources in October 2026; re-verify them
against the official text before relying on them.

Usage:
    python3 tools/classify.py examples/example-answers.json
    python3 tools/classify.py examples/example-answers.json --json
"""

import argparse
import json
import sys
from typing import Dict, List, Tuple

# ---------------------------------------------------------------------------
# Question catalog: id -> (short label, reference)
# ---------------------------------------------------------------------------

PROHIBITED = {
    "p_manipulation": ("Manipulative or subliminal techniques causing significant harm", "Art. 5(1)(a)"),
    "p_vulnerability": ("Exploits vulnerabilities (age, disability, social or economic situation)", "Art. 5(1)(b)"),
    "p_social_scoring": ("Social scoring leading to unjustified or detrimental treatment", "Art. 5(1)(c)"),
    "p_crime_prediction": ("Crime-risk prediction based solely on profiling", "Art. 5(1)(d)"),
    "p_face_scraping": ("Untargeted scraping of facial images for databases", "Art. 5(1)(e)"),
    "p_emotion_work_edu": ("Emotion inference in workplace or education", "Art. 5(1)(f)"),
    "p_biometric_sensitive": ("Biometric categorisation inferring sensitive traits", "Art. 5(1)(g)"),
    "p_realtime_rbi": ("Real-time remote biometric identification for law enforcement", "Art. 5(1)(h)"),
    "p_intimate_imagery": ("Non-consensual intimate imagery generation (applies from 2 Dec 2026)", "Digital Omnibus"),
    "p_csam": ("Child sexual abuse material generation (applies from 2 Dec 2026)", "Digital Omnibus"),
}

ANNEX_III_AREAS = {
    "h_biometrics": ("Biometrics (identification, categorisation, emotion recognition)", "Annex III(1)"),
    "h_critical_infrastructure": ("Critical infrastructure safety component", "Annex III(2)"),
    "h_education": ("Education and vocational training", "Annex III(3)"),
    "h_employment": ("Employment and worker management", "Annex III(4)"),
    "h_essential_services": ("Access to essential services (benefits, credit, insurance, emergency)", "Annex III(5)"),
    "h_law_enforcement": ("Law enforcement", "Annex III(6)"),
    "h_migration": ("Migration, asylum and border control", "Annex III(7)"),
    "h_justice_democracy": ("Justice and democratic processes", "Annex III(8)"),
}

ANNEX_I = {
    "h_annex1_safety": ("Safety component of an Annex I regulated product", "Art. 6(1), Annex I"),
}

OTHER_HIGH_RISK_INPUTS = {
    "profiling_of_persons": ("Profiles natural persons", "Art. 6(3)"),
    "narrow_task_exemption": ("Narrow-task / preparatory-use exemption claimed", "Art. 6(3)"),
}

TRANSPARENCY = {
    "t_interacts_with_people": ("Interacts directly with people", "Art. 50(1)"),
    "t_synthetic_content": ("Generates synthetic audio, image, video or text", "Art. 50(2)"),
    "t_emotion_or_biometric_cat": ("Emotion recognition or biometric categorisation deployed", "Art. 50(3)"),
    "t_deepfake": ("Generates or manipulates realistic media (deepfake)", "Art. 50(4)"),
    "t_public_interest_text": ("AI text published on matters of public interest", "Art. 50(4)"),
}

GPAI = {
    "gpai_provider": ("Provider of a general-purpose AI model", "Arts. 51-55"),
    "gpai_systemic_risk": ("Model with systemic risk (10^25 FLOPs or designated)", "Art. 51"),
}

ALL_QUESTIONS = {}
for group in (PROHIBITED, ANNEX_III_AREAS, ANNEX_I, OTHER_HIGH_RISK_INPUTS, TRANSPARENCY, GPAI):
    ALL_QUESTIONS.update(group)

# Tier labels, ordered from most to least severe.
PROHIBITED_TIER = "POTENTIALLY PROHIBITED"
HIGH_RISK_TIER = "POTENTIALLY HIGH-RISK"
EXEMPTION_TIER = "ANNEX III AREA, EXEMPTION CLAIMED (document your assessment)"
TRANSPARENCY_TIER = "TRANSPARENCY OBLIGATIONS"
MINIMAL_TIER = "MINIMAL RISK (under the AI Act)"

NEXT_STEPS = {
    PROHIBITED_TIER: [
        "Stop. Do not build, buy, or deploy until Legal has reviewed.",
        "Confirm whether a narrow exception applies and document the analysis.",
        "Notify the AI governance lead and your general counsel.",
    ],
    HIGH_RISK_TIER: [
        "Escalate to the AI governance committee before launch.",
        "Plan for risk management, data governance, technical documentation, logging, human oversight, accuracy and robustness testing, and conformity assessment.",
        "Check applicable dates: Annex III obligations apply from 2 December 2027; Annex I from 2 August 2028 (verify current text).",
        "Run a DPIA and check GDPR and employment-law requirements.",
    ],
    EXEMPTION_TIER: [
        "Write down why the system does not pose a significant risk to health, safety, or fundamental rights.",
        "Confirm it does not profile natural persons (profiling always means high-risk).",
        "Keep the assessment on file; regulators can request it.",
        "Re-assess whenever the use case changes.",
    ],
    TRANSPARENCY_TIER: [
        "Tell users when they are interacting with AI, unless it is obvious.",
        "Providers: mark synthetic output in a machine-readable way (grace period to 2 December 2026 for systems already on the market before 2 August 2026).",
        "Deployers: disclose deepfakes and label public-interest AI text unless it has human editorial review.",
    ],
    MINIMAL_TIER: [
        "No specific AI Act obligations flagged. Apply the baseline policy controls.",
        "Check GDPR, consumer-protection, IP, and contractual requirements.",
        "Re-assess if the purpose, data, or users change.",
    ],
}


def _true_ids(answers: Dict[str, bool], group: Dict[str, Tuple[str, str]]) -> List[str]:
    return [qid for qid in group if answers.get(qid) is True]


def classify(answers: Dict[str, bool]) -> Dict:
    """Return a screening result for a dict of question id -> bool."""
    prohibited_hits = _true_ids(answers, PROHIBITED)
    area_hits = _true_ids(answers, ANNEX_III_AREAS)
    annex1_hits = _true_ids(answers, ANNEX_I)
    transparency_hits = _true_ids(answers, TRANSPARENCY)
    gpai_hits = _true_ids(answers, GPAI)

    profiling = answers.get("profiling_of_persons") is True
    exemption = answers.get("narrow_task_exemption") is True

    notes: List[str] = []
    drivers: List[str] = []

    if prohibited_hits:
        tier = PROHIBITED_TIER
        drivers = prohibited_hits
    elif annex1_hits:
        tier = HIGH_RISK_TIER
        drivers = annex1_hits
        notes.append("Annex I systems cannot use the Annex III narrow-task exemption.")
    elif area_hits and profiling:
        tier = HIGH_RISK_TIER
        drivers = area_hits + ["profiling_of_persons"]
        notes.append("Profiling of natural persons in an Annex III area is always treated as high-risk.")
    elif area_hits and exemption:
        tier = EXEMPTION_TIER
        drivers = area_hits + ["narrow_task_exemption"]
    elif area_hits:
        tier = HIGH_RISK_TIER
        drivers = area_hits
    elif transparency_hits:
        tier = TRANSPARENCY_TIER
        drivers = transparency_hits
    else:
        tier = MINIMAL_TIER

    if exemption and not area_hits and not annex1_hits:
        notes.append("Exemption answered but no Annex III area selected; check the answers.")
    if gpai_hits and "gpai_provider" not in gpai_hits:
        notes.append("Systemic-risk answered without being a GPAI model provider; check the answers.")

    overlays: List[str] = []
    # Transparency duties can apply on top of a high-risk or exempt classification.
    if transparency_hits and tier in (HIGH_RISK_TIER, EXEMPTION_TIER):
        overlays.append("Transparency obligations also apply (Art. 50): " + ", ".join(transparency_hits))
    if "gpai_provider" in gpai_hits:
        if "gpai_systemic_risk" in gpai_hits:
            overlays.append("General-purpose AI model provider with systemic risk: extra duties apply (Arts. 51-55).")
        else:
            overlays.append("General-purpose AI model provider: documentation, copyright policy and training-data summary duties apply (Arts. 53-54).")

    unanswered = [qid for qid in ALL_QUESTIONS if qid not in answers]

    return {
        "preliminary_tier": tier,
        "drivers": [
            {"id": d, "label": ALL_QUESTIONS[d][0], "reference": ALL_QUESTIONS[d][1]}
            for d in drivers
        ],
        "overlays": overlays,
        "notes": notes,
        "next_steps": NEXT_STEPS[tier],
        "unanswered_questions": unanswered,
        "disclaimer": (
            "Preliminary screening aid only. Not legal advice. "
            "A qualified person must make the final classification."
        ),
    }


def load(path: str) -> Tuple[Dict, Dict[str, bool]]:
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict) or "answers" not in data:
        raise ValueError("Input must be a JSON object with an 'answers' key.")
    answers = data["answers"]
    unknown = [k for k in answers if k not in ALL_QUESTIONS]
    if unknown:
        raise ValueError("Unknown question id(s): " + ", ".join(sorted(unknown)))
    bad = [k for k, v in answers.items() if not isinstance(v, bool)]
    if bad:
        raise ValueError("Answers must be true or false (JSON booleans): " + ", ".join(sorted(bad)))
    return data.get("use_case", {}), answers


def render(use_case: Dict, result: Dict) -> str:
    lines: List[str] = []
    name = use_case.get("name", "(unnamed use case)")
    lines.append("AI GOVERNANCE SCREENING RESULT")
    lines.append("=" * 60)
    lines.append("Use case: " + name)
    if use_case.get("description"):
        lines.append("Description: " + use_case["description"])
    lines.append("")
    lines.append("Preliminary tier: " + result["preliminary_tier"])
    if result["drivers"]:
        lines.append("")
        lines.append("What drove this result:")
        for d in result["drivers"]:
            lines.append("  - [{}] {} ({})".format(d["id"], d["label"], d["reference"]))
    if result["overlays"]:
        lines.append("")
        lines.append("Also applies:")
        for o in result["overlays"]:
            lines.append("  - " + o)
    if result["notes"]:
        lines.append("")
        lines.append("Notes:")
        for n in result["notes"]:
            lines.append("  - " + n)
    lines.append("")
    lines.append("Suggested next steps:")
    for s in result["next_steps"]:
        lines.append("  - " + s)
    if result["unanswered_questions"]:
        lines.append("")
        lines.append("Unanswered (treated as 'no'): " + ", ".join(result["unanswered_questions"]))
    lines.append("")
    lines.append(result["disclaimer"])
    return "\n".join(lines)


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Preliminary EU AI Act tier screening.")
    parser.add_argument("answers_file", help="Path to a JSON file of questionnaire answers")
    parser.add_argument("--json", action="store_true", help="Print the result as JSON")
    args = parser.parse_args(argv)

    try:
        use_case, answers = load(args.answers_file)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("Error: {}".format(exc), file=sys.stderr)
        return 2

    result = classify(answers)
    if args.json:
        print(json.dumps({"use_case": use_case, **result}, indent=2))
    else:
        print(render(use_case, result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
