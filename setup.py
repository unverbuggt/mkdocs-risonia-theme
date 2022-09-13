from setuptools import setup, find_packages

VERSION = '0.1'


setup(
    name="mkdocs-w3css-theme",
    version=VERSION,
    url='https://github.com/unverbuggt/mkdocs-w3css-theme',
    license='MIT',
    description='w3css theme for MkDocs',
    author='René Rüthlein',
    author_email='unverbuggt@xn--rthlein-n2a.de',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'w3csstheme = w3css_theme',
        ],
        'mkdocs.plugins': [
            'color-theme = w3css_theme.plugins.color.plugin:W3cssColorTheme'
        ]
    },
    zip_safe=False
)
