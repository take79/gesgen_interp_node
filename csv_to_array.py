from os import path
import csv

for i in range(1,1183):
  file_path = path.abspath(path.join("data", "gesture" + str(i) + ".bvh"))
  out_file_path = path.abspath(path.join("data", "gesture" + str(i) + ".csv"))
  try:
    rf = open(file_path, "r")
    # read all lines of the bvh file
    raw = rf.readlines()
    del raw[0:311]
    wf = open(out_file_path, "w")
    csv_writer = csv.writer(wf, lineterminator='\n', escapechar=',', quoting=csv.QUOTE_NONE)
    for line in raw:
      line = line.split(" ")
      del line[-1]
      csv_writer.writerow(line)
  except IOError:
    print("file gesture" + str(i) + ".bvh doesn't exist, skipping...")
    continue

