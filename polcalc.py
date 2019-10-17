from building_datastructures/stack import Stack

class Expression:

    def __init__(self, operator=None, expressions=None, operand=[]):
        self.operator = operator
        self.expressions = expressions
        self.operand = operand

    def __repr__(self):
        return f"Expression object, which applies {self.operator} to {self.contents}"

class ValueExpression:

    def __init__(self, operator=None, operand=[]):
        self.operator = operator
        self.contents = operand

def check_matching_paras(rawstringinput):
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

def check_expression_or_valueexpression():
    ...

def evaluate_expression(expression):

    groupings = check_matching_paras(expression)

    # for group in groupings:
    #     grouplen = group[1] - group[0]
    #     start = group[0] + 1
    #     end = grouplen + 1
    #     grouptext = expression[start:end]
    #     print(grouptext)

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


def evaluate_valueexpression():
    ...



evaluate_expression("((THIS)((IS)FUN YEAH))")