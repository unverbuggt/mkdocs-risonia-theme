title: MkDocs

## Einleitung

Übersetzt von der [MkDocs](https://www.mkdocs.org/) Seite:

> MkDocs ist ein **schneller**, **einfacher** und **absolut prächtiger** Generator für statische Webseiten
> gedacht zur Erstellung von Projektdokumentationen. Die Dokumentation wird in Markdown Dateien verfasst,
> und alles wird mit einer einzelnen YAML Datei konfiguriert. Am besten fängst du mit dem
> [Einsteigertutorial](https://www.mkdocs.org/getting-started/) an, danach findest du weitere Informationen
> im [Benutzerhandbuch](https://www.mkdocs.org/user-guide/).

## Themen

MkDocs bringt zwei Themen gleich mit (`mkdocs` und `readthedocs`). 
Aber es gibt einige [Themen von Drittanbietern](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes) die man stattdessen verwenden kann.

### Größenvergleich

Ich habe einmal (Stand 14.12.2022) diese Seite mit verschiedenen Themen generiert
um ein Gefühl für die Größe der generierten Seiten zu bekommen. 
Alle Größenangaben in Kilobyte (aufgerundet).

Thema | Version | HTML | CSS | JS/JSON/MAP | Webfonts | Sonstiges | Gesamt
---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
`risonia` | 0.1 | 712 | 213 | 439 | 76 | 807 | 2247
`mkdocs` | 1.4.2 | 593 | 203 | 597 | 1030 | 803 | 3226
`material` | 8.5.10 | 1045 | 151 | 2183 | 76 | 801 | 4256
`material` | 8.4.4-insiders | 1110 | 534 | 2946 | 703 | 801 | 6094

HTML, CSS, JS müsste einigermaßen vergleichbar sein, wobei Risonia kein "minify" verwendet.
Allerdings verwendet das `material` Thema [Pygments](https://pygments.org/)
statt [highlight.js](https://highlightjs.org/) um Code einzufärben , was den HTML Teil vergrößert.

Bei Webfonts kann man schlecht vergleichen, da `mkdocs` z.B. aus Abwärtskompatibilität sämtliche
Versionen der Schriftarten mitliefert.
Risonia verwendet in der Grundkonfiguration erstmal keine Webfonts.

Die "insiders" Version von `material` war mit dem `privacy` Plugin konfiguriert,
es wurde also alle externen Abhängigkeiten nachgeladen.
