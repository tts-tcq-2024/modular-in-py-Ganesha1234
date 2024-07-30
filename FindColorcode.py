MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]


def format_color_pair_string(major_color, minor_color):
    return f'{major_color} {minor_color}'


def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise Exception('Minor index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_color_index(color, color_list):
    try:
        return color_list.index(color)
    except ValueError:
        raise Exception(f'{color} index out of range')


def get_pair_number_from_color(major_color, minor_color):
    major_index = get_color_index(major_color, MAJOR_COLORS)
    minor_index = get_color_index(minor_color, MINOR_COLORS)
    return major_index * len(MINOR_COLORS) + minor_index + 1
