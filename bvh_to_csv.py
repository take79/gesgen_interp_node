import os
import csv

for i in range(1,1183):
  file_path = os.path.abspath(os.path.join("data", "gesture" + str(i) + ".bvh"))
  out_file_path = os.path.abspath(os.path.join("data", "gesture" + str(i) + ".csv"))
  try:
    rf = open(file_path, "r")
    # read all lines of the bvh file
    raw = rf.readlines()

    frametime = raw[310].split()
    print("frametime is " + frametime[2])
    if float(frametime[2]) != 0.0416667 or i == 301:
        print("frame time is correct at 0.01000, skipping...")
        continue

    del raw[0:311]

    for i in range(0, len(raw)):
      raw[i] = raw[i].split()
      for j in range(0, int(306 / 3)):
        st = j * 3
        del raw[i][st:st + 3]
      raw[i] = " ".join(raw[i])

    #print(raw[0])

    wf = open(out_file_path, "w")
    csv_writer = csv.writer(wf, lineterminator='\n', escapechar=',', quoting=csv.QUOTE_NONE)
    for line in raw:
      line = line.split(" ")
      #del line[-1]
      csv_writer.writerow(line)

    if os.system("node interp_from_csv.js " + out_file_path) != 0:
      print("couldn't run interp_from_csv.js on " + out_file_path)

  except IOError:
    print("file gesture" + str(i) + ".bvh doesn't exist, skipping...")
    continue

