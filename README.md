# mkdocs-risonia-theme

A simple theme for [MkDocs](https://www.mkdocs.org/). Based on [this demo](https://www.w3schools.com/w3css/tryw3css_examples_material.htm) 
using the [w3.css](https://www.w3schools.com/w3css/) framework and configurable color schemes
(inspiration [here](https://www.w3schools.com/colors/colors_schemes.asp)).

## Design goals

* Be a simple starting point for modifications.
* Be colorful and readable.
* Implement all features of the standard MkDocs theme (in progress).
* Integrate some useful plugins.
* Don't require translations.
* Don't be obfuscated.
* Add as little nonsense as possible.

## Ugly compromises

* To use w3css we need to add additional classes to the markdown output.
    * The good part is, while we're at it, we are also able to mark externals links.
* The SVG icons need to be included in every page, because otherwise they can't be set to the text color.

## Features

* Light and dark mode.
* Integration of `mkdocs-static-i18n` pLugin.
* Integration of `mkdocs-encryptcontent-plugin`.
* Web app support.

## Installation

Install the package with pip:

```bash
pip install mkdocs-risonia-theme
```

Install the package from source with pip:

```bash
cd mkdocs-risonia-theme/
python setup.py sdist bdist_wheel
pip install dist/mkdocs_risonia_theme-0.1-py3-none-any.whl
```

## Configuration

Enable the theme and plugins in your `mkdocs.yml`:

```yaml
theme:
    name: risonia
    #custom_dir: files/ #add static files or overrides
    #logo: img/logo.svg #if undefined a burger symbol is displayed on mobile devices
    #favicon: img/logo.ico #if undefined img/favicon.ico is used
    #manifest: manifest.json #manifest for installable webapp
    #serviceworker: service-worker.js #for webapp an empty file is sufficient
    #extlink: true #mark external links with symbol
    
plugins:
    - search: {}

    #- i18n: {...} #mkdocs-static-i18n

    - color-theme: #optional
        theme_color: '#ff6600' #primary color
        secondary_color: 'complementary' #can be a color or scheme
        #extra_css_light: #list of extra CSS for light mode
        #    - 'css/additional-light.css'
        #extra_css_dark:  #list of extra CSS for dark mode
        #    - 'css/additional-dark.css'

    - w3css-classes: {} #mandatory

    #- encryptcontent: {...} #mkdocs-encryptcontent-plugin
```