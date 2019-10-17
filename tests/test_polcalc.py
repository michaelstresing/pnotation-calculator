import unittest

from calculator.polcalc import Expression

class TestCalc(unittest.TestCase):

    def test_no_missordered_paras(self):
        te = Expression()
        even_grouped = te.check_matching_paras("()()()()")
        even_nested = te.check_matching_paras("(((())))")
        missmatched_but_same = te.check_matching_paras("()))((()")
        missmatched_odd_open = te.check_matching_paras("(()")
        missmatched_odd_close = te.check_matching_paras("())")

        self.assertEqual([(0, 1), (2, 3), (4, 5), ()], even_grouped, "Para Matching broken: even_grouped")
        self.assertEqual(True, even_nested, "Para Matching broken: even_nested")
        self.assertEqual(False, missmatched_but_same, "Para Matching broken: odd_same")
        self.assertEqual(False, missmatched_odd_open, "Para Matching broken: odd_open")
        self.assertEqual(False, missmatched_odd_close, "Para Matching broken: odd_close")

