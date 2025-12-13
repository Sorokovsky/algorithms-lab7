def choose_number(question: str, minimum: int | None, maximum: int | None, failure_message: str) -> int:
    try:
        number = int(input(question))
        is_in_minimum: bool = minimum is not None and number < minimum
        is_in_maximum: bool = maximum is not None and number > maximum
        if is_in_minimum or is_in_maximum:
            print(failure_message)
            print("Спробуйте ще.")
            return choose_number(question, minimum, maximum, failure_message)
        return number
    except ValueError:
        return choose_number(question, minimum, maximum, failure_message)


def choose_binary(question: str) -> bool:
    bit = choose_number(f"{question}(0-Ні, 1-Так): ", 0, 1, "Відповідь не розпізнано")
    if bit == 0:
        return False
    else:
        return True
