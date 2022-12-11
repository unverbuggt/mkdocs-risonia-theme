title: Static i18n plugin

Ist das [`mkdocs-static-i18n`](https://ultrabug.github.io/mkdocs-static-i18n/) Plugin installiert, in der `mkdocs.yaml` Datei aktiviert und konfiguriert,
dann kann über das <svg class="svg-1em"><use xlink:href="#i18n" /></svg> Symbol rechts oben die Sprache umgeschaltet werden.

```yaml
plugins:
    #...
    - i18n:
        default_language: de
        default_language_only: false
        docs_structure: suffix
        languages:
          default:
            name: Deutsch
            build: true
          en:
            name: English
            build: true
            site_name: "MkDocs Risonia theme"
        nav_translations:
          en:
            Farben: Colors
            Zweitfarben: Secondary colors
            Erweiterungen: Extensions
            Javascript: Javascript
    #...
```

Suchmaschinen erhalten über zusätzliche Informationen in den generierten Seiten Hinweise auf die anderen Sprachversionen.

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <!-- ... -->
  <link rel="alternate" hreflang="fr" href="https://example.com/fr/">
  <link rel="alternate" hreflang="en" href="https://example.com/en/">
  <!-- ... -->
</head>
```