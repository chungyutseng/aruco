#!/usr/bin/env python
import numpy as np
import sys, time, math
# aaa = [[[1, 2], [3, 4], [5, 6], [7, 8]]]
# aaaa = np.array(aaa)
# aaaa = aaaa.reshape(4, 2)
# print(aaaa[0])
# print(aaaa.ndim)

# path = ""
# matrix = np.loadtxt(path + 'test.txt', delimiter=',')
calib_path = ""
camera_matrix = np.loadtxt(calib_path + 'cameraMatrix.txt', delimiter = ',')
print(camera_matrix)