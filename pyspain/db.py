# -*- coding: utf-8 -*-
#
# Author: Jose Jiménez (jjimenez@fidesol.org) - Fundación I+D del Software Libre

from xml.dom.minidom import parse
import os

DB_FILENAME = 'pobmun11.xml'
DB_PATH = os.path.join(os.path.dirname(__file__), 'db')


class Database():

    dom = None

    def __init__(self):
        self.dom = parse(os.path.join(DB_PATH, DB_FILENAME))

    def get_provinces(self):
        return self.dom.getElementsByTagName('province')

    def get_localities(self, province):
        """
        Returns the localities for the given provicne.
        """

        provs = self.dom.getElementsByTagName('province')
        for p in provs:
            if p.getAttribute('name') == province:
                return p.childNodes

        return None

    def get_all_localities(self):
        locs = self.dom.getElementsByTagName('locality')

        return locs
