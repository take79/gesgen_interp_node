import numpy as np
import math

with open ('hierarchy.txt', 'r') as f:
  hie = f.readlines()

  joint_offsets = []
  joint_names = []

  for idx, line in enumerate(hie):
    hie[idx] = hie[idx].split()
    print(hie[idx])
    if not len(hie[idx]) == 0:
      line_type = hie[idx][0]
      if line_type == 'OFFSET':
        offset = [float(hie[idx][1]), float(hie[idx][2]), float(hie[idx][3])]
        joint_offsets.append(offset)
      elif line_type == 'ROOT' or line_type == 'JOINT':
        joint_names.append(hie[idx][1])
      elif line_type == 'End':
        joint_names.append('End Site')
  
  nodes = []
  for idx, name in enumerate(joint_names):
    if idx == 0:
      parent = None
    elif idx in [6, 30]: #spine1->shoulders
      parent = 2
    elif idx in [14, 18, 22, 26]: #lefthand->leftfingers
      parent = 9
    elif idx in [38, 42, 46, 50]: #righthand->rightfingers
      parent = 33
    elif idx in [54, 59]: #hip->legs
      parent = 0
    else:
      parent = idx - 1

    node = dict([('name', name), ('parent', parent), ('offsets', joint_offsets[idx])])
    nodes.append(node)

  #xrot_mat = np.matrix([1, 0, 0], [0, np.cos(np.radians(x)), -np.sin(np.radians(x))], [0, np.sin(np.radians(x)), np.cos(np.radians(x))])
  #yrot_mat = np.matrix([np.cos(np.radians(y)), 0, np.sin(np.radians(y))], [0, 1, 0], [-np.sin(np.radians(y)), 0, np.cos(np.radians(y))])
  #zrot_mat = np.matrix([np.cos(np.radians(z)), -np.sin(np.radians(z)), 0], [np.sin(np.radians(z)), np.cos(np.radians(z)), 0], [0, 0, 1])

  print(joint_offsets)
  print(len(joint_offsets))
  print(joint_names)
  print(len(joint_names))
  for node in nodes:
      print(node)

  for i in range(len(nodes)):
    current_node = nodes[i]
    print(">" + current_node['name'])
    while current_node['parent'] is not None:
      print(nodes[current_node['parent']]['name'] + "->")
      current_node = nodes[current_node['parent']]
    print("origin")
    print("-------------------------------------------")

