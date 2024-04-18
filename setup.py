#setup.py is building the app as a package

from setuptools import setup,find_packages
from typing import List # type: ignore

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    Description: This function is used to read the requirements.txt file and return a list of requirements
    """
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n","") for r in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Predictive Modeling for Insurance Premiums Based on Population Trends',#Name of the project
    version='1.0.0',#Version of the project
    packages=find_packages(),#List of packages it goes to src and every file called __init__.py
    url='https://github.com/BerghazHatim/mlproject_krish',#URL of the project
    author='Berghazhatim',#Author of the project
    author_email='berghazhatim6@gmail.com',#Email of the project
    install_requires=get_requirements('requirements.txt')#List of requirements
)