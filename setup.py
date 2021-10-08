try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='randa_test',
    version= '0.0.2',
    url='https://github.com/randalee/setuptools_test',
    author='RandaLee',
    author_email='ruciain@gmail.com',
    packages=['randalee', 'randalee.t1'],
    license='GPL License',
    install_requires=[
        'requests',
    ],
    description='seuptools test code',
    long_description='Testing-- setuptools'
)
