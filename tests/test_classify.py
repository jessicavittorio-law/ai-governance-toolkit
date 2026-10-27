"""Basic tests for tools/classify.py. Run with: python3 -m unittest discover -s tests"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

import classify  # noqa: E402


def answers(**true_ids):
    base = {qid: False for qid in classify.ALL_QUESTIONS}
    base.update({k: True for k in true_ids})
    return base


class ClassifyTests(unittest.TestCase):
    def test_minimal(self):
        self.assertEqual(classify.classify(answers())["preliminary_tier"], classify.MINIMAL_TIER)

    def test_prohibited_wins(self):
        r = classify.classify(answers(p_social_scoring=True, t_interacts_with_people=True))
        self.assertEqual(r["preliminary_tier"], classify.PROHIBITED_TIER)

    def test_annex_iii_high_risk(self):
        r = classify.classify(answers(h_employment=True))
        self.assertEqual(r["preliminary_tier"], classify.HIGH_RISK_TIER)

    def test_exemption_allowed_without_profiling(self):
        r = classify.classify(answers(h_employment=True, narrow_task_exemption=True))
        self.assertEqual(r["preliminary_tier"], classify.EXEMPTION_TIER)

    def test_profiling_defeats_exemption(self):
        r = classify.classify(
            answers(h_employment=True, narrow_task_exemption=True, profiling_of_persons=True)
        )
        self.assertEqual(r["preliminary_tier"], classify.HIGH_RISK_TIER)

    def test_annex_i_ignores_exemption(self):
        r = classify.classify(answers(h_annex1_safety=True, narrow_task_exemption=True))
        self.assertEqual(r["preliminary_tier"], classify.HIGH_RISK_TIER)

    def test_transparency(self):
        r = classify.classify(answers(t_interacts_with_people=True))
        self.assertEqual(r["preliminary_tier"], classify.TRANSPARENCY_TIER)

    def test_transparency_overlay_on_high_risk(self):
        r = classify.classify(answers(h_employment=True, t_interacts_with_people=True))
        self.assertEqual(r["preliminary_tier"], classify.HIGH_RISK_TIER)
        self.assertTrue(any("Transparency" in o for o in r["overlays"]))

    def test_gpai_overlay(self):
        r = classify.classify(answers(gpai_provider=True, gpai_systemic_risk=True))
        self.assertTrue(any("systemic risk" in o for o in r["overlays"]))

    def test_unanswered_reported(self):
        r = classify.classify({"h_employment": True})
        self.assertIn("p_csam", r["unanswered_questions"])


if __name__ == "__main__":
    unittest.main()
