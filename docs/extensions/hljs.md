title: highlight.js

Um hljs zu nutzen erstmal [herunterladen](https://highlightjs.org/download/), in `custom_dir` speichern und als `extra_javascript` in die `mkdocs.yml` Datei einfügen.

Unter den [Beispielstylesheets](https://github.com/highlightjs/highlight.js/tree/main/src/styles) passen die am besten von denen es eine "-light" und "-dark" Version gibt.

> An den CSS Dateine muss ggf. noch die `background-color` Eingenschaft entfernt werden, da dies sonst das Farbthema überschreibt.

```yaml
theme:
    name: risonia
    custom_dir: theme_override/

extra_javascript:
  - 'assets/javascripts/highlight.min.js'

plugins:
    #...
    - color-theme:
        theme_color: '#ef6110'
        secondary_color: 'complementary'
        extra_css_light:
          - 'extra_css/stackoverflow-light.min.css' #hljs CSS für helle Ansicht
        extra_css_dark:
          - 'extra_css/stackoverflow-dark.min.css' #hljs CSS für dunkle Ansicht
    #...
```

Außerdem kann man mit Anlegen der Datei `main.html` in `custom_dir` noch den `exec_script` Block überschreiben.

```html
{% extends "base.html" %}

{% block exec_script %}
<script id="theme">
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('pre code').forEach((el) => {
    hljs.highlightElement(el);
  });
});
</script>
{% endblock %}
```

Aber man kann den Javascriptcode auch im Markdown der Seiten einfügen die Codeeinfärbung benötigen.