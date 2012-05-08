#!/usr/bin/env python

from HTMLElement import HTMLElement
from attr_property import attr_property

class HTMLFrameSetElement(HTMLElement):
    def __init__(self, doc, tag):
        HTMLElement.__init__(self, doc, tag)

    cols            = attr_property("cols")
    rows            = attr_property("rows")

