from tests import run_tests
from ReferenceManual import create_reference_manual


def main():
    # Running tests
    run_tests()

    # Generating reference manual
    manual = create_reference_manual()
    print(manual)


if __name__ == '__main__':  
    main()
