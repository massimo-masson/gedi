#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='ftel package',sqlschema='ftel',sqlprefix=True,
                    name_short='Ftel', name_long='Ftel', name_full='Ftel')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
