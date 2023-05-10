import os

from setuptools import find_packages, setup



pkg_name = 'SpyderHound'

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

with open('README.md') as f:
    readme = f.read()

with open(os.path.join(pkg_name, 'sassyBot/__init__.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip("'")
            break
    else:
        version = '0.0.1'

setup(
    name=pkg_name,
    author='MicMetzger',
    url='https://github.com/MicMetz/SpyderHound',

    version=version,
    description='A web crawler for hating yourself',
    long_description=readme,


    install_requires=open('./requirements.txt', 'r').read().split('\n'),
    packages=find_packages(exclude=['tests', 'tests.*', 'docs', 'docs.*', 'venv', 'venv.*']),
    package_data={'': ['*.json', '*.txt', '*.csv', '*.xml', '.lxml', '*.gif', '*.png', '*.ico', '*.jpg', '*.jpeg', '*.svg']},

    dependency_links=[],
)
