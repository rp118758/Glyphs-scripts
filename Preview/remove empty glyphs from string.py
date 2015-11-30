#MenuTitle: Remove missing glyphs from sample string
# -*- coding: utf-8 -*-
__doc__="""Opens a new tab from selected sample text, removing glyphs that contain no paths (excluding word spaces)"""

# -> Robert Pratley aka rp118758 @ GitHub
# -> www.robertpratley.co.uk

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers
entryText = [ thisLayer.parent.name for thisLayer in selectedLayers ]

emptyGlyphs = []
for thisLayer in selectedLayers:
	numberOfPaths = len(thisLayer.paths)
	if numberOfPaths < 1:
		if thisLayer.parent.name != 'space':
			emptyGlyphs.append(thisLayer.parent.name)
			
newText = [x for x in entryText if x not in emptyGlyphs]
newText = "/" + "/ ".join(newText).replace(' ', '')

Glyphs.currentDocument.windowController().addTabWithString_( newText )
