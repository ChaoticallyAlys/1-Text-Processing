from PartA import Path, tokenize, _parse_file


def _print_common(input_file: Path) -> None:
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
    input_file1 = Path(input())
    input_file2 = Path(input())
    _print_common(input_file1)