import numpy as np
import math
import sys
import pyquaternion as pyq

WIN_LEN = int(sys.argv[2]) #Enter odd number; winlen = pastlen + self + futurelen
FILE_PATH = sys.argv[1]
EXTRA_MODE = 0 #if input file has additional data other than pos -> 1

def read_pos_to_array(filename):
  with open(filename, 'r') as f:
    raw = f.readlines()
    posvel_list = []
    for line in raw:
      posvel_list.append(line.split())

    pos_list = []
    for idx, line in enumerate(posvel_list):
      three_flg = False
      line = []
      for i, el in enumerate(posvel_list[idx]):
        if EXTRA_MODE == 0:
          three_flg = True
        elif i%3 == 0:
          three_flg = not three_flg

        if three_flg:
          line.append(float(el))
      pos_list.append(line)

  pos_array = np.array(pos_list)
  #print(len(pos_array))
  #print(len(pos_array[0]))
  print(pos_array)

  return pos_array

def simple_moving_average(pos_array, winlen):
  pos_columns = []
  winlen_oneside = (winlen-1)/2
  for i in range(len(pos_array[0])):
    line = []
    for j in range(len(pos_array)):
      line.append(pos_array[j][i])
    pos_columns.append(line)

  res_list = []
  for i, joint in enumerate(pos_columns):
    line = []
    for j in range(len(pos_columns[i])):
      start_idx = j-winlen_oneside
      end_idx = j+winlen_oneside+1
      if start_idx < 0:
        line.append(np.mean(pos_columns[i][:end_idx]))
      elif end_idx > len(pos_columns[i]):
        line.append(np.mean(pos_columns[i][start_idx:]))
      else:
        line.append(np.mean(pos_columns[i][start_idx:end_idx]))
    res_list.append(line)

  res_array = np.array(res_list)

  print(res_array.shape)
  print(res_array.transpose().shape)
  print(res_array.transpose())

  #print(pos_columns)
  #print(len(pos_columns))
  #print(len(pos_columns[0]))

  return res_array.transpose()

def write_pos_to_txt(out_data):
  with open(FILE_PATH.replace('.txt', '_sma' + str(WIN_LEN) + '.txt'), 'w') as fr:
    for line in out_data:
      for el in line:
        fr.write(str(el) + " ")
      fr.write("\n")

if __name__ == '__main__':
  print(len(sys.argv))
  if len(sys.argv) > 3:
    EXTRA_MODE = 1
  pos_array = read_pos_to_array(FILE_PATH)
  #print(pos_array)
  res_array = simple_moving_average(pos_array, WIN_LEN)
  write_pos_to_txt(res_array)

