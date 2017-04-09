from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='apptrackly',
    packages=['apptrackly'],
    version='0.2',
    long_description=long_description,
    description='Python lib for apptrackly',
    author='Doniyor Jurabayev',
    author_email='behconsci@gmail.com',
    url='https://github.com/behconsci/apptracklypython',
    download_url='https://github.com/behconsci/apptracklypython/archive/0.2.tar.gz',
    keywords=['track', 'monitor', 'bug'],
    classifiers=[],
)
