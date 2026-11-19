#used unittest for check function


import unittest

from app import create_weekly_plan


class StudyPlanner(unittest.TestCase):

    def test_creates_rotating_weekly_plan(self):
        test_data={
        "Monday":"python",
        "Tuesday":"sql",
        "Wednesday":"python",
            }
        self.assertEqual(
            create_weekly_plan(["python","sql"],3),
            test_data
        )
    def test_rejects_empty_subjects(self):
        with self.assertRaises(ValueError):
            create_weekly_plan([],3)


if __name__=="__main__":
    unittest.main()