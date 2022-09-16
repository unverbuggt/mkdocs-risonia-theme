import os

from colorsys import rgb_to_hls
from colorsys import hls_to_rgb
import math

from jinja2 import Template

from pathlib import Path

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
CSS_TPL_PATH = os.path.join(PLUGIN_DIR, 'w3-theme.jinja2.py')

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

    config_scheme = (
        ('theme_color', config_options.Type(str, default='#efc050')),
        ('light_text_color', config_options.Type(str, default='#000')),
        ('dark_text_color', config_options.Type(str, default='#fff')),
    )

    def textContrast(self, value, prefDark):
        pbg = perceived_brightness(value)
        pl = perceived_brightness(self.config['light_text_color'])
        pd = perceived_brightness(self.config['dark_text_color'])
        diff_to_l = abs(pbg-pl)
        diff_to_d = abs(pbg-pd)
        diff_ld = abs(diff_to_l-diff_to_d)
        if diff_ld < 0.2:
            if prefDark:
                return self.config['dark_text_color']
            else:
                return self.config['light_text_color']
        elif diff_to_d > diff_to_l:
            return self.config['dark_text_color']
        else:
            return self.config['light_text_color']

    def on_post_build(self, config, **kwargs):
        theme = self.config['theme_color']
        themergb = hex_to_rgb(theme)
        themehls = rgb_to_hls(themergb[0],themergb[1],themergb[2])
        hue = themehls[0]
        light = themehls[1]
        sat = themehls[2]
        
        data = {}
        data['bgcolor_l5'] = rgb_to_hex(hls_to_rgb(hue, light + ((1.0-light) / 5.0 * 4.5), sat))
        data['bgcolor_l4'] = rgb_to_hex(hls_to_rgb(hue, light + ((1.0-light) / 5.0 * 3.6), sat))
        data['bgcolor_l3'] = rgb_to_hex(hls_to_rgb(hue, light + ((1.0-light) / 5.0 * 2.7), sat))
        data['bgcolor_l2'] = rgb_to_hex(hls_to_rgb(hue, light + ((1.0-light) / 5.0 * 1.8), sat))
        data['bgcolor_l1'] = rgb_to_hex(hls_to_rgb(hue, light + ((1.0-light) / 5.0 * 0.9), sat))
        data['bgcolor_theme'] = rgb_to_hex(hls_to_rgb(hue, light, sat))
        data['bgcolor_d1'] = rgb_to_hex(hls_to_rgb(hue, light - (light / 5.0 * 0.9), sat))
        data['bgcolor_d2'] = rgb_to_hex(hls_to_rgb(hue, light - (light / 5.0 * 1.8), sat))
        data['bgcolor_d3'] = rgb_to_hex(hls_to_rgb(hue, light - (light / 5.0 * 2.7), sat))
        data['bgcolor_d4'] = rgb_to_hex(hls_to_rgb(hue, light - (light / 5.0 * 3.6), sat))
        data['bgcolor_d5'] = rgb_to_hex(hls_to_rgb(hue, light - (light / 5.0 * 4.5), sat))
        
        data['color_l5'] = self.textContrast(data['bgcolor_l5'],0)
        data['color_l4'] = self.textContrast(data['bgcolor_l4'],0)
        data['color_l3'] = self.textContrast(data['bgcolor_l3'],0)
        data['color_l2'] = self.textContrast(data['bgcolor_l2'],0)
        data['color_l1'] = self.textContrast(data['bgcolor_l1'],0)
        data['color_theme_l'] = self.textContrast(data['bgcolor_theme'],0)
        data['color_theme_d'] = self.textContrast(data['bgcolor_theme'],1)
        data['color_d1'] = self.textContrast(data['bgcolor_d1'],1)
        data['color_d2'] = self.textContrast(data['bgcolor_d2'],1)
        data['color_d3'] = self.textContrast(data['bgcolor_d3'],1)
        data['color_d4'] = self.textContrast(data['bgcolor_d4'],1)
        data['color_d5'] = self.textContrast(data['bgcolor_d5'],1)
        
        #shadow_rgb = hex_to_rgb(data['bgcolor_d5'])
        #data['shadow_l'] = str(int(shadow_rgb[0]*255.0))+','+str(int(shadow_rgb[1]*255.0))+','+str(int(shadow_rgb[2]*255.0))
        #shadow_rgb = hex_to_rgb(data['bgcolor_l5'])
        #data['shadow_d'] = str(int(shadow_rgb[0]*255.0))+','+str(int(shadow_rgb[1]*255.0))+','+str(int(shadow_rgb[2]*255.0))
        
        with open(CSS_TPL_PATH) as file_:
            template = Template(file_.read())
            
        Path(config.data["site_dir"] + '/css/').mkdir(parents=True, exist_ok=True)
        w3_theme_css_path = Path(config.data["site_dir"] + '/css/w3-theme.css')
        with open(w3_theme_css_path, "w") as file:
            file.write(template.render(data))
