title: color-theme plugin

The `color-theme` plugin generates the colors of the theme depending on various settings. The usage is optional.

`theme_color` sets the [primary color](primary/) ot the theme. This color is consistent through light and dark mode (<svg class="svg-1em"><use xlink:href="#theme-toggle" /></svg>).

With `secondary_color` you can either define a [secondary color](secondary/) or a [color scheme](secondary/mono/).

The text colors `light_text_color` and `dark_text_color` don't need to be black and white.
But they aren't explicitely assigned to dark or light mode. They are chosen depending on best contrast.

Use options `extra_light_path` and `extra_dark_path` to integradte additional CSS to the modes.

```yaml
plugins:
    #...
    - color-theme:
        theme_color: '#ef6110' #primary color
        secondary_color: 'complementary' #can be a color or scheme
        light_text_color: '#000' #black
        dark_text_color: '#fff' #white
        #extra_light_path: 'css/additional-light.css' #path to addition CSS for light mode
        #extra_dark_path: 'css/additional-dark.min.css' #path to addition CSS for dark mode
    #...
```

The settings `theme_color` and `secondary_color` can also be set as meta tag in the header of each markdown document.

> **Attention:** don't use quotes here.

```markdown
theme_color: #ef6110
secondary_color: mono
```
