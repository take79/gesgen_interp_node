import numpy as np
import math
import sys
import pyquaternion as pyq

with open (sys.argv[1], 'r') as f:
  raw = f.readlines()

  hierarchy = raw[0:311]
  frames = raw[311:]
  print(len(frames))

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

    node = dict([('name', name), ('parent', parent), ('children', children), ('offset', joint_offsets[idx]), ('rel_degs', None), ('abs_qt', None), ('rel_pos', None), ('abs_pos', None)])
    if idx == 0:
        node['rel_pos'] = node['abs_pos'] = [float(0), float(60), float(0)]
        node['abs_qt'] = pyq.Quaternion() #[z_org_axis, x_org_axis, y_org_axis]
        print(node['rel_pos'])
        print(node['abs_pos'])
    nodes.append(node)

  output_lines = []
  for idx, frame in enumerate(frames):
    frames[idx] = frame.split()

  for frame in frames:
    #print(frame)
    node_idx = 0
    for i in range(51): #changed from 51
      stepi = i*3
      z_deg = float(frame[stepi])
      x_deg = float(frame[stepi+1])
      y_deg = float(frame[stepi+2])

      if nodes[node_idx]['name'] == 'End Site':
        node_idx = node_idx + 1
      nodes[node_idx]['rel_degs'] = [z_deg, x_deg, y_deg]
      current_node = nodes[node_idx]
      #print(current_node['name'])

      node_idx = node_idx + 1
      #print(nodes)

    for start_node in nodes:
      abs_pos = np.array([0, 60, 0])
      current_node = start_node
      #print(">" + current_node['name'])
      if start_node['children'] is not None: #= if not start_node['name'] = 'end site'
        for child_idx in start_node['children']:
          child_node = nodes[child_idx]

          child_offset = np.array(child_node['offset'])
          #print(start_node['rel_degs'])
          qz = pyq.Quaternion(axis=[0, 0, 1], degrees=start_node['rel_degs'][0])
          qx = pyq.Quaternion(axis=[1, 0, 0], degrees=start_node['rel_degs'][1])
          qy = pyq.Quaternion(axis=[0, 1, 0], degrees=start_node['rel_degs'][2])
          qrot = qz * qx * qy
          offset_rotated = qrot.rotate(child_offset)
          child_node['rel_pos']= start_node['abs_qt'].rotate(offset_rotated)

          child_node['abs_qt'] = start_node['abs_qt'] * qrot
          #print(child_node['abs_qt'])
      while current_node['parent'] is not None:
        #print(nodes[current_node['parent']]['name'] + "->")
        abs_pos = abs_pos + current_node['rel_pos']
        current_node = nodes[current_node['parent']]
      start_node['abs_pos'] = abs_pos
      #print("origin")
      #print("-------------------------------------------")

    line = []
    for node in nodes:
      line.append(node['abs_pos'])
    output_lines.append(line)

  print(str(len(output_lines)) + ", " + str(len(output_lines[0])) + ", " + str(len(output_lines[0][0])))
  #print(joint_offsets)
  #print(len(joint_offsets))
  #print(joint_names)
  #print(len(joint_names))
  #for node in nodes:
     #print(node)
  print(nodes[0]['abs_pos'])

  with open(sys.argv[2], 'w') as fr:
    for line in output_lines:
      for pos in line:
        fr.write(str(pos[0]) + " " + str(pos[1]) + " " + str(pos[2]) + ",")
      fr.write("\n")
