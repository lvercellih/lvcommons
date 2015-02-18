from setuptools import setup, find_packages
from lvcommons import __version__

setup(
    name='lvcommons',
    version=__version__,
    url='https://github.com/lvercelli/lvcommons',
    author='lvercelli',
    author_email='lvercellih@gmail.com',
    description='Funciones comunes que uso en mis proyectos',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
)
