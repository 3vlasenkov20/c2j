import setuptools
import c2j

with open('Readme.md') as fr:
    long_description = fr.read()

setuptools.setup(
    name='c2j',
    version=c2j.__version__,
    author='Vlasenkov A.S.',
    author_email='3vlasenkov20@mail.ru',
    description='.csv-.json transformator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/3vlasenkov20/c2j',
    packages=setuptools.find_packages(),
    install_requires=['pandas >= 1.2.4'],
    test_suite='tests',
    python_requires='>=3.7',
    platforms=["any"]
)