from distutils.core import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='circuitpy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.0.1',
    author='Rafael Acioly',
    author_email='aciolyr@gmail.com',
    packages=['circuitpy'],
    description='A simple circuit breaker implementation',
    keywords=['circuit', 'breaker', 'integration'],
    license="MIT",
    url='https://github.com/rafa-acioly/circuitpy',
    download_url='https://github.com/rafa-acioly/circuitpy'
)
