def is_sum_or_subtraction(problem_str):
    is_sum = "+" in problem_str
    is_subtraction = "-" in problem_str
    # Raise Exception if there is no sum or subtraction operators
    if (not (is_sum or is_subtraction)) or (is_sum and is_subtraction):
        raise Exception("Error: Operator must be '+' or '-'")
    return is_sum


def extract_values(problem_str, operator):
    problem_values_str = problem_str.split(operator)

    # Raise Exception if after splitting the String there aren't 2 values
    if len(problem_values_str) != 2:
        raise Exception("Error: Syntax Error.")

    value1_str = problem_values_str[0].strip()
    value1_len = len(value1_str)
    value1 = int(value1_str)

    value2_str = problem_values_str[1].strip()
    value2_len = len(value2_str)
    value2 = int(value2_str)

    if operator == "+":
        answer = value1 + value2
    elif operator == "-":
        answer = value1 - value2
    else:
        raise Exception("Error: Invalid Operator.")
    answer_str = str(answer)
    answer_len = len(answer_str)

    values = [{"String": value1_str, "Length": value1_len, "Value": value1},
              {"String": value2_str, "Length": value2_len, "Value": value2},
              {"String": answer_str, "Length": answer_len, "Value": answer}]
    return values


def print_line_when_line_not_biggest(bigger_value_len, line_value_len, line_value,is_first_value):
    if is_first_value:
        print("  ", end="")
    else:
        print("+ ", end="")
    for i in range(bigger_value_len - line_value_len):
        print(" ", end="")
    print(line_value, end="    ")


def print_first_line(values_list):
    for values in values_list:
        value1 = values[0]["String"]
        value1_len = values[0]["Length"]
        value2_len = values[1]["Length"]
        answer_len = values[2]["Length"]

        if value1_len >= value2_len >= answer_len:
            print("  ", value1, end="    ")
        elif value2_len >= value1_len and value2_len >= answer_len:
            print_line_when_line_not_biggest(value2_len, value1_len, value1, True)
        else:
            print_line_when_line_not_biggest(answer_len, value1_len, value1, True)
    print()


def print_second_line(values_list):
    for values in values_list:
        value2 = values[1]["String"]
        value1_len = values[0]["Length"]
        value2_len = values[1]["Length"]
        answer_len = values[2]["Length"]

        if value2_len >= value1_len >= answer_len:
            print("+ ", value2, end="    ")
        elif value1_len >= value2_len and value1_len >= answer_len:
            print_line_when_line_not_biggest(value1_len, value2_len, value2, False)
        else:
            print_line_when_line_not_biggest(answer_len, value2_len, value2, False)
    print()


def print_third_line(values_list):
    for values in values_list:
        value1_len = values[0]["Length"]
        value2_len = values[1]["Length"]
        answer_len = values[2]["Length"]

        max_len = max([value1_len, value2_len, answer_len])
        print("--", end="")
        for i in range(max_len):
            print("-", end="")
        print("    ",end="")
    print()


class ArithmeticArranger:

    def __init__(self, problems):
        # Raise Exception if too many problems are supplied to the function
        if len(problems) > 5:
            raise Exception("Error: Too many problems.")

        is_sum_list = list()
        values_list = list()
        for problem_str in problems:
            is_sum = is_sum_or_subtraction(problem_str)
            is_sum_list.append(is_sum)

            if is_sum:
                values = extract_values(problem_str, "+")
                values_list.append(values)

        print(values_list)
        print_first_line(values_list)
        print_second_line(values_list)
        print_third_line(values_list)

        # TO-DO: Discover why there is two spaces after the first sum operator