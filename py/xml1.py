from lxml import etree

def main():
	xml = etree.parse('conf.xml')
	root = xml.getroot() 
	print root.tag
	for child in root:
		print child.tag, child.attrib, child.text
		for child2 in child:
			print '\t', child2.tag, child2.attrib

main()