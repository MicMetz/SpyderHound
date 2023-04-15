from setuptools import find_packages, setup



setup(
    title='SpyderHound',
    author='MicMetzger',

    version='0.0.1',
    description='A web crawler for hating yourself',

    packages=[],
    package_data={'': ['*.json', '*.png', '*.gif', '*.ico', '*.txt', '*.csv']},

    reqs=open('./requirements.txt', 'r').read().split('\n'),
    install_requires=[],
    dependency_links=[],
)
