from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='ConnectPyse',
      version='0.2',
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
      packages=['', 'system', 'company', 'finance', 'service'],
      install_requires=[
          'requests',
          'ujson'
      ],
      include_package_data=True,
      zip_safe=False)
