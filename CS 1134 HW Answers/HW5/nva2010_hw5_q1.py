import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

variables = {}

def evaluate_expression(expression):
    stack = []
    for token in expression.split():
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)
        elif token in variables:
            stack.append(variables[token])
        else:
            stack.append(float(token))
    return stack.pop()

def process_input(input_str):
    if input_str.strip() == "done()":
        return False
    elif "=" in input_str:
        variable_name, expression = input_str.split("=")
        variable_name = variable_name.strip()
        expression = expression.strip()
        value = evaluate_expression(expression)
        variables[variable_name] = value
        print(variable_name)
    else:
        result = evaluate_expression(input_str)
        print(result)
    return True

# Main loop
while True:
    input_str = input("--> ")
    if not process_input(input_str):
        break
