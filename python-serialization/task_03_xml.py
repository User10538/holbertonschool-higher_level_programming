#!/usr/bin/python3
import xml.etree.ElementTree as ET

#dictionary to XML
def serialize_to_xml(dictionary, filename):
    root = ET.Element("Data")
    for k in dictionary.keys():
        ET.SubElement(root, k).text = dictionary[k]

    tree = ET.ElementTree(root)
    tree.write(filename)
    
#XML to dictionary    
def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
