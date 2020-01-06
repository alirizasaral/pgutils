import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='pgutils',  
    version='0.1.0',
    py_modules=['pgutils'],
    install_requires=[
    'Click',
    'shell_utils',
    ],
    entry_points='''
    [console_scripts]
    pgutils=pgutils:cli
    ''',
    author="Ali Riza Saral",
    author_email="aliriza.saral@gmail.com",
    description="Various utilities for Postgres.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alirizasaral/pgutils",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.6'
 )