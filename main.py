from tests import run_tests
from manual import create_reference_manual


def main():
    # Running tests
    run_tests()

    # Generating and printing the reference manual
    manual = create_reference_manual()
    print('Color Code Reference Manual:')
    print(manual)


if __name__ == '__main__':
    main()
