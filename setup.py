from setuptools import setup

setup(
    name='imageode',
    url='https://github.com/i-rb/imageode',
    author='Ivan Rendo Barreiro',
    author_email='irendo@yahoo.es',
    packages=['imageode'],
    install_requires=['numpy'], #more
    version='0.1',
    license='MIT',
    description='A package for plotting easily linear systems',
    long_description=open('README.md').read(),
)
