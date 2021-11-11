from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='metagen',
    version='0.0.1',
    description='Unity `.meta` file generator',
    url='https://github.com/KageKirin/metagen-py',
    author='Chris Helmich',
    author_email='kagekirin@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['metagen'],
    install_requires=[
        'xxhash',
        'colorama',
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

    entry_points={
        'console_scripts': [
            'metagen=metagen.metagen:main',
        ],
    },
)
