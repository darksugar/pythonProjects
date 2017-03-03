#Authon Ivor

import xml.etree.ElementTree as et

tree = et.parse("test.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)

#只遍历year节点
for node in root.iter("year"):
    print(node.tag,node.text)

#修改
for node in root.iter("year"):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updates","yes")

tree.write("test2.xml")

#删除
for country in root.findall("country"):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write("test3.xml")