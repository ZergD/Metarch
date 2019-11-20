import os
import sys
import pprint
import pkgutil
from pathlib import WindowsPath, Path

from metarch.exercices.exercice1 import ex1


def run_exercice(num_ex: str):
    """This function runs exercice num_ex"""
    print("Running exercice n°", num_ex)
    ex_path = WindowsPath("./metarch/exercices/exercice1/" + num_ex + ".py")

    t = Path(".")
    all_python_files_in_subdirs = list(t.glob("**/*.py"))

    if ex_path in all_python_files_in_subdirs:
        print(os.system(str(ex_path)))

    pass
    # ex1.draf()


# print("sys.path = ", sys.path)
# sys.path.append(sys.path[0] + "./metarch/exercices/")
# pprint.pprint(sys.path)
# # res = os.system("echo %cd%")
# # print("res =", res)
# print("current path = ", sys.path[0])
# print("pwd = ", os.system("cd"))
# print("=============================== sys.builtin_module_names ===============================")
# # print(sys.builtin_module_names)
# # pprint.pprint(sys.builtin_module_names)
#
# search_path = ['.'] # set to None to see all modules importable from sys.path
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print("from __init__ file =", all_modules)
#
#
#
# ex_path = WindowsPath("./metarch/exercices/exercice1/ex1.py")
# sub_dirs = [x for x in ex_path.iterdir() if x.is_dir()]
# print(sub_dirs)
#
#
#
# for s in current_path.iterdir():
#     if s.is_dir():
#         n_path = WindowsPath(s.name)
#         sub_dirs = [x for x in n_path.iterdir() if x.is_dir()]
#         print(sub_dirs)

