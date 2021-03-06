from __future__ import print_function
import os
import re

node_version_h = os.path.join(
    os.path.dirname(__file__),
    '..',
    'src',
    'node_version.h')

f = open(node_version_h)

for line in f:
  if re.match('^#define NODE_MAJOR_VERSION', line):
    major = line.split()[2]
  if re.match('^#define NODE_MINOR_VERSION', line):
    minor = line.split()[2]
  if re.match('^#define NODE_PATCH_VERSION', line):
    patch = line.split()[2]

print('%(major)s.%(minor)s.%(patch)s'% locals())
