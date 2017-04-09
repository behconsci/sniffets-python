from distutils.core import setup

try:
    with open('README.rst') as file:
        long_description = file.read()
except IOError:
    long_description = 'Python lib for apptrackly'

setup(
    name='sniffets',
    packages=['sniffets'],
    version='0.2.2',
    long_description=long_description,
    description='Python lib for sniffets.com',
    author='Doniyor Jurabayev',
    author_email='behconsci@gmail.com',
    url='https://github.com/behconsci/apptracklypython',
    download_url='https://github.com/behconsci/apptracklypython/archive/0.2.2.tar.gz',
    keywords=['track', 'monitor', 'bug'],
    classifiers=[],
    install_requires=[
        'requests', 'grequests'
    ],
)
