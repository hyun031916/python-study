'''
p236
<movie>
    <title>트랜스포머</title>
    <genre>SF</genre>
    <rating>8</rating>
</movie>
<phonebook>
    <name>일미림</name>
    <phone>010-1111-2222</phone>
</phonebook>
'''
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

root = Element('movie')
title = SubElement(root, 'title')
title.text = '트렌스포머'
genre = SubElement(root, 'title')
genre.text = 'SF'
rating = SubElement(root, 'rating')
rating.text = '8'

ET.ElementTree(root).write('movie.xml', encoding="utf8", xml_declaration=False)