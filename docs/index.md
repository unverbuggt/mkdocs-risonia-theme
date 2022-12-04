title: MkDocs Risonia Thema

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
    #custom_dir: files/ # statische Inhalte und Anpassungen
    #logo: img/logo.svg # ohne logo wird bei mobilen Geräten ein Burgermenü angezeigt
    #favicon: img/logo.ico # sonst wird img/favicon.ico angenommen
    #manifest: manifest.json # Manifest für Webapp
    #serviceworker: service-worker.js # Benötigt für Webapp, kann eine leere Datei sein
    #extlink: true # externe Links markieren
    
plugins:
    - search: {}
    #- i18n: {...} #mkdocs-static-i18n
    - color-theme: #optional
        theme_color: '#ff6600' #Hauptfarbe
        secondary_color: 'complementary' #Zweitfarbe oder Farbschema
        #extra_light_path: 'css/additional-light.css'
        #extra_dark_path: 'css/additional-dark.min.css'
    - w3css-classes: {} #nötig
    #- encryptcontent: {...} #mkdocs-encryptcontent-plugin
```

<script>

document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('pre code').forEach((el) => {
    hljs.highlightElement(el);
  });
});

</script>