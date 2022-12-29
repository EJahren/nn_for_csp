from typing import List, Tuple


def parse_txt_input(
    text_input: str,
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, List[bool]]]]:
    """Parses the problems in the txt files format given by csplib.

    returns a tuple of the list of option limitations and list of car classes,
    i.e., ([(1, 3),(2, 5)], [(4, [True, False]), (2, [False, True])) means the
    problem has two options with capacity 1/3 and 2/5, and two classes
    where one should produce 4 of the first kind and 2 of the second
    kind. The first class of car should be fitted with the first option
    and the second class of car should be fitted with the second option.
    """
    numbers = [
        [int(number) for number in line.split()]
        for line in text_input.split("\n")
        if line != ""
    ]
    if numbers == []:
        raise ValueError("Missing header line for input")
    if len(numbers[0]) < 3:
        raise ValueError(f"Header line {numbers[0]} has too few numbers")
    header = numbers[0]
    num_cars = header[0]
    num_options = header[1]
    num_classes = header[2]

    if len(numbers[1]) != len(numbers[2]) or len(numbers[1]) != num_options:
        raise ValueError(
            f"Incorrect number of options in {numbers[1],numbers[2]} should be {num_options}"
        )

    options = list(zip(numbers[1], numbers[2]))

    if num_classes != len(numbers[3:]):
        raise ValueError(
            f"mismatch in number of classes:"
            f" {num_classes} in header, actual: {len(numbers[3:])}"
        )
    if num_cars != sum(c[1] for c in numbers[3:]):
        raise ValueError("mismatch in number of cars")

    return (options, [(car[1], [(o != 0) for o in car[2:]]) for car in numbers[3:]])


def show_problem(
    problem: Tuple[List[Tuple[int, int]], List[Tuple[int, List[bool]]]]
) -> str:
    """Performs the inverse action of parse_txt_input: outputs it to str"""
    options = problem[0]
    classes = problem[1]
    num_cars = sum(c[0] for c in classes)
    num_options = len(options)
    num_classes = len(classes)

    result = f"{num_cars} {num_options} {num_classes}\n"

    result += " ".join([str(o[0]) for o in options]) + "\n"
    result += " ".join([str(o[1]) for o in options]) + "\n"

    for i, c in enumerate(classes):
        result += f"{i} {c[0]} "
        options = c[1]
        result += " ".join(["1" if o else "0" for o in options])
        result += "\n"
    return result
