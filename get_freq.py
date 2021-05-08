import os
import pandas as pd

def get_mol_data(folder: str, file: str):
    mol = file.split(".")[0]
    i = 0
    print_lines = False
    results = {}
    for line in open(os.path.join(folder, file)):
        if print_lines:
            i += 1
            if i > 1:
                if line == '\n':
                    break
                if "Saving results in set" in line:
                    print_lines = False
                    output = ''
                    i = 0
                    continue
                l = line.split(' ')
                l = [x for x in l if x != '']
                if 'i' in l:
                    print("Not minimised: {}".format(mol))
                    return
                assert len(l) == 2, l
                fn = int(l[0])
                if mol in ["02_C2H2", "08_ClCN", "10_CO2", "12_CS2", "20_HCN", "26_N2O", "27_OCS"]:
                    if i == 2:
                        results[mol + "_" + str(fn)] = float(l[1])
                    fn += 1
                results[mol + "_" + str(fn)] = float(l[1])
        if "Vibrational frequencies" in line:
            print_lines = True

    return results

def get_results(folder):
    all_results = {}
    for file in os.listdir(folder):
        if file.endswith(".out"):
            mol_results = get_mol_data(folder, file)
            all_results = {**all_results, **mol_results}

    return all_results


def main(folder):
    all_results = {}
    for freq_dir in os.listdir(folder):
        full_dir = os.path.join(folder, freq_dir)
        if os.path.isdir(full_dir):
            all_results[freq_dir] = get_results(full_dir)
    
    pd.DataFrame(all_results).to_csv("freq_data.csv") 


if __name__ == '__main__':
    import sys
    folder = sys.argv[1]
    path = os.path.abspath(folder)
    print(path)
    main(path)

