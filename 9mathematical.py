from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

addition = 'add'
multiplication = 'mul'

fact(commutative, multiplication)
fact(commutative, addition)
fact(associative, multiplication)
fact(associative, addition)

x, y, z = var('a'), var('b'), var('c')
originalPattern = (multiplication, (addition, z, x), y)

# Dynamic input for expressions to match
n = int(input("Enter the number of expressions to test: "))
expressions = []
for i in range(n):
    expr_input = input(f"Enter expression {i+1} (e.g., '(mul, 9, (add, 5, 1))'): ")
    expr = eval(expr_input)
    expressions.append(expr)

for i, expr in enumerate(expressions):
    result = run(0, (x, y, z), eq(originalPattern, expr))
    print(f"Match for expression {i+1}: {result}")
