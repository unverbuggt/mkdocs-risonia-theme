import os

from colorsys import rgb_to_hls
from colorsys import hls_to_rgb
from jinja2 import Template

from pathlib import Path

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
CSS_TPL_PATH = os.path.join(PLUGIN_DIR, 'w3-theme.jinja2.py')

def hex_to_rgb(value):
    h = value.lstrip('#')
    return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4))

def rgb_to_hex(value):
    return '#%02x%02x%02x' % (int(value[0]*255.0), int(value[1]*255.0), int(value[2]*255.0))

class W3cssColorTheme(BasePlugin):

    config_scheme = (
        ('theme_color', config_options.Type(str, default='#efc050')),
        ('light_text_color', config_options.Type(str, default='#000')),
        ('dark_text_color', config_options.Type(str, default='#fff')),
    )

    def isDark(self, value, prefDark):
        #got it from here: https://www.w3schools.com/lib/w3color.js
        #respectively https://www.w3.org/TR/AERT#color-contrast
        rgb = hex_to_rgb(value)
        perceived_luminance = (((rgb[0] * 255 * 299) + (rgb[1] * 255 * 587) + (rgb[2] * 255 * 114)) / 1000)
        if perceived_luminance > 96 and perceived_luminance < 160:
            if prefDark:
                return self.config['dark_text_color']
            else:
                return self.config['light_text_color']
        elif perceived_luminance < 128:
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
        
        data['color_l5'] = self.isDark(data['bgcolor_l5'],0)
        data['color_l4'] = self.isDark(data['bgcolor_l4'],0)
        data['color_l3'] = self.isDark(data['bgcolor_l3'],0)
        data['color_l2'] = self.isDark(data['bgcolor_l2'],0)
        data['color_l1'] = self.isDark(data['bgcolor_l1'],0)
        data['color_theme_l'] = self.isDark(data['bgcolor_theme'],0)
        data['color_theme_d'] = self.isDark(data['bgcolor_theme'],1)
        data['color_d1'] = self.isDark(data['bgcolor_d1'],1)
        data['color_d2'] = self.isDark(data['bgcolor_d2'],1)
        data['color_d3'] = self.isDark(data['bgcolor_d3'],1)
        data['color_d4'] = self.isDark(data['bgcolor_d4'],1)
        data['color_d5'] = self.isDark(data['bgcolor_d5'],1)
        
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