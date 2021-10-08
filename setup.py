try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='randa_test',
    version= '0.0.1',
    url='https://github.com/randalee/setuptools_test',
    author='RandaLee',
    author_email='ruciain@gmail.com',
    packages=['randalee'],
    license='GPL License',
    install_requires=[
        'requests',
    ],
    description='seuptools test code',
    long_description='Testing-- setuptools'
)
