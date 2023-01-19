import os
from setuptools import setup, find_packages

VERSION = '0.1.5'

def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path) as file:
        content = file.read()
    return content if content else 'no content read'

setup(
    name="mkdocs-risonia-theme",
    version=VERSION,
    url='https://github.com/unverbuggt/mkdocs-risonia-theme',
    description='A simple theme for MkDocs using using the w3.css framework and configurable color schemes',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs theme python markdown',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs',
        'beautifulsoup4',
    ],
    author='René Rüthlein',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'risonia = risonia_theme',
        ],
        'mkdocs.plugins': [
            'risonia/color-theme = risonia_theme.plugins.color.plugin:W3cssColorTheme',
            'risonia/w3css-classes = risonia_theme.plugins.classes.plugin:W3cssClassesPlugin'
        ]
    },
    zip_safe=False
)
