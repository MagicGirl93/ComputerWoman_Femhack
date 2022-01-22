import unittest
import json
from calculator_ballistic_trajectories import BallisticTrajectories
from create_file import SaveResult


class NameTestCase(unittest.TestCase):
    """Test for class and function we are use in FemHack.py"""

    def test_cal_h_max(self):
        """Test if calculate correctly the maximum height of the projectile."""
        ballistic_tra = BallisticTrajectories(5.2, 6.3)
        test_h_max = ballistic_tra.cal_h_max()
        self.assertEqual(test_h_max, 1.379591836734694)

    def test_cal_x_max(self):
        """Test if calculate correctly the maximum traveled distance."""
        ballistic_tra = BallisticTrajectories(5.2, 6.3)
        test_x_max = ballistic_tra.cal_x_max()
        self.assertEqual(test_x_max, 0.11645273830070109)

    def test_write_file(self):
        """Test if json file is written correctly."""
        save_result = SaveResult(5.2, 6.3, 1.379591836734694, 0.11645273830070109)
        save_result.write_file("computerwomen.json")
        with open("computerwomen.json") as jsonFile:
            jsonobject = json.load(jsonFile)
        expected_result={"InitialVelocity": 5.2, "LaunchAngle": 6.3, "h_max": 1.379591836734694, "x_max": 0.11645273830070109}
        self.assertEqual(jsonobject, expected_result)


if __name__ == '__main__':
    unittest.main()
