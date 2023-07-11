class TokenType:
    FUNC = "FUNC"
    EXPR = "EXPR"
    EOF = "EOF"
    BRACK = "BRACK"

class Token:

    def __init__(self, type:TokenType, val):
        self.type = type
        self.val = val

    def __str__(self) -> str:
        return f"Token is of type {self.type} and has a value of {self.val}."

    def __repr__(self) -> str:
        return str(self)

if __name__ == "__main__":
    print(Token("bye", "now"))