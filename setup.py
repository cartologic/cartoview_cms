from distutils.core import setup
from setuptools import find_packages

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
setup(
    name='cartoview_cms',
    packages=find_packages(),
    version='1.7.5',
    description='Content Management System for Cartoview',
    long_description=long_description,
    author='Cartologic',
    author_email='info@cartologic.com',
    url='https://github.com/cartologic/cartoview_cms',
    include_package_data=True,
    keywords=['cartoview', 'gis', 'geonode', "django", "web mapping", "applications", "apps", "cms", "wagtail"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 1.8",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    license="BSD",
    install_requires=['cartoview']
)
