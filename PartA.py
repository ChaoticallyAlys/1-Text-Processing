from pathlib import Path

class BadInput(Exception):
    pass

class Token:
    # O(n) - strip(), lower(), and the for-loop checking for non-English
    # chars takes O(n) time, each, where n is the num of chars in token
    def __init__(self, token: str) -> None:
        """Initializes Token according to specifications"""
        # no spaces & lowercase
        token = token.strip().lower()

        # raises error if non-English char found
        for c in token:
            if not (('a' <= c <= 'z') or ('0' <= c <= '9')):
                raise BadInput

        self._token = token

    # O(1) - returning a string takes O(1) time
    def token(self):
        """Gets stored Token information"""
        return self._token

    # O(n) - comparing a string depends on its length,
    # so it takes O(n) time where n is the num of chars of the shorter string
    def __lt__(self, other):
        """Returns true if Token is less than the other"""
        return self._token < other.token()

    # O(n) - comparing a string depends on its length,
    # so it takes O(n) time where n is the num of chars of the shorter string
    def __le__(self, other):
        """Returns true if Token is less than or equal to the other"""
        return self._token <= other.token()

    # O(n) - comparing a string depends on its length,
    # so it takes O(n) time where n is the num of chars of the shorter string
    def __eq__(self, other):
        """Returns true if Tokens are equivalent"""
        return self._token == other.token()

    # O(n) - hashing a string depends on its length,
    # so it takes O(n) time where n is the num of chars in _token
    def __hash__(self):
        """Returns a hash of the str stored in Token"""
        return hash(self._token)

    # O(1) - returning a string takes O(1) time
    def __repr__(self):
        """Returns the str stored for debugging"""
        return self._token


# O(n) - the for loop calls the generator and appends each
# processed token to the list only once,
# so this takes O(n) time, where n is the num of tokens in the file
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

# O(n) - although each token undergoes multiple operations,
# they are processed only once, thus taking O(n) time,
# where n is the number of tokens in the file
#
# the operations performed on each individual character also
# takes O(n) time, if n is the number of chars in the file
def _parse_file(file):
    """Generates Tokens from read text"""

    while True:
        line = file.readline()
        if line == "":
            break

        # replace all non-alphanumeric chars with space, then split by spaces
        line = "".join(c if c.isalnum() else " " for c in line)
        for word in line.split():
            try:
                t = Token(word)
                yield t
            except BadInput:
                pass


# O(n) - each token in the list is accessed once,
# so this takes O(n) time, where n is the number of tokens in token_list
def computeWordFrequencies(token_list: list[Token]) -> dict[Token, int]:
    """Counts the occurrences of each Token in the list"""

    token_dict = dict()
    for token in token_list:
        if token not in token_dict:
            token_dict[token] = 1
        else:
            token_dict[token] += 1

    return token_dict


# O(n^2) - printing out each token and their count takes O(n) time,
# but _sort_frequencies takes O(n^2), where n is the number of tokens in token_dict
def printFrequencies(token_dict: dict[Token, int]) -> None:
    """Prints the frequencies of each Token"""

    ordered = _sort_frequencies(token_dict)
    for token, count in ordered.items():
        print(f"{token} - {count}")

# O(n^2) - while loop loops through the n tokens in the dict(),
# then removes one, then loops again until the dict() is empty
# n + (n-1) + (n-2)... = n(n+1)/2 = approximately O(n^2) time,
def _sort_frequencies(token_dict: dict[Token, int]) -> dict[Token, int]:
    """Sorts the dict of Tokens by frequency, then alphabetically"""

    ordered = dict()

    largest = None
    largest_count = -1
    # finds the token with the largest count, then appends it to ordered and pops it from token_dict
    # if tokens are tied, then they're chosen alphabetically
    while len(token_dict) != 0:
        for token, count in token_dict.items():
            if largest is None or count > largest_count or (count==largest_count and token < largest):
                largest = token
                largest_count = count

        ordered[largest] = token_dict.pop(largest)

        largest = None
        largest_count = -1

    return ordered