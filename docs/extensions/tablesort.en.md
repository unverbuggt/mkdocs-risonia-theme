title: tablesort

## Example

| Player | Deaths | Frags | Latency |
| ------ | ------ | ----- | ------- |
| Coni   | 106    | 73    | 46      |
| Kapu   | 98     | 100   | 33      |
| Le Franzose | 91    | 66    | 50      |
| TheoneEP | 89    | 87    | 34      |
| arsh0r | 86     | 88    | 0       |
| gr3t   | 72     | 85    | 49      |
| BMW Doktor | 40    | 83    | 47      |

<p></p>

## Installation

To use tablesort download a [release](https://github.com/tristen/tablesort/releases/), place it in `custom_dir` and add to `extra_javascript` in the `mkdocs.yml` file.

You can derive a dark theme version of the example [CSS](https://tristen.ca/tablesort/tablesort.css) by adjusting the `border-color` property.

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
          - 'extra_css/tablesort-light.css' #place tablesort light theme here
        extra_css_dark:
          - 'extra_css/tablesort-dark.css' #place tablesort dark theme here
    #...
```

You could add the file `main.html` to `custom_dir` to override the `exec_script` block:

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

But you can also add said javascript code to the markdown pages that should make use of tables.