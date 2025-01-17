#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='anag package',sqlschema='anag',sqlprefix=True,
                    name_short='Anag', name_long='Anag', name_full='Anag')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
