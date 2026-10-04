import sys
from pathlib import Path
from PartA import tokenize, _parse_file


def _print_common(input_file1: Path, input_file2: Path) -> None:
    """Prints common Tokens & num of common Tokens"""

    set1 = set(tokenize(input_file1))

    count = 0
    try:
        with input_file2.open('r') as file:
            # check if the yielded token is already in set1
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
    _print_common(input_file1, input_file2)