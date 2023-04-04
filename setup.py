from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:

    '''
    This function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
        requirements = [req for req in requirements if not req.startswith('-e')]

    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Rohan',
author_email = 'rohan.calculus@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)