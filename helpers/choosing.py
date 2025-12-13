def choose_number(question: str, minimum: int, maximum: int, failure_message: str) -> int:
    try:
        number = int(input(question))
        if number < minimum or number > maximum:
            print(failure_message)
            print("Спробуйте ще.")
            return choose_number(question, minimum, maximum, failure_message)
        return number
    except ValueError:
        return choose_number(question, minimum, maximum, failure_message)
