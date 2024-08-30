### We have made this file so that our project can be made as packages that can be installed or import like other packages

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
  '''
  this function will return the list of requirements
  '''
  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n","") for req in requirements]



setup(
name="ML_PROJECT",
version="0.0.1",
author="Arjun",
author_email="arjun.gupta.nit17@gmail.com",
packages=find_packages(),  ### This find_packages will check for __init__ file for every folder and make that as a package
install_requires=get_requirements('requirements.txt')
)