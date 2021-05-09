import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D

PATH_mvtec = "C:\\knv\\Projs\\2021-1\\KnV\\MVTEC_bottle\\"
PATH_knv = 'C:\\knv\\Projs\\2021-1\\KnV\\DATA\\Dataset\\0324_10K_classified_by_human_learning\\train\\normal\\'
# PATH = 'C:\\normal\\'

PREFIX_BMP = '.bmp'
PREFIX_PNG = '.png'

global n_img
n_img = 0

def prnFile(rootDir, prefix):
    files = os.listdir(rootDir)
    tmp = []
    global n_img
    
    for file in files:
        path = os.path.join(rootDir, file)
        if(file[-4:] == prefix):
            tmp.append(path)
            n_img += 1
    return tmp

def get_density(PATH, prefixs, imsize):
    xybgr = dict()
    py = []
    for i, filePath in enumerate(prnFile(PATH, prefixs)):
        img = cv2.imread(filePath, cv2.IMREAD_COLOR) # BGR (imsize, imsize, 3)
        img = np.transpose(img, (2,0,1)) # (3, imsize, imsize)

        for j in range(imsize):
            for k in range(imsize):
                xybgr[(j, k, img[0][j][k], img[1][j][k], img[2][j][k])] = 1
        py.append(len(xybgr.keys()) / (255**3 * imsize**2) * 100)

        print(f'{PATH[-5:]}\t{i} / {n_img}')

        # if i==5:
        #     break

    # return len(xybgr.keys()) / (255**3 * imsize**2) * 100
    return len(xybgr.keys()) / (255**3 * imsize**2) * 100, py

mvtec, plot_mvtec = get_density(PATH_mvtec, PREFIX_PNG, 900)
knv, plot_knv = get_density(PATH_knv, PREFIX_BMP, 128)

# plt.plot(plot_mvtec, 'ro')
# plt.plot(plot_knv, '.')
# plt.show()
