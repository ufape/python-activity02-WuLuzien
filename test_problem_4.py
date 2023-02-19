# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 4
# Description:

import os.path
import sys

from problem_4 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_4():
    if not os.path.exists("problem_4.py"):
        sys.exit("Error: problem_4.py not found")

    expected_output = [
        "Digite o valor 1/6: ",
        "Digite o valor 2/6: ",
        "Digite o valor 3/6: ",
        "Digite o valor 4/6: ",
        "Digite o valor 5/6: ",
        "Digite o valor 6/6: ",
        "Você digitou 3 valores pares."

    ]

    set_keyboard_input([2, 35, 4, -4, 5, 7])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
