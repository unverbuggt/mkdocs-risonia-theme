import os
import sys
import re
from timeit import default_timer as timer
from datetime import datetime, timedelta

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
        html = re.sub('<blockquote>', '<div class="w3-panel w3-theme-l4 w3-leftbar w3-border-theme">', html)
        html = re.sub('</blockquote>', '</div>', html)
        #html = re.sub('<table>', '<table class="w3-table w3-theme-l4 w3-border w3-bordered w3-hoverable">', html)
        #html = re.sub('<tr>', '<tr class="w3-hover-theme">', html)
        #html = re.sub('<pre>', '<pre class="w3-code">', html)
        #html = re.sub('<code>', '<code class="w3-codespan">', html)
        return html
