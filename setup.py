import os
import sys
from setuptools import setup, find_packages
import glob

src_dir = os.path.dirname(__file__)

def get_version(src_dir):
    sys.path.insert(0, src_dir)
    import crier
    return crier.__version__


def read(filename):
    full_path = os.path.join(src_dir, filename)
    with open(full_path) as fd:
        return fd.read()


if __name__ == '__main__':
    setup(
        name='crier',
        version=get_version(src_dir),
        author='Michael Barrett',
        author_email='loki77@gmail.com',
        license="New BSD license",
        url="https://github.com/phobologic/crier",
        description='A simple service/client coordination system.',
        long_description=read('README.rst'),
        classifiers=[
            "License :: OSI Approved :: BSD License",
            "Development Status :: 3 - Alpha"],
        packages=find_packages(),
        scripts=glob.glob(os.path.join(src_dir, 'scripts', '*')),
    )
