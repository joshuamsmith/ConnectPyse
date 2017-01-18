from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='connectpyse',
      version='0.1',
      description='A ConnectWise API tool for the rest of us.',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5'
      ],
      keywords='connectwise rest api',
      url='https://github.com/joshuamsmith/ConnectPyse',
      author='Joshua M Smith',
      author_email='saether@gmail.com',
      license='MIT',
      packages=['connectpyse'],
      install_requires=[
          'restapi-client',
      ],
      include_package_data=True,
      zip_safe=False)
