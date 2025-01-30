from setuptools import find_packages, setup
from typing import List

''' file_path: str → The function expects a string (the path to the requirements.txt file).
 List[str] → The function will return a list of strings (each representing a package name from the file).
This function will return the list of requirements
'''

Hyphen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path) as file_obj:
        requirements  = file_obj.readlines()
        requirements  = [req.replace('\n',' ')for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)

    return requirements



setup(
name= 'mlproject',
version = '0.0.1',
author='Sai Keerthi',
author_email = 'saikeerthiv11@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)