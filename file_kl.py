from pathlib import Path

def folders_in_path(path):
    if not Path.is_dir(path):
        raise ValueError("argument is not a directory")
    yield from filter(Path.is_dir, path.iterdir())

def folders_in_depth(path, depth):
    if 0 > depth:
        raise ValueError("depth smaller 0")
    if 0 == depth:
        yield from folders_in_path(path)
    else:
        for folder in folders_in_path(path):
            yield from folders_in_depth(folder, depth-1)

def files_in_path(path):
    if not Path.is_dir(path):
        raise ValueError("argument is not a directory")
    yield from filter(Path.is_file, path.iterdir())

def sum_file_size(filepaths):
    return sum([filep.stat().st_size for filep in filepaths])

if __name__ == '__main__':
    for folder in folders_in_depth(Path.cwd(),1):
        #       vvvv quick hack to to use len(), does not perform well
        files = list(files_in_path(folder))
        total_size = sum_file_size(files)
        print(f'{folder}: filecount:{len(files)}, total size:{total_size}')