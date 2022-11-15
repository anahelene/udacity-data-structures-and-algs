import os


def find_files_helper(suffix, path, list_of_paths):
    if not os.path.isdir(path):
        return list_of_paths

    for branch in os.listdir(path):
        path_name = path + '/' + branch

        if branch.endswith(suffix):
            list_of_paths.append(path_name)
        else:
            find_files_helper(suffix, path_name, list_of_paths)

    return list_of_paths


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    list_of_paths = find_files_helper(suffix, path, [])
    return list_of_paths

print(find_files('.h','testdir'))
# expected output is ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h']

print(find_files('.c','testdir'))
# expected output is ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

print(find_files('.py', 'testdir'))
# expected output is [], since there are no .py files in testdir

print(find_files('.py', 'problem2.py'))
# expected output is [], since problem2.py is not a directory.

print(find_files('', ''))
# expected output is [] since the empty strings are not valid suffixes nor valid path.
