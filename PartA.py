from pathlib import Path

class Token:
    def __init__(self, token: str) -> None:
        """Initializes Token according to specifications"""
        self._token = "".join([c for c in token.strip().lower() if c.isalnum()])

    def token(self):
        """Gets stored Token information"""
        return self._token

    def __eq__(self, other):
        """Returns true if Tokens are equivalent"""
        return self._token == other.token()

    def __hash__(self):
        """Returns a hash of the str stored in Token"""
        return hash(self._token)

    def __repr__(self):
        """Returns the str stored as its representation"""
        return self._token


def tokenize(text_file_path: Path) -> list[Token]:
    """Parses text file into list of Tokens"""
    token_list = []

    if text_file_path.exists() and text_file_path.is_file():
        file = None
        try:
            file = text_file_path.open('r')
            _parse_file(file, token_list)
            file.close()
        except:
            # file cannot be opened/read
            pass
        finally:
            # always close file
            if file!=None:
                file.close()

    return token_list

def _parse_file(file, token_list: list[Token]):
    """Splits read text into Tokens"""

    while True:
        line = file.readline()
        if line == "":
            break

        for word in line.split():
            token_list.append(Token(word))


def computeWordFrequencies(token_list: list[Token]) -> dict[Token, int]:
    """Counts the occurrences of each Token in the list"""

    token_dict = dict()
    for token in token_list:
        token_dict[token] += 1

    return token_dict