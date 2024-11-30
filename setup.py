from setuptools import find_packages,setup

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> list[str]:
    '''
    this function will eturn the list of requirements
    '''
    requirements = []
    with open(file_path) as File_obj:
        requirements = File_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
name = 'MLporject',
version= '0.0.1',
author= 'uzman',
author_email= 'ahmeduzman432@gmail.com',
packages= find_packages(),
install_requirements = get_requirements('requirements.txt')

    
)