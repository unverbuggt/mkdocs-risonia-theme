import os

from colorsys import rgb_to_hls
from colorsys import hls_to_rgb
from jinja2 import Template

from pathlib import Path

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
CSS_TPL_PATH = os.path.join(PLUGIN_DIR, 'w3-theme.css.jinja2')

def hex_to_rgb(value):
    h = value.lstrip('#')
    return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4))

def rgb_to_hex(value):
    return '#%02x%02x%02x' % (int(value[0]*255.0), int(value[1]*255.0), int(value[2]*255.0))

def isDark(value):
    rgb = hex_to_rgb(value)
    hls = rgb_to_hls(rgb[0],rgb[1],rgb[2])
    if hls[1] < 0.5:
        return "#fff"
    else:
        return "#000"

class W3cssColorTheme(BasePlugin):

    config_scheme = (
        ('color', config_options.Type(str, default='#efc050')),
        ('center', config_options.Type(bool, default=False)),
    )
    
    def on_post_build(self, config, **kwargs):
    #def on_pre_build(self, config, **kwargs):
        theme = self.config['color']
        themergb = hex_to_rgb(theme)
        themehls = rgb_to_hls(themergb[0],themergb[1],themergb[2])
        hue = themehls[0]
        if self.config['center']:
            light = 0.5
        else:
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
        
        data['color_l5'] = isDark(data['bgcolor_l5'])
        data['color_l4'] = isDark(data['bgcolor_l4'])
        data['color_l3'] = isDark(data['bgcolor_l3'])
        data['color_l2'] = isDark(data['bgcolor_l2'])
        data['color_l1'] = isDark(data['bgcolor_l1'])
        if self.config['center']:
            data['color_theme_l'] = "#000"
            data['color_theme_d'] = "#fff"
        else:
            data['color_theme_l'] = isDark(data['bgcolor_theme'])
            data['color_theme_d'] = isDark(data['bgcolor_theme'])
        data['color_d1'] = isDark(data['bgcolor_d1'])
        data['color_d2'] = isDark(data['bgcolor_d2'])
        data['color_d3'] = isDark(data['bgcolor_d3'])
        data['color_d4'] = isDark(data['bgcolor_d4'])
        data['color_d5'] = isDark(data['bgcolor_d5'])
                
        with open(CSS_TPL_PATH) as file_:
            template = Template(file_.read())
            
        Path(config.data["site_dir"] + '/css/').mkdir(parents=True, exist_ok=True)
        w3_theme_css_path = Path(config.data["site_dir"] + '/css/w3-theme.css')
        with open(w3_theme_css_path, "w") as file:
            file.write(template.render(data))
