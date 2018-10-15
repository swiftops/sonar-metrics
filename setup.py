from setuptools import setup, find_packages

setup(
    name='Get Code quality result from Sonar server'
    version='1.0.0'
    description='This service can be used to get scanned results metrics from sonarqube'
    author='Hitesh Bhandari'
    author_email='hbhandari@digite.com'
    url='',
    install_requires=open('requirements.txt').read(),
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.md').read(),
)
