from models import Hamster
from binary_search import BST

def get_input_data(filename):
    with open(filename, 'r') as file:
        s = int(file.readline())
        c = int(file.readline())
        bst = BST(lambda x: (x.daily_food, x.daily_food + x.greediness))
        for line in file.readlines():
            val1, val2 = line.split()
            bst.add(Hamster(int(val1), int(val2)))

    return {'s': s, 'c': c, 'hamsters': bst}


def write_data(filename, value_to_write):
    filename = filename.replace('in', 'out')
    with open(filename, 'w') as file:
        file.write(str(value_to_write))
