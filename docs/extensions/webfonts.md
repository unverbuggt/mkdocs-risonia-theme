title: Webfonts

## Webfonts selbst hosten { style="font-family:Lobster;" }

Um Webfonts einzubinden muss zuerst die gewünschte Schriftart heruntergeladen werden. Das geht z.B. über den [google-webfonts-helper](https://gwfh.mranftl.com/fonts).

Die Dateien müssen dann in den `custom_path` kopiert werden und die `fonts.css` unter `extra_css` eingebunden werden. 
Die Markdownerweiterung `attr_list` wird benötigt um das Webfont z.B. für einzelne Überschriften zu verwenden.

```yaml
theme:
    name: risonia
    custom_dir: theme_override/

extra_css:
  - 'css/fonts.css'

markdown_extensions:
    - attr_list
```

Die Pfadangaben in der `fonts.css` gelten relativ zur CSS Datei die in `theme_override/css/` liegt.

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

Die Webfonts (woff\* Dateien) selber liegen also in `theme_override/assets/fonts/`.

In der Markdown Datei kann das Webfont dann so zugewiesen werden:

```markdown
## Webfonts selbst hosten { style="font-family:Lobster;" }
```