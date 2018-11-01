import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ediblepaste',
    version='1.2.1',
    author='Chris Doucette',
    author_email='chrisdoucette15@gmail.com',
    description='Wrapper for paste sites API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/ediblesushi/ediblepaste',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
