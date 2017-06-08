#Authon Ivor
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

yml_filename = input(">>>:")
yaml_file = open(yml_filename,'r')
data = yaml.load(yaml_file)
print(data)

for key, val in data.items():
    print(key, val)