from setuptools import setup, find_packages

VERSION = '0.1'


setup(
    name="mkdocs-risonia-theme",
    version=VERSION,
    url='https://github.com/unverbuggt/mkdocs-risonia-theme',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs',
        'beautifulsoup4',
    ],
    description='risonia theme for MkDocs',
    author='René Rüthlein',
    author_email='unverbuggt@xn--rthlein-n2a.de',
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
