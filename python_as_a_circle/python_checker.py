#!/usr/bin/python3
'''checker for python code only'''

import os
import sys
import pydoc


def check_requirements(file_path):
    # Check the first line of the file
    with open(file_path, "r") as f:
        first_line = f.readline().strip()
        if first_line != "#!/usr/bin/python3":
            return False

    # Check if the file ends with a new line
    with open(file_path, "rb") as f:
        f.seek(-1, os.SEEK_END)
        last_byte = f.read(1)
        if last_byte != b'\n':
            return False

    # Check if the file is executable
    if not os.access(file_path, os.X_OK):
        return False

    # Check the number of lines using wc
    lines = os.popen(f"wc -l {file_path}").read().strip().split()[0]
    if int(lines) <= 0:
        return False

    # Check if the module, class, and functions are documented
    try:
        module_name = file_path.replace(".py", "").replace("/", ".")
        module = __import__(module_name)
        module_doc = pydoc.getdoc(module)
        if len(module_doc.strip()) <= 0:
            return False

        for name in dir(module):
            obj = getattr(module, name)
            if hasattr(obj, "__doc__") and len(obj.__doc__.strip()) <= 0:
                return False
    except Exception as e:
        return False

    return True


if __name__ == "__main__":
    # Check the requirements for all Python files in the current directory
    for filename in os.listdir():
        if filename.endswith(".py"):
            if not check_requirements(filename):
                print(f"Requirements not met for {filename}")
                sys.exit(1)

    print("All requirements met for all Python files.")
