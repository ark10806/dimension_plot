import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D

PATH = "C:\\knv\\Projs\\2021-1\\KnV\\MVTEC_bottle\\"
PATH = 'C:\\knv\\Projs\\2021-1\\KnV\\DATA\\Dataset\\0324_10K_classified_by_human_learning\\train\\normal\\'
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

imsize = 128

x = []
y = []
z = []

fig = plt.figure()
ax = fig.gca(projection='3d')

def BGR2HEX(dec:int)->str:
    b_int, g_int, r_int = 0, 0, 0
    color = []

    b_int = int(dec / (256*256))
    color.append(b_int)
    g_int = int((dec - b_int*(256*256)) / 256)
    color.append(g_int)
    r_int = int((dec - b_int*(256*256) - g_int*(256)))
    color.append(r_int)

    hex_string = '#'
    hex_string += format(color[0], '02x') + format(color[1], '02x') + format(color[2], '02x')
    return hex_string

for i, filePath in enumerate(prnFile(PATH, PREFIX_BMP)):
    img = cv2.imread(filePath, cv2.IMREAD_COLOR) # BGR (imsize, imsize, 3)
    print(np.shape(img))
    img = np.transpose(img, (2,0,1)) # (3, imsize, imsize)

    for j in range(imsize):
        for k in range(imsize):
            idx = img[0][j][k]*256*256 + img[1][j][k]*256 + img[2][j][k]
            # x.append(i)
            # y.append(j)
            # z.append(idx)
            ax.scatter(j,k,idx, '.', c=BGR2HEX(idx), s=1)
        print(f'{j*k / (imsize * imsize) *100}')

            

    if i ==0:
        break


    print(f'{i} / {n_img}')



# for i in range(np.shape(z)[0]):
#     ax.plot(x[i],y[i],z[i], '.', c=BGR2HEX(z[i]), markersize=1)
plt.show()

