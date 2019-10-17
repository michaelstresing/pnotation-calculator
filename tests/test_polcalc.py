import unittest

from pnotation_calculator.polcalc import Expression, ValueExpression


class TestCalc(unittest.TestCase):

    def test_no_missordered_paras(self):
        te = Expression("(()()()())")
        even_grouped = te.get_matching_para_sets()
        # even_nested = te.get_matching_para_sets("(((())))")
        # missmatched_but_same = te.get_matching_para_sets("()))((()")
        # missmatched_odd_open = te.get_matching_para_sets("(()")
        # missmatched_odd_close = te.get_matching_para_sets("())")

        self.assertEqual([(1, 2), (3, 4), (5, 6), (7, 8), (0, 9)], even_grouped, "Para Matching broken: even_grouped")
        # self.assertEqual(True, even_nested, "Para Matching broken: even_nested")
        # self.assertEqual(False, missmatched_but_same, "Para Matching broken: odd_same")
        # self.assertEqual(False, missmatched_odd_open, "Para Matching broken: odd_open")
        # self.assertEqual(False, missmatched_odd_close, "Para Matching broken: odd_close")

    def test_ve_formatting_correct(self):
        ve1 = ValueExpression("(+ 1 2 3)")
        ve2 = ValueExpression("(+ 1 9)")
        ve3 = ValueExpression("(+ 12 2")

        ve1.reformat_ve()
        ve2.reformat_ve()
        ve3.reformat_ve()

        ve1f = ve1.operator
        ve1o = ve1.operand

        self.assertEqual("+", ve1f, "VE did not take operator")
        self.assertEqual(["1","2","3"], ve1o, "VE did not take operand")

    def test_ve_add(self):
        ve1 = ValueExpression("(+ 1 2 3)")
        ve2 = ValueExpression("(+ 1 9)")
        ve3 = ValueExpression("(+ 12 2)")

        ve1 = ve1.evaluate_ve()
        ve2 = ve2.evaluate_ve()
        ve3 = ve3.evaluate_ve()

        self.assertEqual(6, ve1, "VE did not sum")
        self.assertEqual(10, ve2, "VE did not sum")
        self.assertEqual(14, ve3, "VE did not sum")

    def test_ve_subtract(self):
        ve1 = ValueExpression("(- 1 2 3)")
        ve2 = ValueExpression("(- 1 9)")
        ve3 = ValueExpression("(- 12 2)")

        ve1 = ve1.evaluate_ve()
        ve2 = ve2.evaluate_ve()
        ve3 = ve3.evaluate_ve()

        self.assertEqual(-4, ve1, "VE did not subtract")
        self.assertEqual(-8, ve2, "VE did not subtract")
        self.assertEqual(10, ve3, "VE did not subtract")

    def test_ve_multiply(self):
        ve1 = ValueExpression("(* 1 2 3)")
        ve2 = ValueExpression("(* 1 9)")
        ve3 = ValueExpression("(* 12 2)")

        ve1 = ve1.evaluate_ve()
        ve2 = ve2.evaluate_ve()
        ve3 = ve3.evaluate_ve()

        self.assertEqual(6, ve1, "VE did not multiply")
        self.assertEqual(9, ve2, "VE did not multiply")
        self.assertEqual(24, ve3, "VE did not multiply")

    def test_ve_divide(self):
        ve1 = ValueExpression("(/ 1 2 3)")
        ve2 = ValueExpression("(/ 1 9)")
        ve3 = ValueExpression("(/ 12 2)")

        ve1 = ve1.evaluate_ve()
        ve2 = ve2.evaluate_ve()
        ve3 = ve3.evaluate_ve()

        self.assertAlmostEqual(0.166, ve1, 0, "VE did not divide")
        self.assertAlmostEqual(0.111, ve2, 0, "VE did not divide")
        self.assertEqual(6, ve3, "VE did not divide")

    def test_ve_repr(self):
        ve1 = ValueExpression("(+ 4 5 12)")
        ver = str(ve1)

        self.assertEqual(
            f'ValueExpression object, which applies {ve1.operator} to {ve1.operand}', ver, "Not repr right"
        )

    def test_expression_raw_assignment(self):
        ex1 = Expression("(4 5 2) (4 3 1)")
        test1 = ex1.assign_content_to_expressions()

        self.assertEqual([("4 3 2"), ("4 3 1")], test1, "exp assignment broken")