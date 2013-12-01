#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("XDG_CONFIG_HOME", get.workDIR())
shelltools.export("PKG_CONFIG_PATH", "/usr/local/lib/pkgconfig")

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

# By PiSiDo 2.0.0
