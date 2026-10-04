import sys
from PartA import Path, tokenize, _parse_file


def _print_common(input_file: Path) -> None:
    """Prints the num of common Tokens"""

    set1 = set(tokenize(input_file))

    count = 0
    try:
        with input_file2.open('r') as file:
            for t in _parse_file(file):
                if t in set1:
                    count += 1
                    print(t)
                    set1.remove(t)
    except:
        pass

    print(count)


if __name__ == '__main__':
    input_file1 = Path(sys.argv[1])
    input_file2 = Path(sys.argv[2])
    _print_common(input_file1)