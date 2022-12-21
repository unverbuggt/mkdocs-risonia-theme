title: tablesort

## Beispiel

| Spieler | Deaths | Frags | Latenz |
| ------ | ------ | ----- | ------- |
| Coni   | 106    | 73    | 46      |
| Kapu   | 98     | 100   | 33      |
| Le Franzose | 91    | 66    | 50      |
| TheoneEP | 89    | 87    | 34      |
| arsh0r | 86     | 88    | 0       |
| gr3t   | 72     | 85    | 49      |
| BMW Doktor | 40    | 83    | 47      |

<p></p>

## Einrichtung

Um tablesort zu nutzen erst mal [herunterladen](https://github.com/tristen/tablesort/releases/), in `custom_dir` speichern und als `extra_javascript` in die `mkdocs.yml` Datei einfügen.

Aus dem Beispiel [CSS](https://tristen.ca/tablesort/tablesort.css) kann man durch ändern des `border-color` leicht eine Version für das dunkle Thema machen.

```yaml
theme:
    name: risonia
    custom_dir: theme_override/

extra_javascript:
  - 'assets/javascripts/tablesort.js'
  - 'assets/javascripts/tablesort.number.js'

plugins:
    #...
    - color-theme:
        theme_color: '#ef6110'
        secondary_color: 'complementary'
        extra_css_light:
          - 'extra_css/tablesort-light.css' #tablesort CSS für helle Ansicht
        extra_css_dark:
          - 'extra_css/tablesort-dark.css' #tablesort CSS für dunkle Ansicht
    #...
```

Außerdem kann man mit Anlegen der Datei `main.html` in `custom_dir` noch den `exec_script` Block überschreiben.

```html
{% extends "base.html" %}

{% block exec_script %}
<script id="theme">
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('table').forEach(function(table) {
    if (!table.hasAttribute('Tablesort')) {
      new Tablesort(table);
      table.setAttribute('Tablesort', '');
    }
  });
});
</script>
{% endblock %}
```

Aber man kann den Javascriptcode auch im Markdown der Seiten einfügen die Tabellen enthalten.