import pkgutil
import pprint
import sys

from metarch.core import qt_app
from metarch.core.alphadeesp import AlphaDeesp
from metarch.katas import kata1


# def test(txt):
#     prev2 = None
#     for word2 in vocab_list:
#         prev = None
#         for elem in sentence2:
#             if prev == prev2 and elem == word2:
#             # do something
#             prev = elem
#         prev2 = word2


def mytest(argv):
    prev = None
    for word in argv:
        for letter in word:
            if prev == "-" and letter == "h":
                return True
            prev = letter
    return False


def is_help_in_args(argv):
    for word in argv:
        for letter in word:
            print(f"letter : {letter} and letter.next : {letter.next()}")
            if "-" in letter and "h" in letter.next():
                print(f"letter : {letter} and letter.next : {letter.next()}")
                return True
    return False


if __name__ == "__main__":
    print("sysargv = ", sys.argv)

    # print(f"There is -h in sysargv: {is_help_in_args(sys.argv)}")
    print(f"There is -h in sysargv: {mytest(sys.argv)}")

    if "alphadeesp" in sys.argv:
        print("Metarch initializes... Power grid network tools")
        print("...")
        print("AlphaDeesp subroutine loaded")

        alphadeesp = AlphaDeesp()
        alphadeesp.run()

    elif "--ex1" in sys.argv:
        # ex1 started by Metarch
        print("Starting ex1...")

        # search_path = ['.']  # set to None to see all modules importable from sys.path
        search_path = None
        all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
        # print("from run.py file =", all_modules)

        p = pprint.PrettyPrinter(compact=True)
        p.pprint(all_modules)

        # run_exercice("ex1")

    elif "--hots" in sys.argv:
        print("lauching Hots stats module...")

    elif "--hots" and is_help_in_args in sys.argv:
        print("possibilities are:")
        print("--hots-load,"
              "--hots-compute")

    elif "--kata1" in sys.argv:
        print("launching Kata1 module...")
        kata1.run()

    elif "qt" in sys.argv:
        print("Starting Qt Qml example")

        app = qt_app.run(sys)
        sys.exit(app)
