import random
import unittest

import gate


class UseCaseTest(unittest.TestCase):
    def test_telecom_uses_intent_prefix(self):
        task = {"id": "[mms_issue]bad_network|no_apn[PERSONA:None]"}
        self.assertEqual(gate.use_case("telecom", task), "mms_issue")

    def test_first_write_action_names_the_flow(self):
        task = {"id": "7", "evaluation_criteria": {"actions": [
            {"name": "get_user_details"}, {"name": "cancel_reservation"},
            {"name": "send_certificate"}]}}
        self.assertEqual(gate.use_case("airline", task), "cancel_reservation")

    def test_read_only_task_is_no_write(self):
        task = {"id": "0", "evaluation_criteria": {"actions": [{"name": "get_reservation_details"}]}}
        self.assertEqual(gate.use_case("airline", task), "no_write")


class BootstrapTest(unittest.TestCase):
    def test_identical_models_have_zero_diff(self):
        a = {str(i): [1.0, 0.0, 1.0, 1.0] for i in range(10)}
        d, lo, hi = gate.bootstrap_diff(list(a), a, a, 500, random.Random(0))
        self.assertEqual((d, lo, hi), (0.0, 0.0, 0.0))

    def test_uniform_drop_is_flagged(self):
        a = {str(i): [1.0] * 4 for i in range(10)}
        b = {str(i): [0.0, 1.0, 1.0, 1.0] for i in range(10)}
        d, lo, hi = gate.bootstrap_diff(list(a), a, b, 500, random.Random(0))
        self.assertAlmostEqual(d, -0.25)
        self.assertLess(hi, 0)


if __name__ == "__main__":
    unittest.main()
