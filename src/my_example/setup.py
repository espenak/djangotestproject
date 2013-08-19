from setuptools import setup, find_packages

setup(name = 'my_example',
      description = 'Example.',
      version = '1.0',
      author = 'Espen A. Kristiansen',
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['distribute', 'Django',],
      include_package_data=True,
      long_description = 'Example.',
      zip_safe=False,
      classifiers=[
                   'Development Status :: 5 - Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
)

