"""A setup script for the package to distribute it to PyPi."""
from setuptools import setup


def readme():
    """Return the contents of the README file for this project."""
    with open('README.md') as readme_file:
        return readme_file.read()


setup(
    name='semver-setuptools-git-version',
    url='https://github.com/jsporna/semver-setuptools-git-version',
    author='Jakub Spórna',
    author_email='jakub.sporna@gmail.com',
    description='Automatically set package version using git tags with semver ordering.',
    version="1.0.0",
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords='setuptools git version-control semver',
    license='MIT',
    classifiers=[
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
    ],
    py_modules=['semver_setuptools_git_version'],
    install_requires=[
        'setuptools >= 8.0',
    ],
    entry_points={
        'distutils.setup_keywords': [
            'version_config = semver_setuptools_git_version:validate_version_config'
        ],
        'console_scripts': [
            'semver-setuptools-git-version = semver_setuptools_git_version:get_version'
        ]
    }
)
