from FindColorcode import MAJOR_COLORS, MINOR_COLORS, Collect_pair_number_from_color, color_pair_to_string


def create_reference_manual():
    manual = []
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            pair_number = Collect_pair_number_from_color(major, minor)
            manual.append(f'{pair_number:2d} - {color_pair_to_string(major, minor)}')
    return '\n'.join(manual)


if __name__ == '__main__':
    manual = create_reference_manual()
    print(manual)

