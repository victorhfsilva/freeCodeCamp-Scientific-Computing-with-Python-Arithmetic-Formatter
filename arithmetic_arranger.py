def is_sum_or_subtraction(problem_str):
    is_sum = "+" in problem_str
    is_subtraction = "-" in problem_str
    # Raise Exception if there is no sum or subtraction operators
    if (not (is_sum or is_subtraction)) or (is_sum and is_subtraction):
        raise Exception("Error: Operator must be '+' or '-'")
    return is_sum


def raise_values_exceptions(problem_values_str):
    # Raise Exception if after splitting the String there aren't 2 values
    if len(problem_values_str) != 2:
        raise Exception("Error: Syntax Error.")

    value1_str = problem_values_str[0].strip()
    value2_str = problem_values_str[1].strip()

    # Raise Exception if the values have more than four digits
    if len(value1_str) > 4 or len(value2_str) > 4:
        raise Exception("Error: Numbers cannot be more than four digits.")

    # Raise Exception if the values have more than
    if not (value1_str.isdigit() and value2_str.isdigit()):
        raise Exception("Error: Numbers must only contain digits.")


def calculate_answer(value1, value2, operator):
    if operator == "+":
        answer = value1 + value2
    elif operator == "-":
        answer = value1 - value2
    else:
        raise Exception("Error: Invalid Operator.")
    return answer


def extract_values(problem_str, operator):
    problem_values_str = problem_str.split(operator)
    raise_values_exceptions(problem_values_str)

    value1_str = problem_values_str[0].strip()
    value1_len = len(value1_str)
    value1 = int(value1_str)

    value2_str = problem_values_str[1].strip()
    value2_len = len(value2_str)
    value2 = int(value2_str)

    answer = calculate_answer(value1, value2, operator)
    answer_str = str(answer)
    answer_len = len(answer_str)

    values = [{"String": value1_str, "Length": value1_len, "Value": value1},
              {"String": value2_str, "Length": value2_len, "Value": value2},
              {"String": answer_str, "Length": answer_len, "Value": answer}]
    return values


def print_line_when_line_not_biggest(biggest_value_len, line_value_len, line_value,is_second_value,is_sum):
    if is_second_value:
        if is_sum:
            print("+ ", end="")
        else:
            print("- ", end="")
    else:
        print("  ", end="")
    for i in range(biggest_value_len - line_value_len):
        print(" ", end="")
    print(line_value, end="    ")


def print_first_line(values_list, is_sum_list):
    i = 0
    for values in values_list:
        value1 = values[0]["String"]
        value1_len = values[0]["Length"]
        value2_len = values[1]["Length"]
        answer_len = values[2]["Length"]

        if value1_len >= value2_len >= answer_len:
            print(" ", value1, end="    ")
        elif value2_len >= value1_len >= answer_len:
            print_line_when_line_not_biggest(value2_len, value1_len, value1, False, is_sum_list[i])
        else:
            print_line_when_line_not_biggest(answer_len, value1_len, value1, False, is_sum_list[i])
    print()
    i += 1


def print_second_line(values_list, is_sum_list):
    i = 0
    for values in values_list:
        value2 = values[1]["String"]
        value1_len = values[0]["Length"]
        value2_len = values[1]["Length"]
        answer_len = values[2]["Length"]

        if value2_len >= value1_len >= answer_len:
            print("+", value2, end="    ")
        elif value1_len >= value2_len >= answer_len:
            print_line_when_line_not_biggest(value1_len, value2_len, value2, True, is_sum_list[i])
        else:
            print_line_when_line_not_biggest(answer_len, value2_len, value2, True, is_sum_list[i])
    print()
    i += 1


def print_third_line(values_list):
    for values in values_list:
        value1_len = values[0]["Length"]
        value2_len = values[1]["Length"]
        answer_len = values[2]["Length"]

        max_len = max([value1_len, value2_len, answer_len])
        print("--", end="")
        for i in range(max_len):
            print("-", end="")
        print("    ", end="")
    print()


def print_answers(values_list, is_sum_list):
    i = 0
    for values in values_list:
        answer = values[2]["String"]
        value1_len = values[0]["Length"]
        value2_len = values[1]["Length"]
        answer_len = values[2]["Length"]

        if answer_len >= value1_len >= value2_len:
            print(" ", answer, end="    ")
        elif value1_len >= value2_len >= answer_len:
            print_line_when_line_not_biggest(value1_len, answer_len, answer, False, is_sum_list[i])
        else:
            print_line_when_line_not_biggest(value2_len, answer_len, answer, False, is_sum_list[i])
    print()
    i += 1


def get_problems(problems):
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
        else:
            values = extract_values(problem_str, "-")
        values_list.append(values)
    return [values_list, is_sum_list]


def print_problems(problems):

    problems_list = get_problems(problems)
    values_list = problems_list[0]
    is_sum_list = problems_list[1]

    print_first_line(values_list, is_sum_list)
    print_second_line(values_list, is_sum_list)
    print_third_line(values_list)


def arithmetic_arranger(*args):
    if len(args) == 1 and isinstance(args[0], list):
        problems = args[0]
        problems_list = get_problems(problems)
        values_list = problems_list[0]
        is_sum_list = problems_list[1]
        print_problems(problems)
    elif len(args) == 2 and isinstance(args[1], bool):
        problems = args[0]
        check_answers = args[1]
        problems_list = get_problems(problems)
        values_list = problems_list[0]
        is_sum_list = problems_list[1]
        print_problems(problems)
        if check_answers:
            print_answers(values_list, is_sum_list)
    else:
        raise Exception("Error: Wrong Parameters.")

