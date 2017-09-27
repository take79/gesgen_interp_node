import numpy as np

with open('hformat.txt', 'r') as ftemp:
  hformat = ftemp.readlines()

for i in range(1,1183):

    try:
      rf = open('data/gesture' + str(i) + '_out.csv', 'r')
      frames = rf.readlines()
      for idx, line in enumerate(frames):
        frames[idx] = line.replace(',', ' ')

      with open('data/gesture' + str(i) + '_rev.bvh', 'w') as fo:
        offset = [0,60,0]
        #print(offset)
        #print(offset.shape)
        offset_line = "\tOFFSET " + " ".join("{:.6f}".format(x) for x in offset) + '\n'
        fo.write("HIERARCHY\n")
        fo.write("ROOT Hips\n")
        fo.write("{\n")
        fo.write(offset_line)
        fo.writelines(hformat)
        fo.write("MOTION\n")
        fo.write("Frames: " + str(len(frames)) + '\n')
        fo.write("Frame Time: " + "0.01" + "\n")
        fo.writelines(frames)
        print("bvh created from interpolated data gesture" + str(i) + "_out.csv")

    except IOError:
        print("interpolated data gesture" + str(i) + "_out.csv not found, skipping...")
        continue
