# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 1
# Description:

import os.path
import sys

from problem_1 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_1():
    if not os.path.exists("problem_1.py"):
        sys.exit("Error: problem_1.py not found")

    expected_output = [
        "Digite o valor A: ",
        "Digite o valor B: ",
        "Digite o valor C: ",
        "Digite o valor D: ",
        "Valores recusados."
    ]

    set_keyboard_input([5, 6, 7, 8])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"

    expected_output = [
        "Digite o valor A: ",
        "Digite o valor B: ",
        "Digite o valor C: ",
        "Digite o valor D: ",
        "Valores aceitos."
    ]

    set_keyboard_input([2, 3, 2, 6])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
