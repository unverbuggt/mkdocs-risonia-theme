title: color-theme Plugin

Das `color-theme` Plugin generiert das farbliche Aussehen anhand von verschiedenen Optionen. Die Verwendung des Plugins ist optional.

Mit `theme_color` wird die [Hauptfarbe](primary/) des Themas festgelegt. Diese Farbe bleibt in der hellen und dunklen Ansicht (<svg class="svg-1em"><use xlink:href="#theme-toggle" /></svg>) gleich.

Durch `secondary_color` wird entweder eine [Zweitfarbe](secondary/) oder ein [Schema](secondary/mono/) für die Zweitfarben definiert.

Die Textfarben unter `light_text_color` und `dark_text_color` müssen nicht unbedingt Schwarz und Weiss lauten.
Sie werden allerdings nicht explizit für helle bzw. dunkle Ansicht verwendet sondern je nach bestem Kontrast ausgewählt.

Durch die Option `extra_light_path` und `extra_dark_path` können zusätzliche CSS in das Aussehen der jeweiligen Ansicht eingebunden werden.

```yaml
plugins:
    #...
    - color-theme:
        theme_color: '#ef6110' #Hauptfarbe
        secondary_color: 'complementary' #Zweitfarbe oder Farbschema
        light_text_color: '#000' #Schwarz
        dark_text_color: '#fff' #Weiss
        #extra_css_light: #Liste mit zuätzlichen CSS Dateien für die helle Ansicht
        #    - 'css/additional-light.css'
        #extra_css_dark:  #Liste mit zuätzlichen CSS Dateien für die dunkle Ansicht
        #    - 'css/additional-dark.css'
    #...
```

Die beiden Einstellungen `theme_color` und `secondary_color` können auch als Metainformation Im Kopf jeder Markdowndatei individuell festgelegt werden.

> **Achtung:** hierbei keine Anführungszeichen verwenden.

```markdown
theme_color: #ef6110
secondary_color: mono
```
