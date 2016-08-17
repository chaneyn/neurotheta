#Write the libraries
from setuptools import setup
#from setuptools import setup,find_packages
setup(name='neurotheta',
      version=0.1,
      description='NeuroTheta',
      url='http://github.com/chaneyn/neurotheta',
      author='Nathaniel W. Chaney',
      author_email='nchaney@princeton.edu',
      license='MIT',
      packages=['neurotheta',],
      package_data={'neurotheta':['*.txt'],},
      include_package_data=True,
      )
