from setuptools import setup, find_packages
from pathlib import Path
from typing import List


def get_requirements(file_path):
    '''
    Read the requirements.txt file and return the content as a list

    Args:
        - file_path: Path to the requirements.txt file

    Returns:
        - List of requirements
    '''
    HYPHEN_DOT_E = '-e'
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        requirements = [req for req in requirements if not req.startswith(HYPHEN_DOT_E)]
    return requirements


setup(
    name='laptop_price_prediction',
    version='0.0.1',
    author='Ayush Acharya',
    author_email='ayushach007@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements('requirements.txt')
)
