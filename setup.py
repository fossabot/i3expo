from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setup(name='i3expo',
      version='0.3.1',
      description='Provide a workspace overview for i3wm',
      long_description=long_description,
      url='https://github.com/mihalea/i3expo',
      author='Mircea Mihalea, Josh Walls',
      author_email='mircea@mihalea.rp, me@joshwalls.co.uk',
      license='GPL',
      zip_safe=False,
      install_requires=requirements,
      py_modules=['i3expo'],
      entry_points={
          'console_scripts': [
              'i3expo=i3expo:main'
          ]
      })
