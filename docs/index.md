title: Risonia Thema

Ein einfaches Thema für [MkDocs](https://www.mkdocs.org/), basierend auf [diesem Demo](https://www.w3schools.com/w3css/tryw3css_examples_material.htm) 
, dem [w3.css](https://www.w3schools.com/w3css/) Framework und einstellbaren Farbschemen
(Inspiration von [dort](https://www.w3schools.com/colors/colors_schemes.asp)).

## Designziele

* Es soll einfach zu verstehen und modifizierbar sein.
* Es soll farbenfroh und trotzdem lesbar bleiben.
* Es soll alle Eigenschaften des normalen MkDocs Themas haben (dauert noch).
* Es soll einige nützlichen Plugins integrieren können.
* Es soll nicht übersetzt werden müssen.
* Es soll nicht verschleiern wie es funktioniert.
* Es soll so wenig Quatsch wie möglich enthalten.

## Blöde Kompromisse

* Wegen w3css müssen leider zusätzliche Klassen an die Markdownausgabe angefügt werden.
    * Aber wenn wir schonmal dabei sind, können wir gleich externe Links erkennen und markieren.
* Die SVG Symbole müssen in jede Seite eingefügt werden, weil sie sonst nicht in Textfarbe erscheinen können.

## Merkmale

* Helle und dunkle Ansicht.
* Integration vom `mkdocs-static-i18n` Plugin.
* Integration vom `mkdocs-encryptcontent-plugin`.
* Seite kann als Webapp installiert werden.

## Installation

Über Python pip installieren:

```bash
pip install mkdocs-risonia-theme
```

Oder aus den Quellen bauen mit pip:

```bash
cd mkdocs-risonia-theme/
python setup.py sdist bdist_wheel
pip install dist/mkdocs_risonia_theme-0.1-py3-none-any.whl
```

## Konfiguration

In der `mkdocs.yml` mit Thema und Plugins konfigurieren:

```yaml
theme:
    name: risonia
    #custom_dir: theme_override/ # statische Inhalte und Anpassungen
    #logo: img/logo.svg # ohne logo wird bei mobilen Geräten ein Burgermenü angezeigt
    #favicon: img/logo.ico # sonst wird img/favicon.ico angenommen
    #manifest: manifest.json # Manifest für Webapp
    #serviceworker: service-worker.js # Benötigt für Webapp, kann eine leere Datei sein
    #extlink: true # externe Links markieren
    #extblank: true # externe Links im neuen Browserfenster öffnen
    
plugins:
    - search: {}

    #- i18n: {...} # mkdocs-static-i18n

    - color-theme: #optional
        theme_color: '#ff6600' # Hauptfarbe
        secondary_color: 'complementary' # Zweitfarbe oder Farbschema
        #extra_css_light: # Liste mit zuätzlichen CSS Dateien für die helle Ansicht
        #    - 'css/additional-light.css'
        #extra_css_dark:  # Liste mit zuätzlichen CSS Dateien für die dunkle Ansicht
        #    - 'css/additional-dark.css'

    - w3css-classes: {} # nötig

    #- encryptcontent: {...} # mkdocs-encryptcontent-plugin
```

## Anpassungen

Über die Datei `main.html` im `custom_dir` können verschiedene Blöcke aus der Vorlage überschieben oder erweitert werden:

```html
{% extends "base.html" %}

{% block exec_script %}
<script id="theme">
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('pre code').forEach((el) => {
    hljs.highlightElement(el);
  });
  document.querySelectorAll('table').forEach(function(table) {
    if (!table.hasAttribute('Tablesort')) {
      new Tablesort(table);
      table.setAttribute('Tablesort', '');
    }
  });
});
</script>
{% endblock %}

{%- block footer_ext %}
  <p class="w3-tiny" style="float:right;">
  {%- if i18n_config and i18n_page_file_locale %}
    <a href="{{ (i18n_page_locale + '/imprint/') | url }}">Imprint</a>
  {%- else %}
    <a href="{{ 'imprint/' | url }}">Impressum</a>
  {%- endif %}
  </p>
{%- endblock %}

{%- block top_buttons %}
    <a class="w3-button w3-theme-d1 w3-hover-theme w3-padding-small w3-right no-print" href="https://github.com/unverbuggt/mkdocs-risonia-theme" target="_blank">&lt;/&gt;</a> 
{%- endblock %}
```