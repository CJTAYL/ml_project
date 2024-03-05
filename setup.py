from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Returns list of requirements
    '''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n', '') for req in requirements ]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements 

setup(
name='mlproject',
version='0.0.1',
author='Chris',
author_email='CJTAYL@proton.me',
packages=find_packages(),
install_requries=[get_requirements('requirements.txt')],

)