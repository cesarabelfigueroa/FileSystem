from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='FileSystem',
      version=version,
      description="Operative Systems 2.1",
      long_description="""\
file system""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='cesarfigueroa',
      author_email='cesarabelfigueroa@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
