from tests import run_tests


def create_reference_manual():
    manual = []
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            pair_number = Collect_pair_number_from_color(major, minor)
            manual.append(f'{pair_number:2d} - {color_pair_to_string(major, minor)}')
    return '\n'.join(manual)
  


if __name__ == '__main__':  
     # Running tests
    run_tests()

    # Generating reference manual
    manual = create_reference_manual()
