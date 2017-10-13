import numpy as np
import math
import sys

with open (sys.argv[1], 'r') as f:
  raw = f.readlines()

  hierarchy = raw[0:311]
  frames = raw[312:]

  joint_offsets = []
  joint_names = []

  for idx, line in enumerate(hierarchy):
    hierarchy[idx] = hierarchy[idx].split()
    #print(hierarchy[idx])
    if not len(hierarchy[idx]) == 0:
      line_type = hierarchy[idx][0]
      if line_type == 'OFFSET':
        offset = np.array([float(hierarchy[idx][1]), float(hierarchy[idx][2]), float(hierarchy[idx][3])])
        joint_offsets.append(offset)
      elif line_type == 'ROOT' or line_type == 'JOINT':
        joint_names.append(hierarchy[idx][1])
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

    if name == 'End Site':
      children = None
    elif idx == 0: #hips
      children = [1, 54, 59]
    elif idx == 2: #spine1
      children = [3, 6, 30]
    elif idx == 9: #lefthand
      children = [10, 14, 18, 22, 26]
    elif idx == 33: #righthand
      children = [34, 38, 42, 46, 50]
    else:
      children = [idx + 1]

    node = dict([('name', name), ('parent', parent), ('children', children), ('offset', joint_offsets[idx]), ('rel_pos', None), ('abs_pos', None)])
    if idx == 0:
        node['rel_pos'] = node['abs_pos'] = [float(0), float(60), float(0)]
    nodes.append(node)

  for idx, frame in enumerate(frames):
    frames[idx] = frame.split()

  relatives = []
  node_idx = 0
  for i in range(51):
    stepi = i*3
    z_deg = float(frames[0][stepi])
    x_deg = float(frames[0][stepi+1])
    y_deg = float(frames[0][stepi+2])

    xrot_mat = np.matrix([[1, 0, 0], [0, np.cos(np.radians(x_deg)), -np.sin(np.radians(x_deg))], [0, np.sin(np.radians(x_deg)), np.cos(np.radians(x_deg))]])
    yrot_mat = np.matrix([[np.cos(np.radians(y_deg)), 0, np.sin(np.radians(y_deg))], [0, 1, 0], [-np.sin(np.radians(y_deg)), 0, np.cos(np.radians(y_deg))]])
    zrot_mat = np.matrix([[np.cos(np.radians(z_deg)), -np.sin(np.radians(z_deg)), 0], [np.sin(np.radians(z_deg)), np.cos(np.radians(z_deg)), 0], [0, 0, 1]])

    if nodes[node_idx]['name'] == 'End Site':
      node_idx = node_idx + 1
    current_node = nodes[node_idx]
    print(current_node['name'])

    for child_idx in current_node['children']:
      child_node = nodes[child_idx]
      child_offset = np.array([child_node['offset']]).T
      child_node['rel_pos'] = np.dot(zrot_mat, np.dot(yrot_mat, np.dot(xrot_mat, child_offset))).A1

    node_idx = node_idx + 1

  for start_node in nodes:
    abs_pos = np.array([0, 0, 0])
    current_node = start_node
    print(">" + current_node['name'])
    while current_node['parent'] is not None:
      print(nodes[current_node['parent']]['name'] + "->")
      abs_pos = abs_pos + current_node['rel_pos']
      current_node = nodes[current_node['parent']]
    start_node['abs_pos'] = abs_pos
    print("origin")
    print("-------------------------------------------")

  #print(joint_offsets)
  print(len(joint_offsets))
  print(joint_names)
  print(len(joint_names))
  for node in nodes:
      print(node)

  #for i in range(len(nodes)):
  #  current_node = nodes[i]
  #  print(">" + current_node['name'])
  #  while current_node['parent'] is not None:
  #    print(nodes[current_node['parent']]['name'] + "->")
  #    current_node = nodes[current_node['parent']]
  #  print("origin")
  #  print("-------------------------------------------")

