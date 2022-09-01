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
    sub_dirs = os.listdir(path)
    found_paths = []
    for dir in sub_dirs:
        if os.path.isfile(f'{path}/{dir}'):
            if f'{path}/{dir}'.endswith(suffix):
                found_paths.append(path)
        else:
            found_paths.extend(find_files(suffix, f'{path}/{dir}'))

    return found_paths


if __name__ == '__main__':
    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1
    print(find_files('.h', 'testdir'))
    # Expected result: ['testdir/subdir3/subsubdir1', 'testdir/subdir5', 'testdir', 'testdir/subdir1']

    # Test Case 2
    # print(find_files('.f', 'testdir'))
    # Expected result: []

    # Test Case 3
    # print(find_files('.f', 'unknown/directory'))
    # Expected result: FileNotFoundError: [Errno 2] No such file or directory: 'unknown/directory'
