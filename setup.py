from setuptools import find_namespace_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    """
    This function reads the requirements from a file and returns a list of packages.
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='tanny',
    author_email='tanny.rhythm2211@gmail.com',
    packages=find_namespace_packages(),
    install_requires=get_requirements('requirements.txt'),

)