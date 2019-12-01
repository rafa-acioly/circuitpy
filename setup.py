from distutils.core import setup

setup(
    name='circuitpy',
    long_description=open('README.md').read(),
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
