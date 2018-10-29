from setuptools import setup

setup(name='ediblepaste',
        version='0.1',
        description='Wrapper for paste sites API',
        url='http://github.com/ediblesushi/ediblepaste',
        author='ediblesushi',
        author_email='chrisdoucette15@gmail.com',
        license='MIT',
        packages=['ediblepaste'],
        install_requires=[
            'requests'
        ],
        zip_safe=False)
