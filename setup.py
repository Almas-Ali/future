from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


def readme():
    with open('README.md', 'r') as me:
        content = me.read()
        readme = content.split('\n')

    return readme


classifiers = [
    'Development Status :: 1 - Planning',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'Environment :: Console',
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Natural Language :: English',
    'Environment :: Console',
]


setup(
    name='future',
    version='0.0.1',
    packages=find_packages(),
    description="Future - An AI tool for Python 3 (open source).",
    long_description_content_type="text/markdown",
    long_description=readme(),
    url="https://github.com/almas-ali/future",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="AI, FUTURE, ROBOT",
    license="MIT",
    classifiers=classifiers,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        future=future.cli:main
    """,
)
