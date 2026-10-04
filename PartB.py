from PartA import Path, tokenize, _parse_file

if __name__ == '__main__':
    count = 0

    input_file1 = Path(input())
    input_file2 = Path(input())

    set1 = set(tokenize(input_file1))
    file2 = None
    try:
        file2 = input_file2.open('r')

        for t in _parse_file(file2):
            if t in set1:
                count += 1
                print(t)
                set1.remove(t)

    except:
        # failed to open file
        pass
    finally:
        if file2 is not None:
            file2.close()

    print(count)