
from parser import Parser


parser = Parser(availableTools=[], file="C:/Desk Buddy/TheStackOverflowed/scripts/Player.py")

tree = parser.parse_to_tree()

print(tree)