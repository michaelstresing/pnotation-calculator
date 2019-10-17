from building_datastructures.stack import Stack


class Expression:

    def __init__(self, raw=None, operator=None, expressions=None, operand=None):
        self.raw = raw
        self.operator = operator
        self.expressions = expressions
        self.operand = operand

    def __repr__(self):
        return f"Expression object, ADD SOMETHING USEFUL"

    def get_matching_para_sets(self):
        parastack = Stack()
        parapairs = []
        count = 0

        for i in self.raw:

            if i == "(":
                parastack.push(count)
                count +=1

            elif i == ")" and len(parastack) > 0:
                parapairs.append((parastack.pop(), count))
                count += 1

            elif i == ")" and len(parastack) == 0:
                return None

        if len(parastack) == 0 and count > 0:
            return parapairs

        else:
            return None

    def assign_content_to_expressions(self): #MUST FIX
        contentstack = Stack()
        expressions = []

        for i in self.raw:

            if i == ")" and len(contentstack) == 0:
                return None

            if i == "(":
                contentstack.push(i)

            elif i == ")" and len(contentstack) > 0:

                matchingopen = "("
                newexpression = Expression()
                newraw = []
                contentstack.push('j')
                j = contentstack.peek()

                while j != matchingopen:
                    j = contentstack.pop()
                    newraw.append(j)
                    j = contentstack.peek()

                newraw.append(contentstack.pop())

                newexpression.raw = "".join(newraw)
                expressions.append(newexpression)

                return expressions

            else:
                contentstack.push(i)

        return expressions

class ValueExpression:

    def __init__(self, raw=None, operator=None, operand=None):
        self.operator = operator
        self.contents = operand
        self.raw = raw

    def __repr__(self):
        if self.raw is not None:
            self.reformat_ve()
        return f"ValueExpression object, which applies {self.operator} to {self.operand}"

    def reformat_ve(self):

        if self.raw is None:
            raise Exception("Cannot Reformat a Stack with no Raw Value")

        self.operator = self.raw[1]
        rawwithoutparas = self.raw[2:-1]

        intlist = []

        for i in rawwithoutparas.split():
            intlist.append(int(i))

        self.operand = intlist
        self.raw = None

    def evaluate_ve(self):

        if self.raw:
            self.reformat_ve()

        if self.operator == "+":
            result = 0
            for i in self.operand:
                result += i
            return result

        if self.operator == "-":
            result = self.operand[0]
            for i in self.operand[1:]:
                result -= i
            return result

        if self.operator == "*":
            result = self.operand[0]
            for i in self.operand[1:]:
                result *= i
            return result

        if self.operator == "/":
            result = self.operand[0]
            for i in self.operand[1:]:
                result = result / i
            return result


    # for i in expression:
    #
    #     if i == ")" and len(expression_stack) == 0:
    #         return None
    #
    #     elif i == "(":
    #         expression_stack.push(i)
    #         inexpression = True
    #
    #     elif i in operator:
    #         newexpression = Expression(operator=i)
    #
    #     elif i == ")" and len(expression_stack) > 0:
    #
    #         while expression_stack.pop() != '(':
    #             newexpression.operator.append(j)
    #
    #
    #         #when you hit a close bracket, pop everything into an expression until you hit an open bracket.
    #
    #     #     Recursion somewhere in here?
    #
    #
    #     elif inexpression == True:
    #         newexpression.operand.append(i)
    #
    #     count += 1

