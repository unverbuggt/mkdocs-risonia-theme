title: Webfonts

## Self-host web fonts { style="font-family:Lobster;" }

In order to use web fonts you'll need to download the desired font first. This can be done by using the [google-webfonts-helper](https://gwfh.mranftl.com/fonts).

The files need to be copied to `custom_path` and the corresponding `fonts.css` needs to be added to `extra_css`.
Also the markdown extension `attr_list` can be used to set the font for individual headings for example.

```yaml
theme:
    name: risonia
    custom_dir: theme_override/

extra_css:
  - 'css/fonts.css'

markdown_extensions:
    - attr_list
```

The paths to the fonts in `fonts.css` need to be relative to the CSS file in  `theme_override/css/`.

```css
/* lobster-regular - latin */
@font-face {
  font-family: 'Lobster';
  font-style: normal;
  font-weight: 400;
  src: local(''),
       url('../assets/fonts/lobster-v28-latin-regular.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
       url('../assets/fonts/lobster-v28-latin-regular.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
}
.font-lobster {
    font-family: 'Lobster';
}
```

So the web fonts (woff\* files) reside in `theme_override/assets/fonts/` in this example.

The web font can added to the heading like this:

```markdown
## Self-host web fonts { style="font-family:Lobster;" }
```