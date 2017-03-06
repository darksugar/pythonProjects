# #Authon Ivor
#
# import xml.etree.ElementTree as et
#
# tree = et.parse("test.xml")
# root = tree.getroot()
# print(root.tag)
#
# #遍历xml文档
# for child in root:
#     print(child.tag,child.attrib)
#     for i in child:
#         print(i.tag,i.text)
#
# #只遍历year节点
# for node in root.iter("year"):
#     print(node.tag,node.text)
#
# #修改
# for node in root.iter("year"):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updates","yes")
#
# tree.write("test2.xml")
#
# #删除
# for country in root.iter("country"):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write("test3.xml")
#
# 创建xml
#
# tree = et.Element("Tree")
# stu = et.SubElement(tree,"Stu1")
# name = et.SubElement(stu,"name",attrib={"enrolled":"yes"})
# name.text = "ivor"
# age = et.SubElement(stu,"age",attrib={"checked":"no"})
# age.text = "22"
# stu2 = et.SubElement(tree,"Stu2")
# name = et.SubElement(stu2,"name",attrib={"enrolled":"yes"})
# name.text = "dark"
# age = et.SubElement(stu2,"age",attrib={"checked":"no"})
# age.text = "23"
#
# et = et.ElementTree(tree)
# et.write("test4.xml",encoding="utf-8",xml_declaration=True)