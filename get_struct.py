import os
import pandas as pd

def get_mol_data(folder: str, file: str):
    mol = file.split(".")[0]
    j = 0
    print_lines = False
    mol_data = {}
    for line in open(os.path.join(folder, file)):
        if print_lines:
            if line == '\n':
                break
            l = line.split(' ')
            l = [x for x in l if x != '']
            assert len(l) == 4, l
            for k in range(1, 4):
            #    print("{}_{}:\t{:.9f}".format(mol, str(j), float(l[k])))
                mol_data[mol + "_" + str(j)] = float(l[k])
                j += 1
        if "Final structure" in line:
            print_lines = True

    return mol_data


def get_dir_data(folder):
    all_data = {}
    for file in os.listdir(folder):
        if file.endswith(".out"):
            mol_data = get_mol_data(folder, file)
            all_data = {**all_data, **mol_data}

    return all_data


def main(folder):
    output_data = {}
    for grad_dir in os.listdir(folder):
        full_dir = os.path.join(folder, grad_dir)
        if os.path.isdir(full_dir):
            output_data[grad_dir] = get_dir_data(full_dir)

    pd.DataFrame(output_data).to_csv("struct_data.csv")


if __name__ == '__main__':
    import sys
    folder = sys.argv[1]
    path = os.path.abspath(folder)
    print(path)
    main(path)

