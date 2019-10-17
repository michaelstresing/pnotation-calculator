from building_datastructures.stack import Stack


class Expression:

    def __init__(self, operator=None, expressions=None, operand=[]):
        self.operator = operator
        self.expressions = expressions
        self.operand = operand

    def __repr__(self):
        return f"Expression object, which applies {self.operator} to {self.contents}"

    def check_matching_paras(self, rawstringinput):
        parastack = Stack()
        parapairs = []
        count = 0

        for i in rawstringinput:

            if i == "(":
                parastack.push(count)

            elif i == ")" and len(parastack) == 0:
                return None

            elif i == ")" and len(parastack) > 0:
                parapairs.append((parastack.pop(), count))
            count += 1

        if len(parastack) == 0 and count > 0:
            return parapairs

        else:
            return None

    def assign_content_to_expressions:


class ValueExpression:

    def __init__(self, raw=None, operator=None, operand=None):
        self.operator = operator
        self.contents = operand
        self.raw = raw

    def reformat_ve(self, raw):
        self.operator = self.raw[1]
        del self.raw[0], self.raw[-1], self.raw[1]

        operandlist = self.raw.split()
        self.operand = operandlist

    def evaluate_ve(self):

         for group in groupings:
             grouplen = group[1] - group[0]
             start = group[0] + 1
             end = grouplen + 1
             grouptext = self(start:end)
             print(grouptext)

        expression_stack = Stack()
        count = 0
        inexpression = False
        operator = ['+','-','*','/','%','//','sqrt']
        expressions = []

    for i in expression:

        if i == ")" and len(expression_stack) == 0:
            return None

        elif i == "(":
            expression_stack.push(i)
            inexpression = True

        elif i in operator:
            newexpression = Expression(operator=i)

        elif i == ")" and len(expression_stack) > 0:

            while expression_stack.pop() != '(':
                newexpression.operator.append(j)


            #when you hit a close bracket, pop everything into an expression until you hit an open bracket.

        #     Recursion somewhere in here?


        elif inexpression == True:
            newexpression.operand.append(i)

        count += 1

