from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='flask-objectid-converter',
    version='2.0.0',
    description='Provides url converters for flask to support pymonogs ObjectIDs',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/Fischerfredl/flask-objectid-converter',
    author='Alfred Melch',
    author_email='alfred.melch@gmx.de',
    license='MIT',
    classifiers=[
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['flask', 'bson', 'pymongo', 'objectid', 'converter'],
    packages=find_packages(exclude=['tests.*', 'tests']),
    # pymongo uses its own bson implementation. install pymongo instead of bson to prevent bugs
    install_requires=['werkzeug', 'pymongo', 'itsdangerous'],
    test_suite='tests.test_suite',
    tests_require=['flask']
)
