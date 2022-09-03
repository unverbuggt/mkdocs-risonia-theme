#!/usr/bin/env python3

import sys
import tinycss
from jinja2 import Template

if len(sys.argv) < 2:
    print("usage: python "+sys.argv[0]+" [textfile]")
    sys.exit()

filename = sys.argv[1]

data = {}

parser = tinycss.make_parser('page3')
stylesheet = parser.parse_stylesheet_file(filename)
for rule in stylesheet.rules:
    if not getattr(rule, 'selector'):
        continue
    path = rule.selector.as_css()
    if path == '.w3-theme-l5':
        data['color_l5'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-l4':
        data['color_l4'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-l3':
        data['color_l3'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-l2':
        data['color_l2'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-l1':
        data['color_l1'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme':
        data['color_theme'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-d1':
        data['color_d1'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-d2':
        data['color_d2'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-d3':
        data['color_d3'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-d4':
        data['color_d4'] = rule.declarations[1].value.as_css()
    elif path == '.w3-theme-d5':
        data['color_d5'] = rule.declarations[1].value.as_css()

with open('w3-theme.css.jinja2') as file_:
    template = Template(file_.read())

with open('_out/'+filename, 'w') as file_:
    file_.write(template.render(data))