from pathlib import Path

class Token:
    def __init__(self, token: str) -> None:
        """Initializes Token"""
        self._token = token

    def token(self):
        """Gets stored Token information"""
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
            if word.isalnum():
                token_list.append(Token(word.strip().lower()))