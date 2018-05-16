import pathlib
import argparse


def split(file_in):

    files = open(file_in, 'r').read().split('$$$$')
    base_name = 'file_'
    for i, file in enumerate(files):
        path = f'/opt/data/{base_name}{i}'
        pathlib.Path(path).mkdir()  # create dir
        open(f'{path}/{base_name}{i}.sdf', 'w').write(file)  # create path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args()

    split(args.file)
