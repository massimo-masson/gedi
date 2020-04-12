#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='cogen package',sqlschema='cogen',sqlprefix=True,
                    name_short='Cogen', name_long='Cogen', name_full='Cogen')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
