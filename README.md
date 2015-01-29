ArcGIS Desktop Python AddIn for converting selected features to a definition query.

Built and tested on ArcGIS 10.3

Install: Run Selection_to_DefQuery2.esriaddin

Use: In ArcMap open the Customize dialog and open the "Selection to Def Query" Toolbar. Once open, select a layer from the combobox. Select features from the selected layer (by attribute, on the map, or spatially). Click the button on the left to apply the def query. Click the button on the right to clear the def query.
Thats about it.

Planned enhancements include.
1) ArcScene Support
2) Highlighting when def queries are applied

MANIFEST
========

README.md    : This file

makeaddin.py : A script that will create a .esriaddin file out of this
               project, suitable for sharing or deployment

config.xml   : The AddIn configuration file

Images/*     : all UI images for the project (icons, images for buttons,
               etc)

Install/*    : The Python project used for the implementation of the
               AddIn. The specific python script to be used as the root
               module is specified in config.xml.
