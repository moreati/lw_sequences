#!/usr/bin/env python2

import pprint
import re
import sys

codes = {}
node_patt = re.compile(r'\s+([a-z]+[0-9]+) \[URL="http://lesswrong.com/lw/([a-z0-9]+)')
edge_patt = re.compile(r'(\s+)([a-z]+[0-9]+)($| ->|;)')

def replace(m):
    return '%s"%s"%s' % (m.group(1), 
                         codes.get(m.group(2), m.group(2)), 
                         m.group(3))

for line in sys.stdin:
    node = node_patt.match(line)
    if node:
        old = node.group(1)
        new = node.group(2)
        codes[old] = new
        sys.stdout.write(re.sub(r'^(\s+)([a-z]+[0-9]+)', r'\g<1>"%s"' % new, line))
        continue
    
    edge = edge_patt.match(line)
    if edge:
        sys.stdout.write(re.sub(edge_patt, replace, line))
        continue
    
    sys.stdout.write(line)

