import xml.etree.ElementTree as ET

estructura_xml = ET.parse("reg1.xml",'rb')


raiz = estructura_xml.getroot()

for reg1 in raiz:
	print (reg1.tag)