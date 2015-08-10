# !/usr/bin/env python
# coding:utf-8
# Author: D.E.Smith
# Date:
# Description:
# Notes: 
# Dependencies: arcpy, os
# Archetecture: 32bit, 64bit (with proper installs)
# Modified by Mat Savage 8/6/2015

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
        val = arcpy.mapping.ListLayers(mxd, selection)[0]
        self.selected_layer = arcpy.mapping.Layer(val)
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
        lyr = arcpy.mapping.Layer(layer_list.value)
        lyr.definitionQuery = ""
        arcpy.RefreshActiveView()

class select_to_defQuery(object):
    """Implementation for Selection_Set_To_Definition_Query_addin.select_to_defQuery (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def_query = ""
        #print layer_list.value
        lyr = layer_list.value
        d = arcpy.Describe(lyr) #Describe the layer
        if lyr.isFeatureLayer:
            objectIDField = d.featureClass.OIDFieldName #Get the official OID field in case it's something weird
        else:
            return #this only works on feature layers
        selectedObjectIDs = d.FIDSet #this gets the selected set of OIDs: [1;2;3]
        selectedObjectIDs = str(selectedObjectIDs.split(";")).replace("[","(").replace("]",")").replace("'","").replace("u","") #format it so it looks like (1,2,3)
        if selectedObjectIDs != "()": #if there's anything in there, do it
            lyr.definitionQuery = objectIDField + " in " + selectedObjectIDs #OBJECTID IN (1,2,3)
            arcpy.RefreshActiveView()
        else:
            pythonaddins.MessageBox("No features are selected in the current layer!","Error") #No features selected? That's a paddlin'
        #print def_query
        
def vectorLayerList():
    global layer, mxd, df
    layer = ""
    mxd = arcpy.mapping.MapDocument('current')
    df = arcpy.mapping.ListDataFrames(mxd)[0]    
    return [x for x in arcpy.mapping.ListLayers(mxd,"",df) if x.isFeatureLayer]
        
#----------MAIN----------
def main():
    layers = vectorLayerList()
    
    
    
#-------------------------------------------
if __name__ == "__main__":
    main()
