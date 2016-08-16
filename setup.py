#Write the libraries
from setuptools import setup
#from setuptools import setup,find_packages
setup(name='neuroman',
      version=0.1,
      description='Neuroman',
      url='http://github.com/chaneyn/neuroman',
      author='Nathaniel W. Chaney',
      author_email='nchaney@princeton.edu',
      license='MIT',
      packages=['neuroman',],
      package_data={'neuroman':['*.txt'],},
      include_package_data=True,
      )
