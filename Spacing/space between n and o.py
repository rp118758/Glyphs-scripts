#MenuTitle: Spacing adhesion
# -*- coding: utf-8 -*-
__doc__="""Opens a new tab from the selected character,creating a placeholder between spacing strings of n and o"""

# -> Robert Pratley aka rp118758 @ GitHub
# -> www.robertpratley.co.uk


import GlyphsApp
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers
entryText = [ thisLayer.parent.name for thisLayer in selectedLayers ]
entryText = "/" + "/ ".join(entryText).replace(' ', '')

newText = entryText + "\n/n/Placeholder/n/n/Placeholder/n/Placeholder/Placeholder/n\n/o/Placeholder/o/o/Placeholder/o/Placeholder/Placeholder/o\n/Placeholder/a/Placeholder/d/Placeholder/h/Placeholder/e/Placeholder/s/Placeholder/i/Placeholder/o/Placeholder/n/Placeholder"


Glyphs.currentDocument.windowController().addTabWithString_( newText )
