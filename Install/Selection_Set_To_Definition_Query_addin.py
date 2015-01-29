# !/usr/bin/env python
# coding:utf-8
# Author: D.E.Smith
# Date:
# Description:
# Notes: 
# Dependencies: arcpy, os
# Archetecture: 32bit, 64bit (with proper installs)

# imports
import arcpy
import pythonaddins

class layer_list(object):
    """Implementation for Selection_Set_To_Definition_Query_addin.layer_list (ComboBox)"""
    selected_layer =""
    def __init__(self):
        self.items = vectorLayerList()
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWWWWW'
        self.width = 'WWWWWW'
        self.selected_layer=""
    def onSelChange(self, selection):
        self.items = vectorLayerList()
        self.selected_layer = arcpy.mapping.ListLayers(mxd, selection)[0]
        print self.selected_layer
        self.refresh()
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        self.items = vectorLayerList()
    def onEnter(self):
        pass
    def refresh(self):
        self.items = vectorLayerList()

class remove_defQuery(object):
    """Implementation for Selection_Set_To_Definition_Query_addin.remove_defQuery (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        layer_list.value.definitionQuery = ""
        arcpy.RefreshActiveView()

class select_to_defQuery(object):
    """Implementation for Selection_Set_To_Definition_Query_addin.select_to_defQuery (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def_query = ""
        print layer_list.value
        oids = [x.OBJECTID for x in arcpy.SearchCursor(layer_list.value)]
        for oid in oids:
            def_query += "OBJECTID = {} OR ".format(oid)
        layer_list.value.definitionQuery = def_query[:-4]
        arcpy.RefreshActiveView()
        print def_query
        
def vectorLayerList():
    global layer, mxd, df
    layer = ""
    mxd = arcpy.mapping.MapDocument('current')
    df = arcpy.mapping.ListDataFrames(mxd)[0]    
    return [x for x in arcpy.mapping.ListLayers(mxd,"",df) if x.isFeatureLayer]
        
#----------MAIN----------
def main():
    mxd = arcpy.mapping.MapDocument('current')
    df = arcpy.mapping.ListDataFrames(mxd)[0]    
    layers = [x for x in arcpy.mapping.ListLayers(mxd,"",df) if x.isFeatureLayer]
    
    
    
#-------------------------------------------
if __name__ == "__main__":
    main()