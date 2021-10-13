#!/sw/lang/anaconda.3.8-2020.07/bin/python

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


def get_basis_data(folder):
    output_data = {}
    for grad_dir in os.listdir(folder):
        full_dir = os.path.join(folder, grad_dir)
        if os.path.isdir(full_dir):
            output_data[grad_dir] = get_dir_data(full_dir)

    return pd.DataFrame(output_data)


def get_all_results():
    results = {}
    for folder in os.listdir():
        if not os.path.isdir(folder):
            continue
        if folder[0] == ".":
            continue
        path = os.path.abspath(folder)

        results[folder] = get_basis_data(path)

    return results


def main():
    results = get_all_results()
    for name, df in results.items():
        mapper = {k: name + "_" + k for k in df.keys()}
        results[name] = df.rename(columns=mapper)
        
    pd.concat([df for df in results.values()], axis=1).to_csv("struct_data.csv")


if __name__ == "__main__":
    main()


