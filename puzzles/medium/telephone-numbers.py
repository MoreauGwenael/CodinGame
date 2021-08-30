import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Tree:
    nb = None
    children = []

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


n = int(input())
numbers = []
for i in range(n):
    telephone = list(map(int, list(input())))
    result = []
    for child in numbers:
        result.append(child.get_nb())
    if telephone[0] in result:
        for child in numbers:
            if child.get_nb() == telephone[0]:
                node = child
                break
    else:
        node = Tree(telephone[0])
        numbers.append(node)
    for nb in telephone[1:]:
        if nb in node.get_children():
            node = node.get_child(nb)
        else:
            node.add_child(nb)
            node = node.get_child(nb)



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# The number of elements (referencing a number) stored in the structure.
result = 0
for child in numbers:
    result += child.get_count()
print(result)
