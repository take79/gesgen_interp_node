import numpy as np
import math
import sys
import pyquaternion as pyq

FILE_PATH = sys.argv[1]

def read_pos_to_array(filename):
  with open(filename, 'r') as f:
    raw = f.readlines()
    posvel_list = []
    for line in raw:
      posvel_list.append(line.split())

    pos_list = []
    for idx, line in enumerate(posvel_list):
      three_flg = True
      line = []
      for i, el in enumerate(posvel_list[idx]):

        if three_flg:
          line.append(float(el))
      pos_list.append(line)

  pos_array = np.array(pos_list)
  #print(len(pos_array))
  #print(len(pos_array[0]))
  print(pos_array)

  return pos_array

def write_flip_pos_to_txt(out_data):
  with open(FILE_PATH.replace('.txt', '_flp.txt'), 'w') as fr:
    for line in out_data:
      count = 0
      for idx,el in enumerate(line):
        if (not idx==0) and idx%3 == 0:
         count = count+1
        #print(count * 3)
        #print(idx)
        if idx == count*3:
          fr.write(str(-el) + " ")
        elif idx == count*3+2:
          fr.write(str(-el) + " ")
        elif idx == count*3+1:
          fr.write(str(el) + " ")
          #print(idx)
      fr.write("\n")

if __name__ == '__main__':
  pos_array = read_pos_to_array(FILE_PATH)
  #print(pos_array)
  write_flip_pos_to_txt(pos_array)

