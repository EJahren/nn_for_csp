import ast
import re


def _read_header(stream):
    """
    Simply reads and checks that the first line is "language Essence 1.3"
    """
    header = next(stream)
    if header != "language Essence 1.3\n":
        raise ValueError(f"Unexpected header {header}")


def _skip_comments(stream):
    """
    skip lines starting with '$' and return the first non-comment line
    """
    line = next(stream)
    while line[0] == "$":
        line = next(stream)
    return line


def _parse_let_statement(line):
    """
    parses one 'letting' statement as it pertains to csp.
    """
    words = line.split(" ")

    def _parse_int():
        if words[2] != "be":
            raise ValueError(f"Could not parse {line}")
        return int(words[3])

    def _parse_function():
        if words[2:4] != ["be", "function"]:
            raise ValueError(f"Could not parse {line}")
        function_def = " ".join(words[4:])
        if function_def[0] != "(":
            raise ValueError(
                f"Expected function definition {function_def} to start with parenthesis"
            )
        if function_def[-2:] != ")\n":
            raise ValueError(
                f"Expected function definition {function_def} to end with parenthesis"
            )
        function_def = [re.split("-->", a) for a in function_def[1:-2].split(",")]
        return {int(k): int(v) for k, v in function_def}

    def _parse_relation():
        if words[2:4] != ["be", "relation"]:
            raise ValueError(f"Could not parse {line}")
        return ast.literal_eval(" ".join(words[4:]))

    if words[0] != "letting":
        raise ValueError(f"Expected line to start with 'letting', but got {words[0]}")
    for var in ["n_cars", "n_classes", "n_options"]:
        if words[1] == var:
            return {var: _parse_int()}

    for var in ["maxcars", "blksize", "quantity"]:
        if words[1] == var:
            return {var: _parse_function()}
    if words[1] == "usage":
        return {"usage": _parse_relation()}

    raise ValueError(f"Could not parse {line}")


def parse_param_file(file_name):
    if isinstance(file_name, str):
        fp = open(file_name, "r")
    else:
        fp = file_name
    _read_header(fp)
    first_line = _skip_comments(fp)
    assignments = _parse_let_statement(first_line)
    for line in fp:
        if line == "\n":
            continue
        assignments.update(**_parse_let_statement(line))
    ratios = []
    classes = []
    for i in range(1, assignments["n_options"] + 1):
        ratios.append((assignments["maxcars"][i], assignments["blksize"][i]))
    for i in range(1, assignments["n_classes"] + 1):
        classes.append(
            (
                assignments["quantity"][i],
                [
                    (i, o) in assignments["usage"]
                    for o in range(1, assignments["n_options"] + 1)
                ],
            )
        )
    return (ratios, classes)
