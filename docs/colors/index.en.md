title: color-theme plugin

The `color-theme` plugin generates the colors of the theme depending on various settings. The usage is optional.

`theme_color` sets the [primary color](primary.md) of the theme. This color is consistent through light and dark mode (<svg class="svg-1em"><use xlink:href="#theme-toggle" /></svg>).

With `secondary_color` you can either define a [secondary color](secondary/index.md) or a [color scheme](secondary/mono.md).

The text colors `light_text_color` and `dark_text_color` don't need to be black and white.
But they aren't explicitly assigned to dark or light mode. They are chosen depending on best contrast.

Use options `extra_css_light` and `extra_css_dark` to integrate additional CSS to the modes.

```yaml
plugins:
    #...
    - color-theme:
        theme_color: '#ef6110' #primary color
        secondary_color: 'complementary' #can be a color or scheme
        light_text_color: '#000' #black
        dark_text_color: '#fff' #white
        #extra_css_light: #list of extra CSS for light mode
        #    - 'css/additional-light.css'
        #extra_css_dark:  #list of extra CSS for dark mode
        #    - 'css/additional-dark.css'
    #...
```

The settings `theme_color` and `secondary_color` can also be set as meta tag in the header of each markdown document.

> **Attention:** don't use quotes here.

```markdown
theme_color: #ef6110
secondary_color: mono
```
