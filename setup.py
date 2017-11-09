"""Create a Python distribution package setup.py."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest', 'pytest-cov', 'tox']
}


setup(
    name="Data Structures Revision",
    description="Refactored versions of prior implemented data structures",
    version=0.1,
    author="Kurt Maurer",
    author_email="kurtrm@gmail.com",
    license="MIT",
    install_requires=[],
    extras_require=extra_packages
)
