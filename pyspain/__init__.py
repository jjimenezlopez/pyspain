# -*- coding: utf-8 -*-
#
# Author: Jose Jiménez (jjimenez@fidesol.org) - Fundación I+D del Software Libre

from db import Database

VERSION = (0, 1, 2, 'beta')

def get_version():
    number = VERSION[0:2]
    main = '.'.join(str(x) for x in number)
    
    sub = ''
    if VERSION[3] != 'final':
        sub = VERSION[3][0]
        
    return main + sub
    
class Spain():
    db = None
    
    def __init__(self):
        self.db = Database()

    def provinces(self):
        dom_provinces = self.db.get_provinces()
        list_provs = []
        for node in dom_provinces:
            list_provs.append(node.getAttribute('name'))

        return list_provs

    def localities(self, province=None):
        if province != None:
            dom_localities = self.db.get_localities(province.decode('utf-8'))
        else:
            dom_localities = self.db.get_all_localities()

        list_localities = []
        if dom_localities != None:
            for node in dom_localities:
                if node.firstChild != None and node.firstChild.nodeType == node.TEXT_NODE:
                    list_localities.append(node.firstChild.nodeValue)

        return list_localities

    def as_hash(self):
        """
        Returns two dictionaries, an example:
        dict_provs = {0: 'province1', 1: 'province2', ...}
        dict_locs = {0: ['locality1', 'locality2'], 1: [...], ... }

        """

        dom_provinces = self.db.get_provinces()
        dict_provs = {}
        dict_locs = {}
        for index, node in enumerate(dom_provinces):
            dict_provs[index] = node.getAttribute('name')
            dom_localities = self.db.get_localities(node.getAttribute('name'))
            list_localities = []
            for loc in dom_localities:
                if loc.firstChild != None and loc.firstChild.nodeType == loc.TEXT_NODE:
                    list_localities.append(loc.firstChild.nodeValue)
            dict_locs[index] = list_localities

        return dict_provs, dict_locs

    def as_hash_with_names(self):
        """
        Returns two dictionaries, an example:
        dict_provs = {0: 'province1', 1: 'province2', ...}
        dict_locs = {0: ['locality1', 'locality2'], 1: [...], ... }

        """

        dom_provinces = self.db.get_provinces()
        dict_provs = {}
        dict_locs = {}
        for index, node in enumerate(dom_provinces):
            dict_provs[node.getAttribute('name')] = node.getAttribute('name')
            dom_localities = self.db.get_localities(node.getAttribute('name'))
            list_localities = []
            for loc in dom_localities:
                if loc.firstChild != None and loc.firstChild.nodeType == loc.TEXT_NODE:
                    list_localities.append(loc.firstChild.nodeValue)
            dict_locs[node.getAttribute('name')] = list_localities

        return dict_provs, dict_locs
