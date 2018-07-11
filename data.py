import json
import pprint
from collections import OrderedDict

from parent import data
from master_parent import child



#Global variables
tree = []
result = []
dataMap = {}



def recursion(id):
    temp = {}
    for x in data:
        if x['parent_id'] == id:
            temp = {
                'id': x['id'],
                'parent_id': x['parent_id'],
                'description': x['description'],
                'url': x['url'],
                'conf': x['conf'],
                'icon': x['icon'],
                'isactive': x['isactive'],
                'isoption': x['isoption']
            }
            if str(temp) not in str(tree):
                tree.append(temp)
            recursion(x['id'])

#Recursion begin
for x in data:
  #recurs each data
  recursion(x['id'])

#Add all master parent (parent_id is 0).
for x in child:
  tree.append(x)

#Creating dataMap (Creating a list of dictionary to be compare to the data)
for x in tree:
  dataMap[x['id']] = x


print('Enter constructTree() to begin')
print('Enter print_tree() to show the result')

#Call this to begin the tree construct
def constructTree():
  for x in tree:

    #check if the parent id is 0=Master Parent
    if x['parent_id'] == 0:
      parent = False
    else:
      parent = dataMap[x['parent_id']]

    #Check if the parent has child
    if parent:
      parent['children'] = []
      #create child if there is no child
      parent['children'].append(x)

    else:
      #Append to result if no child
      result.append(x)
    
#Call this to print the Tree
def print_tree():
  #Print the result
  print(json.dumps(result, indent=2))
  
