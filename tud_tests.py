import builtins

input_values = []
print_values = []


def mock_input(prompt):
    print_values.append(prompt)
    try:
        return input_values.pop(0)
    except IndexError:
        raise Exception("No more mocked inputs available")


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs
