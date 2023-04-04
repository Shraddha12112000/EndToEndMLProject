#This setup.py will be responsible for creating Machine Learning Application as a Package. And deploy in pypi 
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #one one Line will be readed and when we go to nextLine there will be \n will get added. convert \n to blank 
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name ='mlproject',
    version='0.0.1',
    author='Shraddha Gujar',
    author_email='gujarshraddha13@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')




)