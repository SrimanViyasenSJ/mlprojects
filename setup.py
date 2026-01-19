from setuptools import setup, find_packages


def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name = "mlprojects",
    version="3.13.9",
    author="Sriman Viyasen S J",
    author_email="sjsrimanviyasenofficial@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)