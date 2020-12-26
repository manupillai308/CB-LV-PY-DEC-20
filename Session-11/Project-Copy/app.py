import sys
import os


from_dir, to_dir = sys.argv[1], sys.argv[2]


def print_dir_tree(path, intent):
    for i in os.listdir(path):
        c_path = os.path.join(path, i)
        print(intent+i)
        if os.path.isdir(c_path):
            print_dir_tree(c_path, intent+"------>")


def copy(from_dir, to_dir):

    for i in os.listdir(from_dir):
        f_path = os.path.join(from_dir, i)
        t_path = os.path.join(to_dir, i)

        if os.path.isdir(f_path):
            if not os.path.exists(t_path):
                os.mkdir(t_path)
                copy(f_path, t_path)
        else:
            from_file = open(f_path, "rb")

            to_file = open(t_path, "wb")

            to_file.write(from_file.read())
            to_file.close()
            from_file.close()






# print_dir_tree(from_dir, "")
copy(from_dir, to_dir)