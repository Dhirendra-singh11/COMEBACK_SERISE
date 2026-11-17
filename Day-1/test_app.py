#used unittest for check function 


import unittest

from app import cal_plan


class StudyPlanner(unittest.TestCase):
    def __init__(self, param1,param2,exp_res):
        self.param1=param1
        self.param2=param2
        self.expected_res=exp_res
    def test_Checking_op(self):
        self.assertEqual(cal_plan(self.param1,self.param2),self.expected_res)
    def test_checking_zero(self):
        with self.assertRaises(ValueError):
            cal_plan(0,3)
    def test_checking_maxhrs(self):
        with self.assertRaises(ValueError):
            cal_plan(199,2)

if __name__=="__main__":
    SP1=StudyPlanner(int(input("Enter your 1st paramaeter")),int(input("Enter your second param to  check")),float(input("Enter Expected result")))

    unittest.main()