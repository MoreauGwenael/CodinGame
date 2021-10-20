import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Tree:
    nb = None
    children = []
    letter = None

    def __init__(self, nb):
        self.nb = nb
        self.children = []

    def get_nb(self):
        return self.nb

    def get_children(self):
        result = []
        for child in self.children:
            result.append(child.get_nb())
        return result

    def add_child(self, nb):
        child = Tree(nb)
        self.children.append(child)

    def get_child(self, nb):
        for child in self.children:
            if child.get_nb() == nb:
                return child

    def get_count(self):
        result = 1
        for child in self.children:
            result += child.get_count()
        return result

    def get_letter(self):
        return self.letter

    def set_letter(self, letter):
        self.letter = letter

    def is_letter(self):
        return self.letter is not None


root = []
n = int(input())
for i in range(n):
    inputs = input().split()
    b = list(map(int, list(inputs[0])))
    c = int(inputs[1])

    result = []
    for node in root:
        result.append(node.get_nb())
    if b[0] in result:
        for node in root:
            if node.get_nb() == b[0]:
                leaf = node
                break
    else:
        leaf = Tree(b[0])
        root.append(leaf)

    for nb in b[1:]:
        if nb in leaf.get_children():
            leaf = leaf.get_child(nb)
        else:
            leaf.add_child(nb)
            leaf = leaf.get_child(nb)

    leaf.set_letter(c)

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

first_nodes = []
for node in root:
    first_nodes.append(node.get_nb())

result = ""
in_letter = False
index = -1
letter_len  = 0
for i in range(len(s)):
    digit = int(s[i])
    if not in_letter:
        if digit in first_nodes:
            for node in root:
                if node.get_nb() == digit:
                    leaf = node
                    in_letter = True
                    letter_len += 1
                    break

            if leaf.is_letter():
                result += chr(leaf.get_letter())
                in_letter = False
                letter_len = 0

        else:
            index = i
            break

    else:
        if digit in leaf.get_children():
            leaf = leaf.get_child(digit)
            in_letter = True
            letter_len += 1

            if leaf.is_letter():
                result += chr(leaf.get_letter())
                in_letter = False
                letter_len = 0

        else:
            index = i
            break

if index != -1:
    print("DECODE FAIL AT INDEX", index - letter_len)

elif in_letter:
    print("DECODE FAIL AT INDEX", len(s) - 1)

else:
    print(result)
