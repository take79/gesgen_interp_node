import numpy as np
import sys

def del_vel_from_list(predicted):
  for i in range(len(predicted)):
    predicted[i] = predicted[i].split()

  pos_list = []
  for idx, line in enumerate(predicted):
    three_flg = False
    line = []
    for i, el in enumerate(predicted[idx]):
      if i%3 == 0:
        three_flg = not three_flg

      if three_flg:
        line.append(float(el))
    pos_list.append(line)

  return pos_list

def all_del_vel():
  for i in range(1093, 1183):
    filename = "data/" + sys.argv[1] + "/" + sys.argv[2] + "/gesture" + str(i) + ".txt"
    f = open(filename, 'r')
    raw = f.readlines()
    res = del_vel_from_list(raw)
    fw = open(filename.replace('.txt', '_pos.txt'), 'w')
    for line in res:
      for el in line:
        fw.write(str(el) + " ")
      fw.write("\n")

if __name__ == "__main__":
  #f = open("data/" + sys.argv[1] + "/" + sys.argv[2], 'r')
  #raw = f.readlines()
  #res = del_vel_from_list(raw)
  #fw = open(sys.argv[1].replace('.txt', '_pos.txt'), 'w')
  #for line in res:
  #  for el in line:
  #    fw.write(str(el) + " ")
  #  fw.write("\n")
  all_del_vel()

