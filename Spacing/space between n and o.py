#MenuTitle: Selection and n*nn*n**n/o*oo*o**o to new tab
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

newText = entryText + "\n/n/Placeholder/n/n/Placeholder/n/Placeholder/Placeholder/n\n/o/Placeholder/o/o/Placeholder/o/Placeholder/Placeholder/o"
#newText = entryText + "\n/H/Placeholder/H/H/Placeholder/H/Placeholder/Placeholder/H\n/O/Placeholder/O/O/Placeholder/O/Placeholder/Placeholder/O"
#newText = entryText + "\n/a/Placeholder/d/Placeholder/h/Placeholder/e/Placeholder/s/Placeholder/i/Placeholder/o/Placeholder/n/Placeholder"

class dataPick(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow((500,200))
		self.w.textbox = TextBox((10,10,-10,40), 'Choose a spacing string:')
		self.w.button = Button((10, 10, -10, 20), "n and o", callback=self.buttonCallback)
		self.w.open()
    def buttonCallback(self, sender):
        characters = self.w.newText.get()
		Glyphs.currentDocument.windowController().addTabWithString_( characters )
		self.w.close()

dataPick()

