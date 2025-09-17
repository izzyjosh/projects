import os

def create(dirname: str) -> None:
    # check if the path exist
    basedir: str = os.getcwd()
    
    try:
        if type(dirname).__name__ == "tuple":
            for name in dirname:
                os.mkdir(os.path.join(basedir, name))
        else:
            os.mkdir(os.path.join(basedir, dirname))
    except FileExistsError:
        print("Directory name already exist")


def remove(dirname: str) -> None:
    basedir: str = os.getcwd()

    try:
        os.rmdir(os.path.join(basedir, dirname))
    except FileNotFoundError:
        print("Directory does not exist")


def rename(src: str, dst: str) -> None:

    try:
        if not os.path.exists(src):
            print("src does not exist")
            return
        if os.path.exists(dst):
            print("dst already exists")
            return
        os.rename(src, dst)

    except Exception as e:
        print(f"Error: {e}")


def del_file(filename: str) -> None:
    try:
        if not os.path.exists(filename):
            print("File does not exist")
            return
        if not os.path.isfile(filename):
            print("Nkt a file")
            return 
        os.remove(filename)
    except Exception as e:
        print(f"Error: {e}")


def create_file(filename: str)-> None:
    basedir: str = os.getcwd()

    if os.path.exists(filename):
        print("file already exist")
        return 
    else:
        with open(os.path.join(basedir, filename), "w") as f:
            f.write("")


