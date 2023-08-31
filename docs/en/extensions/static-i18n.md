title: static i18n plugin

If the [`mkdocs-static-i18n`](https://ultrabug.github.io/mkdocs-static-i18n/) plugin is installed, activated in `mkdocs.yaml` and configured,
then the language can be switched through the <svg class="svg-1em"><use xlink:href="#i18n" /></svg> symbol at the top right of the page.

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

Additional information about language versions is supplied to the search engines via the head of the pages.

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