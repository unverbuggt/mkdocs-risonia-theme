title: highlight.js

To use hljs [download](https://highlightjs.org/download/), place it in `custom_dir` and add to `extra_javascript` in the `mkdocs.yml` file.

Check the available [styles](https://github.com/highlightjs/highlight.js/tree/main/src/styles) for ones that end with "-light" and "-dark".

> You might need to manually edit the CSS to remove `background-color` properties, because this would override the theme settings.

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
          - 'extra_css/stackoverflow-light.min.css' #place hljs light theme here
        extra_css_dark:
          - 'extra_css/stackoverflow-dark.min.css' #place hljs dark theme here
    #...
```

You could add the file `main.html` to `custom_dir` to override the `exec_script` block:

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

But you can also add said javascript code to the markdown pages that should make use of code highlighting.