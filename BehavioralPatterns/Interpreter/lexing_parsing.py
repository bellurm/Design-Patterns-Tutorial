import re

# Lexer (Tokenizatör)
def lexer(expression):
    tokens = re.findall(r'\d+|\+|\-|\*|\/', expression)  # Sayılar ve operatörleri ayır

    return tokens

# Parser (Ağaç Oluşturucu)
def parser(tokens):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}  # Operatör öncelikleri

    def precedence(operator):
        return operators.get(operator, 0)

    stack = []
    output = []

    for token in tokens:
        if token.isdigit():  # Sayı ise doğrudan çıktıya ekle
            output.append(token)
        elif token in operators:  # Operatör ise
            while stack and precedence(stack[-1]) >= precedence(token):  # Öncelik kontrolü yap
                output.append(stack.pop())  # Öncelikli operatörleri çıktıya ekle
            stack.append(token)  # Operatörü yığına ekle
        elif token == '(':  # Parantez açma ise
            stack.append(token)  # Yığına ekle
        elif token == ')':  # Parantez kapatma ise
            while stack and stack[-1] != '(':  # Yığın boşalmayana veya parantez açana kadar
                output.append(stack.pop())  # Yığından operatörleri çıkarıp çıktıya ekle
            stack.pop()  # Parantezi yığından çıkar

    while stack:  # Yığında kalan operatörleri çıktıya ekle
        output.append(stack.pop())

    return output

# Örnek kullanım
expression = "3 + 4 * (5 - 2)"
tokens = lexer(expression)
parse_tree = parser(tokens)

print("Tokenler:", tokens)
print("Parse Ağacı:", parse_tree)