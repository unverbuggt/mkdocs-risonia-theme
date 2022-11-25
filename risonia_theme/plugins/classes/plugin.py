import os
import sys
import re
from timeit import default_timer as timer
from datetime import datetime, timedelta

from bs4 import BeautifulSoup

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

class W3cssClassesPlugin(BasePlugin):

    config_scheme = (
        ('param', config_options.Type(str, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_page_content(self, html, page, config, files):
        soup = BeautifulSoup(html, 'html.parser')
        for blockquote_tag in soup.find_all('blockquote'):
            blockquote_tag.replace_with('div')
            blockquote_tag['class'] = blockquote_tag.get('class', []) + ['w3-panel', 'w3-theme-l4', 'w3-leftbar', 'w3-border-theme']

        responsive_wrapper = soup.new_tag('div', **{"class": "w3-responsive"})
        
        for table_tag in soup.find_all('table'):
            table_tag['class'] = table_tag.get('class', []) + ['w3-table', 'w3-bordered', 'w3-striped']
            table_tag.wrap(responsive_wrapper)
        
        for pre_tag in soup.find_all('pre'):
            pre_tag['class'] = pre_tag.get('class', []) + ['w3-code', 'w3-responsive']
        
        for code_tag in soup.find_all('code'):
            code_tag['class'] = code_tag.get('class', []) + ['w3-codespan']
        
        for img_tag in soup.find_all('img'):
            img_tag['class'] = img_tag.get('class', []) + ['w3-image']
        
        if 'extlink' in config['theme']._vars and config['theme']._vars['extlink']:
            for link_tag in soup.find_all('a'):
                href = link_tag['href']
                svg_tag = soup.new_tag("svg")
                svg_tag['class'] = "svg-icon svg-1em"
                svg_extlink = soup.new_tag("use")
                svg_extlink['xlink:href'] = "#extlink"
                svg_tag.append(svg_extlink)
                if href.startswith('http://') or href.startswith('https://'):
                    link_tag.append(svg_tag)
        
        return str(soup) #nix! .prettify()
