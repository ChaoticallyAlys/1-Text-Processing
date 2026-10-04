from PartA import Path, tokenize, _parse_file

if __name__ == '__main__':
    count = 0

    input_file1 = Path(input())
    input_file2 = Path(input())

    set1 = set(tokenize(input_file1))
    with input_file2.open('r') as file:
        for t in _parse_file(file):
            if t in set1:
                count += 1
                print(t)
                set1.remove(t)

    print(count)