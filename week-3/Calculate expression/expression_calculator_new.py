"""buyfytcjjfgcjytcytg"""


def calculate_expression(expression):
    """
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    """
    err = "Неправильний вираз!"
    if isinstance(expression, str):
        words = expression.split(" ")
        if (
            words[0] == "Скільки"
            and words[1] == "буде"
            and words[len(words) - 1][-1] == "?"
        ):
            expression = expression.replace("додати", "+")
            expression = expression.replace("відняти", "-")
            expression = expression.replace("мінус", "-")
            expression = expression.replace("помножити на", "*")
            expression = expression.replace("поділити на", "/")
            expression = expression.replace("?", "")
            expression = expression.replace("Скільки буде ", "")
            words = expression.split(" ")
            expression = expression.replace(" + ", "")
            expression = expression.replace(" - ", "")
            expression = expression.replace(" * ", "")
            expression = expression.replace(" / ", "")
            for i in expression:
                if not i.isnumeric() and i != "-":
                    return err
            ans = int(words[0])
            for i in range(1, len(words), 2):

                match words[i]:
                    case "+":
                        ans += int(words[i + 1])
                    case "-":
                        ans -= int(words[i + 1])
                    case "*":
                        ans *= int(words[i + 1])
                    case "/":
                        if words[i + 1] != "0":
                            ans /= int(words[i + 1])
                        else:
                            return err

            return int(ans)
    return err
