# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

INTERPRETERS = {
    'bash': {'shell', 'bash'},
    'csh': {'shell', 'csh'},
    'dash': {'shell', 'dash'},
    'nix-shell': {'shell', 'bash'},
    'node': {'javascript'},
    'nodejs': {'javascript'},
    'perl': {'perl'},
    'python': {'python'},
    'python2': {'python', 'python2'},
    'python3': {'python', 'python3'},
    'ruby': {'ruby'},
    'sh': {'shell', 'sh'},
    'tcsh': {'shell', 'tcsh'},
    'zsh': {'shell', 'zsh'},
}
