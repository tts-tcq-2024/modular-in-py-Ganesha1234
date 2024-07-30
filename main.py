from tests import run_tests  
from FindColorcode import  MAJOR_COLORS,MINOR_COLORS,get_pair_number_from_color,format_color_pair_string

def generate_reference_manual():
    reference_manual = [
        f'{get_pair_number_from_color(major_color, minor_color):2d} - {format_color_pair_string(major_color, minor_color)}'
        for major_color in MAJOR_COLORS
        for minor_color in MINOR_COLORS
    ]
    return '\n'.join(reference_manual)

if __name__ == '__main__':
    # Running tests
    run_tests()

    # Generating reference manual
    reference_manual = generate_reference_manual()

