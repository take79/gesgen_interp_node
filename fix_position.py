import numpy as np
import math
import sys
import pyquaternion as pyq

def fix_root_spines(frames, zero_abspos):
  pos_only = []
  for idx, frame in enumerate(frames):
    frames[idx] = frame.split()

  for frame in frames:
    pos_line = []
    for idx in range(64):
      step = idx * 6
      pos_line.append([float(frame[step]), float(frame[step+1]), float(frame[step+2])])
    pos_only.append(pos_line)

  legs_zero_abspos = zero_abspos[192-3*10:]
  #print(legs_zero_abspos)
  #print(len(legs_zero_abspos))

  #print(range(34,64))
  #print(len(range(34,64)))


  #diffs = []
  #for idx, frame in enumerate(pos_only):
  #  diff_line = []
  #  for num in range(3):
  #    st = num * 3
  #    diff_line.append([float(frame[num][0]) - float(zero_abspos[st]), float(frame[num][1]) - float(zero_abspos[st + 1]), float(frame[num][2]) - float(zero_abspos[st + 2])])
  #    pos_only[idx][num] = [float(zero_abspos[st]), float(zero_abspos[st+1]), float(zero_abspos[st+2])]
  #  diffs.append(diff_line)

  diffs = []

  print(pos_only[0][6])
  print([zero_abspos[90], zero_abspos[91], zero_abspos[92]])
  for idx, frame in enumerate(pos_only):
    diff_line = []
    diff_line.append([float(frame[3][0]) - float(zero_abspos[9]), float(frame[3][1]) - float(zero_abspos[10]), float(frame[3][2]) - float(zero_abspos[11])])
    diff_line.append([float(frame[6][0]) - float(zero_abspos[90]), float(frame[6][1]) - float(zero_abspos[91]), float(frame[6][2]) - float(zero_abspos[92])])
    diff_line.append([float(frame[30][0]) - float(zero_abspos[18]), float(frame[30][1]) - float(zero_abspos[19]), float(frame[30][2]) - float(zero_abspos[20])])
    for num in range(4):
      st = num * 3
      pos_only[idx][num] = [float(zero_abspos[st]), float(zero_abspos[st+1]), float(zero_abspos[st+2])]
    pos_only[idx][6] = [float(zero_abspos[18]), float(zero_abspos[19]), float(zero_abspos[20])]
    pos_only[idx][30] = [float(zero_abspos[90]), float(zero_abspos[91]), float(zero_abspos[92])]
    diffs.append(diff_line)

  print(diffs[0])

  #diff_sums = []
  #for frame in diffs:
  #  frame_sum = [0, 0, 0]
  #  for joint_diff in frame:
  #    for i in range(3):
  #      frame_sum[i] = frame_sum[i] + joint_diff[i]
  #  diff_sums.append(frame_sum)

  #print(len(diff_sums))
  #print(diff_sums)

  #for num in range(len(pos_only)):
  #  for idx in range(len(diff_sums[0])):
  #    for jn in range(3, 64):
  #      print(jn)
  #      for i in range(3):
  #        pos_only[num][jn][i]= pos_only[num][jn][i] - diff_sums[num][i]

  for idx, frame in enumerate(diffs):
    #print(idx)
    for i in range(4,6):
      for j in range(3):
        pos_only[idx][i][j] = pos_only[idx][i][j] - frame[0][j]
    for i in range(7, 30):
      for j in range(3):
        pos_only[idx][i][j] = pos_only[idx][i][j] - frame[1][j]
    for i in range(31, 54):
      for j in range(3):
        pos_only[idx][i][j] = pos_only[idx][i][j] - frame[2][j]

  for ln in range(len(pos_only)):
    for idx in range(54,64):
      #print(idx)
      st = (idx-54)*3
      #print(st)
      pos_only[ln][idx] = [float(legs_zero_abspos[st]), float(legs_zero_abspos[st+1]), float(legs_zero_abspos[st+2])]

  #print pos_only

  return pos_only

def write_pos_to_txt(out_data):
  with open(sys.argv[2], 'w') as fr:
    for line in out_data:
      for el in line:
        fr.write(str(el[0]) + " " + str(el[1]) + " " + str(el[2]) + " ")
      fr.write("\n")

if __name__ == '__main__':
  #f = open('hierarchy.txt', 'r')
  #hierarchy = f.readlines()
  #f.close()
  #nodes = create_hierarchy_nodes(hierarchy)
  f = open('gesture1169_zero_pos.txt', 'r')
  zero_abspos = f.readline().split()

  fb = open(sys.argv[1], 'r')
  frames = fb.readlines()
  fb.close()
  out_data = fix_root_spines(frames, zero_abspos)
  write_pos_to_txt(out_data)
