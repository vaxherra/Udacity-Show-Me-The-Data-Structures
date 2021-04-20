import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    ### First obtain a list of files and dirs in provided path
    try:
        files_dirs = os.listdir(path)
    except FileNotFoundError:  # path does not exist
        return []
    except NotADirectoryError:  # provided path is a file
        if path.endswith(suffix):
            return [path]
        else:
            return []

    ### Loop over the list of files/dirs in "path"
    return_list = []
    for f in files_dirs:
        return_list += find_files(suffix, f"{path}/{f}")

    return return_list


    pass

if(__name__ == "__main__"):

    # TEST #1 : provided testdir
    print(find_files(".c","testdir"))
    # ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

    # TEST #2: empty directory
    print(find_files(suffix=".py", path="testdir2"))
    # []

    # TEST #3: non-existing directory
    print(find_files(suffix=".py", path="noSuchDirectory"))
    # []

    # TEST #4: custom test dir with .py files
    print(find_files(".py", "testdir3"))
    # ['testdir3/hello.py', 'testdir3/f4/hello.py', 'testdir3/f4/hello3.py', 'testdir3/f4/hello2.py']