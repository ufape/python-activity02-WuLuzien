# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 2
# Description:

import os.path
import sys

from problem_2 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_2():
    if not os.path.exists("problem_2.py"):
        sys.exit("Error: problem_2.py not found")

    expected_output = [
        "Digite o valor A: ",
        "Digite o valor B: ",
        "Digite o valor C: ",
        "Impossível calcular."
    ]

    set_keyboard_input([0.0, 20.0, 5.0])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"

    expected_output = [
        "Digite o valor A: ",
        "Digite o valor B: ",
        "Digite o valor C: ",
        "R1 = -0.025",
        "R2 = -19.684"
    ]

    set_keyboard_input([10.3, 203.0, 5.0])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
