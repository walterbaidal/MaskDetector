# Copyright 2020
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys

from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if sys.version_info < (3, 6):
    requirements.append('argparse')

with open('README.md') as f:
    long_description = f.read()

setup(name='MaskDetection',
      version='0.1b0',
      description='Real time mask detector',
      author='Andrés Baidal',
      author_email='walterbaidal96@gmail.com',
      install_requires=requirements,
      # packages=find_packages('.', exclude=["test", "tests"]),
      packages=find_packages('.'),
      # package_data={'': ['config.ini']},  Agregar archivos no python
      include_package_data=True,
      license='Apache License 2.0',
      classifiers=[
          "Development Status :: 1 - Beta",
          "Environment :: Real-Time Mask Detection",
          "License :: OSI Approved :: Apache Software License",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 3.8",
          "Topic :: Mask detection"
      ],
      python_requires='>=3.6',

      entry_points='''
                '''
      )
