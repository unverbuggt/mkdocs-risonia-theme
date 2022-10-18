import os

from colorsys import rgb_to_hls
from colorsys import hls_to_rgb
import math

from jinja2 import Template

from pathlib import Path

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

#PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
#CSS_TPL_PATH = os.path.join(PLUGIN_DIR, 'w3-theme.jinja2.py')

TPL_THEME = \
""".w3-theme-l5 {color:{{ color_l5 }} !important; background-color:{{ bgcolor_l5 }} !important}
.w3-theme-l4 {color:{{ color_l4 }} !important; background-color:{{ bgcolor_l4 }} !important}
.w3-theme-l3 {color:{{ color_l3 }} !important; background-color:{{ bgcolor_l3 }} !important}
.w3-theme-l2 {color:{{ color_l2 }} !important; background-color:{{ bgcolor_l2 }} !important}
.w3-theme-l1 {color:{{ color_l1 }} !important; background-color:{{ bgcolor_l1 }} !important}
.w3-theme-d1 {color:{{ color_d1 }} !important; background-color:{{ bgcolor_d1 }} !important}
.w3-theme-d2 {color:{{ color_d2 }} !important; background-color:{{ bgcolor_d2 }} !important}
.w3-theme-d3 {color:{{ color_d3 }} !important; background-color:{{ bgcolor_d3 }} !important}
.w3-theme-d4 {color:{{ color_d4 }} !important; background-color:{{ bgcolor_d4 }} !important}
.w3-theme-d5 {color:{{ color_d5 }} !important; background-color:{{ bgcolor_d5 }} !important}

.w3-theme-light {color:{{ color_l5 }} !important; background-color:{{ bgcolor_l5 }} !important}
.w3-theme-dark {color:{{ color_d5 }} !important; background-color:{{ bgcolor_d5 }} !important}
.w3-theme-action {color:{{ color_d5 }} !important; background-color:{{ bgcolor_d5 }} !important}

.w3-theme {color:{{ color_theme }} !important; background-color:{{ bgcolor_theme }} !important}
.w3-text-theme {color:{{ bgcolor_theme }} !important}
.w3-border-theme {border-color:{{ bgcolor_theme }} !important}

.w3-hover-theme:hover {color:{{ color_theme }} !important; background-color:{{ bgcolor_theme }} !important}
.w3-hover-text-theme:hover {color:{{ bgcolor_theme }} !important}
.w3-hover-border-theme:hover {border-color:{{ bgcolor_theme }} !important}

.w3-code {
  border-left:4px solid {{ bgcolor_theme }};
}
.w3-code, .w3-codespan {
  color:{{ color_l3 }};
  background-color:{{ bgcolor_l3 }};
}

a{color: inherit !important;}

.w3-striped tbody tr:nth-child(even){
    background-color:{{ bgcolor_l4 }}
}

.w3-bordered tr{
    border-bottom:1px solid {{ color_l5 }}
}

.w3-table tbody tr:hover,table li:hover{
  background-color:{{ bgcolor_l3 }}
}

.search-results article:hover {
  background-color:{{ bgcolor_l3 }}
}"""

TPL = \
"""/* inspired by https://www.w3schools.com/w3css/w3css_color_generator.asp */

/* light theme */
{{ tpl_light }}

@media (prefers-color-scheme: dark) {
  /* dark theme */
{{ tpl_dark | indent(2, True) }}
}"""


def hex_to_rgb(value):
    h = value.lstrip('#')
    if len(h) == 6:
        return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4))
    else:
        return tuple(int(h[i], 16)/15.0 for i in (0, 1, 2))

def rgb_to_hex(value):
    return '#%02x%02x%02x' % (int(value[0]*255.0), int(value[1]*255.0), int(value[2]*255.0))

def perceived_brightness(value):
    #https://alienryderflex.com/hsp.html
    rgb = hex_to_rgb(value)
    return math.sqrt( (0.299 * rgb[0]*rgb[0]) + (0.587 * rgb[1] * rgb[1]) + (0.114 * rgb[2] * rgb[2]) )

class W3cssColorTheme(BasePlugin):

    themes_to_build = set()

    config_scheme = (
        ('theme_color', config_options.Type(str, default='#efc050')),
        ('light_text_color', config_options.Type(str, default='#000')),
        ('dark_text_color', config_options.Type(str, default='#fff')),
    )

    def text_contrast(self, value, pref_dark):
        pbg = perceived_brightness(value)
        pl = perceived_brightness(self.config['light_text_color'])
        pd = perceived_brightness(self.config['dark_text_color'])
        diff_to_l = abs(pbg-pl)
        diff_to_d = abs(pbg-pd)
        diff_ld = abs(diff_to_l-diff_to_d)
        if diff_ld < 0.2: #if the contrast difference isnt't too big, allow to choose text color based on preference
            if pref_dark:
                return self.config['dark_text_color']
            else:
                return self.config['light_text_color']
        if diff_to_d > diff_to_l:
            return self.config['dark_text_color']
        else:
            return self.config['light_text_color']

    def generate_theme(self, config, theme_color, name, scheme='monochromatic'):
        themergb = hex_to_rgb(theme_color)
        themehls = rgb_to_hls(themergb[0],themergb[1],themergb[2])
        hue_theme = themehls[0]
        hues = [hue_theme] * 10
        light = themehls[1]
        sat = themehls[2]
        
        if scheme == 'analogous':
            huep = hue_theme + (1/12)
            huem = hue_theme - (1/12)
            hues[0],hues[3],hues[4],hues[7],hues[8] = [huep] * 5
            hues[1],hues[2],hues[5],hues[6],hues[9] = [huem] * 5
        elif scheme == 'complementary':
            hues[0],hues[1],hues[2],hues[3],hues[4] = [hue_theme + 0.5] * 5
            hues[5],hues[6],hues[7],hues[8],hues[9] = [hue_theme] * 5
        elif scheme == 'triadic':
            huep = hue_theme + (4/12)
            huem = hue_theme - (4/12)
            hues[0],hues[3],hues[4],hues[7],hues[8] = [huep] * 5
            hues[1],hues[2],hues[5],hues[6],hues[9] = [huem] * 5
        elif scheme == 'compound':
            huep = hue_theme + (5/12)
            huem = hue_theme - (5/12)
            hues[0],hues[3],hues[4],hues[7],hues[8] = [huep] * 5
            hues[1],hues[2],hues[5],hues[6],hues[9] = [huem] * 5
        
        #check of scheme made hue12 leave range
        for i in range(len(hues)):
            if hues[i] < 0:
                hues[i] = hues[i] + 1
            elif hues[i] > 1:
                hues[i] = hues[i] - 1
        
        data = {}
        data['bgcolor_l5'] = rgb_to_hex(hls_to_rgb(hues[0], light + ((1.0-light) / 5.0 * 4.5), sat))
        data['bgcolor_l4'] = rgb_to_hex(hls_to_rgb(hues[1], light + ((1.0-light) / 5.0 * 3.6), sat))
        data['bgcolor_l3'] = rgb_to_hex(hls_to_rgb(hues[2], light + ((1.0-light) / 5.0 * 2.7), sat))
        data['bgcolor_l2'] = rgb_to_hex(hls_to_rgb(hues[3], light + ((1.0-light) / 5.0 * 1.8), sat))
        data['bgcolor_l1'] = rgb_to_hex(hls_to_rgb(hues[4], light + ((1.0-light) / 5.0 * 0.9), sat))
        data['bgcolor_theme'] = rgb_to_hex(hls_to_rgb(hue_theme, light, sat))
        data['bgcolor_d1'] = rgb_to_hex(hls_to_rgb(hues[5], light - (light / 5.0 * 0.5), sat))
        data['bgcolor_d2'] = rgb_to_hex(hls_to_rgb(hues[6], light - (light / 5.0 * 1), sat))
        data['bgcolor_d3'] = rgb_to_hex(hls_to_rgb(hues[7], light - (light / 5.0 * 1.5), sat))
        data['bgcolor_d4'] = rgb_to_hex(hls_to_rgb(hues[8], light - (light / 5.0 * 2), sat))
        data['bgcolor_d5'] = rgb_to_hex(hls_to_rgb(hues[9], light - (light / 5.0 * 2.5), sat))
        
        data['color_l5'] = self.text_contrast(data['bgcolor_l5'],0)
        data['color_l4'] = self.text_contrast(data['bgcolor_l4'],0)
        data['color_l3'] = self.text_contrast(data['bgcolor_l3'],0)
        data['color_l2'] = self.text_contrast(data['bgcolor_l2'],0)
        data['color_l1'] = self.text_contrast(data['bgcolor_l1'],0)
        data['color_theme'] = self.text_contrast(data['bgcolor_theme'],0)
        data['color_d1'] = self.text_contrast(data['bgcolor_d1'],0)
        data['color_d2'] = self.text_contrast(data['bgcolor_d2'],0)
        data['color_d3'] = self.text_contrast(data['bgcolor_d3'],0)
        data['color_d4'] = self.text_contrast(data['bgcolor_d4'],0)
        data['color_d5'] = self.text_contrast(data['bgcolor_d5'],0)
        
        tpl = Template(TPL_THEME)
        out_theme_light = tpl.render(data)

        data = {}
        data['bgcolor_d5'] = rgb_to_hex(hls_to_rgb(hues[9], light + ((1.0-light) / 5.0 * 2.5), sat))
        data['bgcolor_d4'] = rgb_to_hex(hls_to_rgb(hues[8], light + ((1.0-light) / 5.0 * 2), sat))
        data['bgcolor_d3'] = rgb_to_hex(hls_to_rgb(hues[7], light + ((1.0-light) / 5.0 * 1.5), sat))
        data['bgcolor_d2'] = rgb_to_hex(hls_to_rgb(hues[6], light + ((1.0-light) / 5.0 * 1), sat))
        data['bgcolor_d1'] = rgb_to_hex(hls_to_rgb(hues[5], light + ((1.0-light) / 5.0 * 0.5), sat))
        data['bgcolor_theme'] = rgb_to_hex(hls_to_rgb(hue_theme, light, sat))
        data['bgcolor_l1'] = rgb_to_hex(hls_to_rgb(hues[4], light - (light / 5.0 * 0.9), sat))
        data['bgcolor_l2'] = rgb_to_hex(hls_to_rgb(hues[3], light - (light / 5.0 * 1.8), sat))
        data['bgcolor_l3'] = rgb_to_hex(hls_to_rgb(hues[2], light - (light / 5.0 * 2.7), sat))
        data['bgcolor_l4'] = rgb_to_hex(hls_to_rgb(hues[1], light - (light / 5.0 * 3.6), sat))
        data['bgcolor_l5'] = rgb_to_hex(hls_to_rgb(hues[0], light - (light / 5.0 * 4.5), sat))
        
        data['color_l5'] = self.text_contrast(data['bgcolor_l5'],1)
        data['color_l4'] = self.text_contrast(data['bgcolor_l4'],1)
        data['color_l3'] = self.text_contrast(data['bgcolor_l3'],1)
        data['color_l2'] = self.text_contrast(data['bgcolor_l2'],1)
        data['color_l1'] = self.text_contrast(data['bgcolor_l1'],1)
        data['color_theme'] = self.text_contrast(data['bgcolor_theme'],1)
        data['color_d1'] = self.text_contrast(data['bgcolor_d1'],1)
        data['color_d2'] = self.text_contrast(data['bgcolor_d2'],1)
        data['color_d3'] = self.text_contrast(data['bgcolor_d3'],1)
        data['color_d4'] = self.text_contrast(data['bgcolor_d4'],1)
        data['color_d5'] = self.text_contrast(data['bgcolor_d5'],1)

        tpl = Template(TPL_THEME)
        out_theme_dark = tpl.render(data)
        
        data = {}
        data['tpl_light'] = out_theme_light
        data['tpl_dark'] = out_theme_dark
        tpl = Template(TPL)
        out_theme = tpl.render(data)

        Path(config.data["site_dir"] + '/css/').mkdir(parents=True, exist_ok=True)
        w3_theme_css_path = Path(config.data["site_dir"] + '/css/w3-theme' + name + '.css')
        with open(w3_theme_css_path, "w") as file:
            file.write(out_theme)
        w3_theme_light_css_path = Path(config.data["site_dir"] + '/css/w3-theme' + name + '-light.css')
        with open(w3_theme_light_css_path, "w") as file:
            file.write(out_theme_light)
        w3_theme_dark_css_path = Path(config.data["site_dir"] + '/css/w3-theme' + name + '-dark.css')
        with open(w3_theme_dark_css_path, "w") as file:
            file.write(out_theme_dark)

    def on_post_build(self, config, **kwargs):
        theme = self.config['theme_color']
        self.generate_theme(config, theme, '')
        for color in self.themes_to_build:
            self.generate_theme(config, color, '-'+color.lstrip('#'))

    def on_page_context(self, context, page, config, nav):
        if 'theme_color' in page.meta.keys():
            theme_color = str(page.meta.get('theme_color'))
            if theme_color is not None:
                context['theme_color'] = theme_color.lstrip('#')
                self.themes_to_build.add(theme_color)
        return context
