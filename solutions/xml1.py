__author__ = 'petro-ew'
print("dom parser")
from xml.dom  import minidom

def dom_parser():
    doc = minidom.parse("recipe.xml")
    ingredients = doc.getElementsByTagName("ingredients")[0]
    items = ingredients.getElementsByTagName("item")
    for item in items:
        num = item.getAttribute("num")
        units = item.getAttribute("units")
        text = item.firstChild.data.strip()
        quantity = "%s %s" % (num, units)
        print("%-10s %s" % (quantity, text))
dom_parser()

print("sax parser")
from xml.sax import ContentHandler, parse

class RecipeHandler(ContentHandler):
    def startDocument(self):
        self.initem = False
    def startElement(self, name, attrs):
        if name == 'item':
            self.num = attrs.get('num', '1')
            self.units = attrs.get('units', 'none')
            self.text = []
            self.initem = True
    def endElement(self, name):
        if name == 'item':
            text = "".join(self.text)
            if self.units == 'none': self.units = ""
            unitstr = "%s %s" % (self.num, self.units)
            print("%-10s %s" % (unitstr, text.strip()))
            self.initem = False
    def characters(self, data):
        if self.initem:
            self.text.append(data)

parse("recipe.xml",RecipeHandler())
print("ElementTree parser")

from xml.etree.ElementTree import ElementTree
def element_tree():
    #file = file
    #print(file)
    doc = ElementTree(file="recipe.xml")
    #ingredients = doc.find('ingredients')

    for item in doc.findall(".//item"):
        num = item.get('num')
        units = item.get('units','')
        text = item.text.strip()
        quantity = "%s %s" % (num, units)
        print("%-10s %s" % (quantity, text))

#file = "recipe.xml"
element_tree()

