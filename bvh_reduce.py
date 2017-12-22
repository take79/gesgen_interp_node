from __future__ import absolute_import
import numpy as np
import sys

def gesturefile_to_label_vector(gesture_filename):
    f = open(gesture_filename, 'r')

    # read all lines of the bvh file
    org = f.readlines()
    # delete the HIERARCHY part
    offset = org[3]
    offset = offset.split()
    del offset[0]
    print(offset)
    del org[0:311]
    bvh_len = len(org)

    for idx, line in enumerate(org):
        org[idx] = [float(x) for x in offset]
        org[idx].extend([float(x) for x in line.split()])

    for i in range(0, bvh_len):
        for j in range(1, 306/3):
            st = j*3
            del org[i][st:st+3]

    train_labels = np.array(org)

    # only keep every second label (BiRNN stride = 2)
    #train_labels = train_labels[::2]

    #train_labels = np.delete(train_labels, np.s_[0:150], 1)

    print(train_labels.shape)

    f.close()

    return train_labels

if __name__ == "__main__":
    bvh_filename = sys.argv[1]
    out_filename = sys.argv[2]
    train_labels = gesturefile_to_label_vector(bvh_filename)
    with open('hformat.txt', 'r') as ftemp:
        hformat = ftemp.readlines()
        del hformat[-1]

    #print(train_labels.shape)
    with open(out_filename, 'w') as fo:
        #offset = [0, 60, 0]
        #offset_line = "\tOFFSET " + " ".join("{:.6f}".format(x) for x in offset) + '\n'
        #fo.write("HIERARCHY\n")
        #fo.write("ROOT Hips\n")
        #fo.write("{\n")
        #fo.write(offset_line)
        fo.writelines(hformat)
        fo.write("MOTION\n")
        #train_labels = train_labels[::10]
        fo.write("Frames: " + str(len(train_labels)) + '\n')
        fo.write("Frame Time: 0.010000\n")
        for row in train_labels:
            row = np.delete(row, np.s_[0:3])
            row[0:3] = 0
            #print(row)
            #print("-----------------------")
            #label_line = " ".join(str(x) for x in row)
            label_line = " ".join("{:.6f}".format(x) for x in row) + " "
            fo.write(label_line + '\n')

