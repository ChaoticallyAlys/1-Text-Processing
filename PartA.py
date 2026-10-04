from pathlib import Path

class Token:
    def __init__(self, token: str) -> None:
        """Initializes Token according to specifications"""
        self._token = token.strip().lower()

    def token(self):
        """Gets stored Token information"""
        return self._token

    def __lt__(self, other):
        """Returns true if Token is less than the other"""
        return self._token < other.token()

    def __le__(self, other):
        """Returns true if Token is less than or equal to the other"""
        return self._token <= other.token()

    def __eq__(self, other):
        """Returns true if Tokens are equivalent"""
        return self._token == other.token()

    def __hash__(self):
        """Returns a hash of the str stored in Token"""
        return hash(self._token)

    def __repr__(self):
        """Returns the str stored for debugging"""
        return self._token


def tokenize(text_file_path: Path) -> list[Token]:
    """Parses text file into list of Tokens"""
    token_list = []

    try:
        with text_file_path.open('r') as file:
            for t in _parse_file(file):
                token_list.append(t)
    except:
        pass

    return token_list

def _parse_file(file):
    """Generates Tokens from read text"""

    while True:
        line = file.readline()
        if line == "":
            break

        line = "".join(c if c.isalnum() else " " for c in line)
        for word in line.split():
            t = Token(word)

            if t.token() != "":
                yield t


def computeWordFrequencies(token_list: list[Token]) -> dict[Token, int]:
    """Counts the occurrences of each Token in the list"""

    token_dict = dict()
    for token in token_list:
        if token not in token_dict:
            token_dict[token] = 1
        else:
            token_dict[token] += 1

    return token_dict


def printFrequencies(token_dict: dict[Token, int]) -> None:
    """Prints the frequencies of each Token"""

    ordered = _sort_frequencies(token_dict)
    for token, count in ordered.items():
        print(f"{token} - {count}")

def _sort_frequencies(token_dict: dict[Token, int]) -> dict[Token, int]:
    """Sorts the dict of Tokens by frequency, then alphabetically"""

    ordered = dict()

    largest = None
    largest_count = -1

    while len(token_dict) != 0:
        for token, count in token_dict.items():
            if largest is None or count > largest_count or (count==largest_count and token < largest):
                largest = token
                largest_count = count

        ordered[largest] = token_dict.pop(largest)

        largest = None
        largest_count = -1

    return ordered