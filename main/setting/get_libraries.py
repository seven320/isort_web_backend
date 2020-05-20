# encoding:utf-8
import requests
import json
import os

def get_abs_dirname():
    return str(os.path.dirname(os.path.abspath(__file__)))

def get_byhand_libraries():
    path = get_abs_dirname() + "/byhand_libraries.txt"
    with open(path) as f:
        ls = f.readlines()

    byhand_libraries = []
    for l in ls:
        l = l.rstrip("\n")
        byhand_libraries += l.split(",")

    return byhand_libraries

def check_python_text_inlibraries(libraries):
    for library in libraries:
        if "python" in library:
            print(library)
    

def get_new_libraries():
    """
    https://hugovk.github.io/top-pypi-packages/
    を用いてtop4000の有名パッケージを返す
    """
    url = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-365-days.json"
    res = requests.get(url)
    values = json.loads(res.text)
    print(values["last_update"])
    values_rows = values["rows"]

    new_libraries = []
    for values_row in values_rows:
        new_libraries.append(values_row["project"])

    return new_libraries

def get_old_libraries():
    old_libraries = []
    with open(get_abs_dirname() + "/old_libraries.txt") as f:
        ls = f.readlines()
    
    for l in ls:
        l = l.rstrip("\n")
        old_libraries += l.split(",")

    return old_libraries

def update_old_libraries(libraries):
    with open(get_abs_dirname() + "/old_libraries.txt", mode="w") as f:
        f.writelines(",".join(libraries))

def get_libraries():
    libraries = []

    libraries += get_old_libraries()
    libraries += get_new_libraries()
    libraries = list(set(libraries))
    update_old_libraries(libraries)

    libraries += get_byhand_libraries()
    libraries = list(set(libraries))

    return libraries

def make_isort_setting_file():
    libraries = get_libraries()
    # check_python_text_inlibraries(libraries)
    path = get_abs_dirname() + "/isort_exam_setting.txt"
    with open(path) as f:
        ls = f.readlines()

    for i in range(len(ls)):
        if "known_third_party" in ls[i]:
            ls[i] = "known_third_party=" + ",".join(libraries) + "\n"

    # 更新作業
    with open(get_abs_dirname() + "/.isort.cfg", mode = "w") as f:
        f.writelines(ls)
    with open(os.environ["HOME"] + "/.isort.cfg", mode = "w") as f:
        f.writelines(ls)

if __name__ == "__main__":
    # print(len(get_libraries()))
    make_isort_setting_file()
