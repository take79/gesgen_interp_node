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

def average_jerk(predicted):
  print(predicted.shape)
  predicted = predicted.transpose()
  jerks = np.empty((len(predicted), len(predicted[0])-3))
  jerks = np.diff(predicted, n=3)
  jerks = jerks.transpose()
  jerks = np.absolute(jerks)

  print(jerks.shape)
  print("--------------------")

  frame_javg = np.average(jerks, axis=1)
  all_javg = np.average(frame_javg)

  return all_javg


def all_test_apes():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_ape.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_" + sys.argv[2] + ".txt")
    original = create_array_from_file("data/original/gesture" + str(i) + ".txt")

    ape = APE(predicted, original)

    line = str(i) + "," +  str(ape) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_jerks():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_absjerk.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_" + sys.argv[2] + ".txt")

    jerk = average_jerk(predicted)

    line = str(i) + "," +  str(jerk) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close() 

def all_test_raw_jerks():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_raw_absjerk.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_pos.txt")

    jerk = average_jerk(predicted)

    line = str(i) + "," +  str(jerk) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_original_jerks():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_absjerk.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    original = create_array_from_file("data/" + sys.argv[1] + "/gesture" + str(i) + ".txt")

    jerk = average_jerk(original)

    line = str(i) + "," +  str(jerk) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

if __name__ == "__main__":
  if (int(sys.argv[3]) == 0):
    all_test_jerks()
  if (int(sys.argv[3]) == 1):
    all_test_raw_jerks()
  if (int(sys.argv[3]) == 2):
    all_test_original_jerks()

