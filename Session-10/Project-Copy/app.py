import sys
import os


from_dir, to_dir = sys.argv[1], sys.argv[2]


def print_dir_tree(path, intent):
    for i in os.listdir(path):
        c_path = os.path.join(path, i)
        print(intent+i)
        if os.path.isdir(c_path):
            print_dir_tree(c_path, intent+"------>")


print_dir_tree(from_dir, "")