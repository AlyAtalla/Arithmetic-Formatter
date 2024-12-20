def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width of the problem
        width = max(len(operand1), len(operand2)) + 2

        # Format the lines
        first_line.append(operand1.rjust(width))
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        dashes.append('-' * width)

        # Calculate the result if needed
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            results.append(result.rjust(width))

    # Join the lines with four spaces between each problem
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')