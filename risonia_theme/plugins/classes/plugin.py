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
            blockquote_tag.name = 'div' #convert blockquote to <div>
            blockquote_tag['class'] = blockquote_tag.get('class', []) + ['w3-panel', 'w3-theme-l3', 'w3-leftbar', 'w3-border-theme'] #add classes
        
        for table_tag in soup.find_all('table'):
            responsive_wrapper = soup.new_tag('div', **{"class": "w3-responsive"})
            table_tag['class'] = table_tag.get('class', []) + ['w3-table', 'w3-bordered', 'w3-striped'] #add classes to <table>
            table_tag.wrap(responsive_wrapper) #wrap tables in w3-responsive <div>
        
        for code_tag in soup.find_all('code'):
            if 'pre' not in code_tag.parent.name: #if not a code block
                code_tag['class'] = code_tag.get('class', []) + ['w3-codespan'] #add class to code
        
        for pre_tag in soup.find_all('pre'):
            pre_tag['class'] = pre_tag.get('class', []) + ['w3-code', 'w3-responsive'] #add classes to code block
        
        for img_tag in soup.find_all('img'):
            img_tag['class'] = img_tag.get('class', []) + ['w3-image'] #add class to <image>
        
        #add extlink svg after external links if configured
        if 'extlink' in config['theme']._vars and config['theme']._vars['extlink']:
            for link_tag in soup.find_all('a'):
                href = link_tag['href']
                svg_tag = soup.new_tag("svg")
                svg_tag['class'] = "svg-1em"
                svg_extlink = soup.new_tag("use")
                svg_extlink['xlink:href'] = "#extlink"
                svg_tag.append(svg_extlink)
                if href.startswith('http://') or href.startswith('https://'):
                    link_tag.append(svg_tag)
        
        #send external links to new tab?
        if 'extblank' in config['theme']._vars and config['theme']._vars['extblank']:
            for link_tag in soup.find_all('a'):
                if href.startswith('http://') or href.startswith('https://'):
                    if not 'target' in link_tag:
                        link_tag['target'] = '_blank'
        
        return str(soup)
