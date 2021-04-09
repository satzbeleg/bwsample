from setuptools import setup
import pypandoc


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='bwsample',
      version=get_version("bwsample/__init__.py"),
      description='Sampling algorithm for best-worst scaling sets.',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/ulf1/bwsample',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='Apache License 2.0',
      packages=['bwsample'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.19.5',
          'scipy>=1.5.4',
          'scikit-learn>=0.24.1'
      ],
      python_requires='>=3.6',
      zip_safe=True)
