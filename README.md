# mkdocs-risonia-theme

[![PyPI Version](https://img.shields.io/pypi/v/mkdocs-risonia-theme.svg)](https://pypi.org/project/mkdocs-risonia-theme/)
[![PyPI downloads](https://img.shields.io/pypi/dm/mkdocs-risonia-theme.svg)](https://pypi.org/project/mkdocs-risonia-theme)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

A simple theme for [MkDocs](https://www.mkdocs.org/). Based on [this demo](https://www.w3schools.com/w3css/tryw3css_examples_material.htm) 
using the [w3.css](https://www.w3schools.com/w3css/) framework and configurable color schemes
(inspiration [here](https://www.w3schools.com/colors/colors_schemes.asp)).

## Demo

See a demo and documentation [here](https://unverbuggt.xn--rthlein-n2a.de/risonia/en/)

![](https://github.com/unverbuggt/mkdocs-risonia-theme/raw/main/screen_big.png)
![](https://github.com/unverbuggt/mkdocs-risonia-theme/raw/main/screen_small.png)

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
* Integration of `mkdocs-static-i18n` plugin.
* Integration of `mkdocs-encryptcontent-plugin`.
* Web app support.
* Rather [lightweight](https://unverbuggt.xn--rthlein-n2a.de/risonia/en/mkdocs/#size-comparison)
* Short (nav) and long (top panel) [page titles](#page-titles)

## Installation

Install the package with pip:

```bash
pip install mkdocs-risonia-theme
```

Install the package from source with pip:

```bash
cd mkdocs-risonia-theme/
python setup.py sdist bdist_wheel
pip install dist/mkdocs_risonia_theme-0.1.9-py3-none-any.whl
```

## Configuration

Enable the theme and plugins in your `mkdocs.yml`:

```yaml
theme:
    name: risonia
    #custom_dir: theme_override/ # add static files or overrides
    #logo: img/logo.svg # if undefined a burger symbol is displayed on mobile devices
    #favicon: img/logo.ico # if undefined img/favicon.ico is used
    #manifest: manifest.json # manifest for installable webapp
    #serviceworker: service-worker.js # for webapp an empty file is sufficient
    #extlink: true # mark external links with symbol
    #extblank: true # send external links to new browser tab
    #toc_sidebar: true # If display is wide enough, then display TOC on the right side
    #zoom_img: true # click on images to view them bigger
    
plugins:
    - search: {}

    #- i18n: {...} # mkdocs-static-i18n

    - color-theme: # optional
        theme_color: '#ff6600' # primary color
        secondary_color: 'complementary' # can be a color or scheme
        #extra_css_light: # list of extra CSS for light mode
        #    - 'css/additional-light.css'
        #extra_css_dark:  # list of extra CSS for dark mode
        #    - 'css/additional-dark.css'

    - w3css-classes: {} # mandatory

    #- encryptcontent: {...} # mkdocs-encryptcontent-plugin
```

## Overrides

The file `main.html` in `custom_dir` can be used to further customize the template:

```html
{% extends "base.html" %}

{% block exec_script %}
<script>
  var DOMContentLoaded_fired = false;
</script>
<script id="theme">
function runWhenDOMContentLoaded() {
  document.querySelectorAll('pre code').forEach((el) => {
    hljs.highlightElement(el);
  });
  document.querySelectorAll('table').forEach(function(table) {
    if (!table.hasAttribute('Tablesort')) {
      new Tablesort(table);
      table.setAttribute('Tablesort', '');
    }
  });
}
if (DOMContentLoaded_fired) {
  runWhenDOMContentLoaded();
}
</script>
<script>
document.addEventListener('DOMContentLoaded',function(){
  DOMContentLoaded_fired=true;
  runWhenDOMContentLoaded();
});
</script>
{% endblock %}

{%- block footer_ext %}
  <p class="w3-right w3-tiny">
  {%- if i18n_config and i18n_page_file_locale %}
    <a href="{{ (i18n_page_locale + '/imprint/') | url }}">Imprint</a>
  {%- else %}
    <a href="{{ 'imprint/' | url }}">Impressum</a>
  {%- endif %}
  </p>
{%- endblock %}

{%- block top_buttons %}
    <a class="w3-button w3-theme-d1 w3-hover-theme w3-padding-small w3-right no-print" href="{{ config.repo_url }}" target="_blank">&lt;/&gt;</a> 
{%- endblock %}
```

## Page titles

Normally `nav` page titles would override `#` heading or `title` meta tag.
But in this theme the `title` meta tag will always be used for the top panel if defined.

For example define the navigation:

```yaml
nav:
    - Short title: 'index.md'
```

And within `index.md` you define the long title like this:

```markdown
title: Long long long title
```