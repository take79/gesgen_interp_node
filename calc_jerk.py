import numpy as np
import sys

def create_array_from_file(filename):
  f = open(filename, 'r')
  org = f.readlines()
  for idx, line in enumerate(org):
    #org[idx] = [float(x) for x in offset]
    org[idx] = [float(x) for x in line.split()]

  return np.array(org) 

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

def average_velaccel(predicted, d): #calculate average velocity or accell
  #print(predicted.shape)
  predicted = predicted.transpose()
  diffs = np.empty((len(predicted), len(predicted[0])-d))
  diffs = np.diff(predicted, n=d)
  diffs = diffs.transpose()
  diffs = np.absolute(diffs)

  #print(diffs.shape)
  print(diffs[-1])
  print("--------------------")

  frame_avg = np.average(diffs, axis=1)
  all_avg = np.average(frame_avg)

  return all_avg

def all_test_jerks(): #AJ of predicted(filtered)
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_" + sys.argv[2] + "_absjerk.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_" + sys.argv[2] + ".txt")

    jerk = average_jerk(predicted)

    line = str(i) + "," +  str(jerk) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close() 

def all_test_raw_jerks(): #AJ of predicted(raw)
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
    original = create_array_from_file("data/" + sys.argv[1] + "/gesture" + str(i) + "_pos.txt")

    jerk = average_jerk(original)

    line = str(i) + "," +  str(jerk) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_exp_jerks():
  fw = open("exp/" + sys.argv[1] + "/" + sys.argv[1] + "_exp_absjerk.txt", 'w')
  out_lines = []
  for i in [1093, 1096, 1107, 1109, 1112, 1119, 1139, 1147, 1159, 1168]:
    predicted = create_array_from_file("exp/" + sys.argv[1] + "/gesture" + str(i) + "_pos.txt")

    jerk = average_jerk(predicted)

    line = str(i) + "," +  str(jerk) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close() 

def all_exp_vels():
  fw = open("exp/" + sys.argv[1] + "/" + sys.argv[1] + "_exp_vels.txt", 'w')
  out_lines = []
  for i in [1093, 1096, 1107, 1109, 1112, 1119, 1139, 1147, 1159, 1168]:
    predicted = create_array_from_file("exp/" + sys.argv[1] + "/gesture" + str(i) + "_pos.txt")

    diffs = average_velaccel(predicted, 1)

    line = str(i) + "," +  str(diffs) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close() 

def all_test_vels():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_raw_vels.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_pos.txt")

    diffs = average_velaccel(predicted, 1)

    line = str(i) + "," +  str(diffs) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_exp_accels():
  fw = open("exp/" + sys.argv[1] + "/" + sys.argv[1] + "_exp_accels.txt", 'w')
  out_lines = []
  for i in [1093, 1096, 1107, 1109, 1112, 1119, 1139, 1147, 1159, 1168]:
    predicted = create_array_from_file("exp/" + sys.argv[1] + "/gesture" + str(i) + "_pos.txt")

    diffs = average_velaccel(predicted, 2)

    line = str(i) + "," +  str(diffs) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_accels():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_raw_accels.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_pos.txt")

    diffs = average_velaccel(predicted, 2)

    line = str(i) + "," +  str(diffs) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_original_vels():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_original_vels.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    original = create_array_from_file("data/" + sys.argv[1] + "/gesture" + str(i) + "_pos.txt")

    diffs = average_velaccel(original, 1)

    line = str(i) + "," +  str(diffs) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_original_accels():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_original_accels.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    original = create_array_from_file("data/" + sys.argv[1] + "/gesture" + str(i) + "_pos.txt")

    diffs = average_velaccel(original, 2)

    line = str(i) + "," +  str(diffs) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close()

def all_test_filter_vels():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_" + sys.argv[2] + "_vels.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_" + sys.argv[2] + ".txt")

    diffs = average_velaccel(predicted, 1)

    line = str(i) + "," +  str(diffs) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close() 

def all_test_filter_accels():
  fw = open("data/" + sys.argv[1] + "/" + sys.argv[1] + "_" + sys.argv[2] + "_accels.txt", 'w')
  out_lines = []
  for i in range(1093, 1183):
    predicted = create_array_from_file("data/" + sys.argv[1] + "/predicted/gesture" + str(i) + "_" + sys.argv[2] + ".txt")

    diffs = average_velaccel(predicted, 2)

    line = str(i) + "," +  str(diffs) + "\n"
    out_lines.append(line)

  fw.writelines(out_lines)
  fw.close() 


if __name__ == "__main__":
  if (int(sys.argv[3]) == 0): #testのAJ(filtered)
    all_test_jerks()
  if (int(sys.argv[3]) == 1):
    all_test_raw_jerks()
  if (int(sys.argv[3]) == 2):
    all_test_original_jerks()
  if (int(sys.argv[3]) == 3):
    all_exp_jerks()
  if (int(sys.argv[3]) == 4):
    all_test_vels()
  if (int(sys.argv[3]) == 5):
    all_test_accels()
  if (int(sys.argv[3]) == 6):
    all_test_original_vels()
  if (int(sys.argv[3]) == 7):
    all_test_original_accels()
  if (int(sys.argv[3]) == 8):
    all_test_filter_vels()
  if (int(sys.argv[3]) == 9):
    all_test_filter_accels()

