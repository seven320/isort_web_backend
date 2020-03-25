# encoding:utf-8
import requests
import json

def get_libraries():
    """
    https://hugovk.github.io/top-pypi-packages/
    を用いてtop4000の有名パッケージを返す
    """
    url = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-365-days.json"
    res = requests.get(url)
    values = json.loads(res.text)
    print(values["last_update"])
    values_rows = values["rows"]

    libraries = []
    for values_row in values_rows:
        libraries.append(values_row["project"])

    return libraries

def make_isort_setting_file():
    new_libraries = get_libraries()
    path = "setting/isort_setting.txt"
    with open(path) as f:
        ls = f.readlines()

    for i in range(len(ls)):
        if "known_third_party" in ls[i]:
            libraries = ls[i].rstrip("\n").split("=")[-1].split(",")
            libraries = list(set(libraries + new_libraries)) # add new
            ls[i] = "known_third_party=" + ",".join(libraries) + "\n"

    with open(path, mode = "w") as f:
        f.writelines(ls)

if __name__ == "__main__":
    make_isort_setting_file()
