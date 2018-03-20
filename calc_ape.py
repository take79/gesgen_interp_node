import numpy as np
import sys

def create_array_from_file(filename):
  f = open(filename, 'r')
  org = f.readlines()
  for idx, line in enumerate(org):
    #org[idx] = [float(x) for x in offset]
    org[idx] = [float(x) for x in line.split()]

  return np.array(org) 

def APE(predicted, original):
  diffs = np.empty((len(predicted), len(predicted[0])))
  for i in range(len(predicted)):
    for j in range(len(predicted[i])):
      diffs[i][j] = abs(predicted[i][j] - original[i][j])

  frame_avg = np.average(diffs, axis=1)
  all_avg = np.average(frame_avg)
  
  return all_avg

def all_test_apes(): #original-predicted(filtered))のAPE
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_" + sys.argv[2] + "_ape.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_" + sys.argv[2] + ".txt")
    original = create_array_from_file("data/original/gesture" + str(i) + "_pos.txt")

    ape = APE(predicted, original)

    line = str(i) + "," +  str(ape) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_raw_apes(): #original-predicted(raw))のAPE
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_raw_ape.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_pos.txt")
    original = create_array_from_file("data/original/gesture" + str(i) + "_pos.txt")

    ape = APE(predicted, original)

    line = str(i) + "," +  str(ape) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_raw_apes_wflip(): #original(前後逆転l-predicted(filtered))のAPE
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_raw_ape_wflip.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_pos.txt")
    original = create_array_from_file("data/original/gesture" + str(i) + "_pos_flp.txt")

    ape = APE(predicted, original)

    line = str(i) + "," +  str(ape) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_filter_apes_wflip(): #original(前後逆転l-predicted(filtered))のAPE
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_" + sys.argv[2] + "_wflip.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_"  + sys.argv[2] + ".txt")
    original = create_array_from_file("data/original/gesture" + str(i) + "_pos_flp.txt")

    ape = APE(predicted, original)

    line = str(i) + "," +  str(ape) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_exp_apes():
  fw = open("exp/" + sys.argv[1] + "/" + sys.argv[1] + "_exp_ape.txt", 'w')
  out_lines = []
  for i in [1093, 1096, 1107, 1109, 1112, 1119, 1139, 1147, 1159, 1168]:
    hikaku = create_array_from_file("exp/" + sys.argv[1] + "/gesture" + str(i) + "_pos.txt")
    original = create_array_from_file("exp/original/gesture" + str(i) + "_pos.txt")

    ape = APE(hikaku, original)

    line = str(i) + "," +  str(ape) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

if __name__ == "__main__":
  if (int(sys.argv[3]) == 0):
    all_test_apes()
  if (int(sys.argv[3]) == 1):
    all_test_raw_apes()
  if (int(sys.argv[3]) == 2):
    all_exp_apes()
  if (int(sys.argv[3]) == 3):
    all_test_raw_apes_wflip()
  if (int(sys.argv[3]) == 4): #今の結果のAPEを算出するにはコレ
    all_test_filter_apes_wflip()

