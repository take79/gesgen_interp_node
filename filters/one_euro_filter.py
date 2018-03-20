# -*- coding: utf-8 -*-
#
# OneEuroFilter.py -
#
# Author: Nicolas Roussel (nicolas.roussel@inria.fr)

import math
import sys
import numpy as np

FILE_PATH = sys.argv[1]
EXTRA_MODE = 0

# ----------------------------------------------------------------------------

class LowPassFilter(object):

    def __init__(self, alpha):
        self.__setAlpha(alpha)
        self.__y = self.__s = None

    def __setAlpha(self, alpha):
        alpha = float(alpha)
        if alpha<=0 or alpha>1.0:
            raise ValueError("alpha (%s) should be in (0.0, 1.0]"%alpha)
        self.__alpha = alpha

    def __call__(self, value, timestamp=None, alpha=None):        
        if alpha is not None:
            self.__setAlpha(alpha)
        if self.__y is None:
            s = value
        else:
            s = self.__alpha*value + (1.0-self.__alpha)*self.__s
        self.__y = value
        self.__s = s
        return s

    def lastValue(self):
        return self.__y

# ----------------------------------------------------------------------------

class OneEuroFilter(object):

    def __init__(self, freq, mincutoff=1.0, beta=0.0, dcutoff=1.0):
        if freq<=0:
            raise ValueError("freq should be >0")
        if mincutoff<=0:
            raise ValueError("mincutoff should be >0")
        if dcutoff<=0:
            raise ValueError("dcutoff should be >0")
        self.__freq = float(freq)
        self.__mincutoff = float(mincutoff)
        self.__beta = float(beta)
        self.__dcutoff = float(dcutoff)
        self.__x = LowPassFilter(self.__alpha(self.__mincutoff))
        self.__dx = LowPassFilter(self.__alpha(self.__dcutoff))
        self.__lasttime = None
        
    def __alpha(self, cutoff):
        te    = 1.0 / self.__freq
        tau   = 1.0 / (2*math.pi*cutoff)
        return  1.0 / (1.0 + tau/te)

    def __call__(self, x, timestamp=None):
        # ---- update the sampling frequency based on timestamps
        if self.__lasttime and timestamp:
            self.__freq = 1.0 / (timestamp-self.__lasttime)
        self.__lasttime = timestamp
        # ---- estimate the current variation per second
        prev_x = self.__x.lastValue()
        dx = 0.0 if prev_x is None else (x-prev_x)*self.__freq # FIXME: 0.0 or value?
        edx = self.__dx(dx, timestamp, alpha=self.__alpha(self.__dcutoff))
        # ---- use it to update the cutoff frequency
        cutoff = self.__mincutoff + self.__beta*math.fabs(edx)
        # ---- filter the given value
        return self.__x(x, timestamp, alpha=self.__alpha(cutoff))

# ----------------------------------------------------------------------------

#implementations for applying this to gesture

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

def apply_one_euro(pos_array):
    pos_along_timestep = pos_array.transpose()

    config = {
        'freq': 20,       # Hz
        'mincutoff': 0.1,  # FIXME
        'beta': 0.08,       # FIXME
        'dcutoff': 1.0     # this one should be ok
        }
    print("#CFG %s"%config)
    oef = OneEuroFilter(**config)

    filtered_pos = []
    for i, joint in enumerate(pos_along_timestep):
        joint_pos = []
        for timestep, pos in enumerate(joint):
            if timestep > 0:
                timestep = timestep * 1.0/config["freq"]
            filt_num = oef(pos, timestep)
            joint_pos.append(filt_num)
            #print(str(pos) + " -> " + filt_num)
        filtered_pos.append(joint_pos)

    filtered_pos_array = np.array(filtered_pos)

    print(filtered_pos_array.transpose().shape)
    return filtered_pos_array.transpose()

def write_pos_to_txt(out_data):
    with open(FILE_PATH.replace('_pos.txt', '_euro.txt'), 'w') as fr:
        for line in out_data:
            for el in line:
                fr.write(str(el) + " ")
            fr.write("\n")

if __name__ == '__main__':

    #print(len(sys.argv))
    if len(sys.argv) > 3:
        EXTRA_MODE = 1
    pos_array = read_pos_to_array(FILE_PATH)
    #print(pos_array)
    res_array = apply_one_euro(pos_array)
    write_pos_to_txt(res_array)

#if __name__=="__main__":
#
#    import random
#
#    duration = 5.0 # seconds
#    
#    config = {
#        'freq': 120,       # Hz
#        'mincutoff': 1.0,  # FIXME
#        'beta': 1.0,       # FIXME
#        'dcutoff': 1.0     # this one should be ok
#        }
#    
#    print "#SRC OneEuroFilter.py"
#    print "#CFG %s"%config
#    print "#LOG timestamp, signal, noisy, filtered"
#    
#    f = OneEuroFilter(**config)
#    timestamp = 0.0 # seconds
#    while timestamp<duration:
#        signal = math.sin(timestamp)
#        noisy = signal + (random.random()-0.5)/5.0
#        filtered = f(noisy, timestamp)
#        print "{0}, {1}, {2}, {3}".format(timestamp, signal, noisy, filtered)
