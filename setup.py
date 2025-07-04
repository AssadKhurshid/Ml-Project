from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> list[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    # Remove any comments or empty line
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='Ml-Project',
    version='0.1.0',
    author='Assad Khurshid',
    author_email='assadkhurshid91@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)