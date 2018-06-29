from setuptools import setup

setup(name='memcheck',
      version='0.1',
      description='Prints the process using the most memory',
      url='',
      author='Dallas Lewis',
      packages=['memcheck'],
      install_requires=[
            'psutil'
      ],
      zip_safe=False)