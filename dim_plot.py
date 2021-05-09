import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D

PATH = "C:\\knv\\Projs\\2021-1\\KnV\\MVTEC_bottle\\"
PATH = 'C:\\knv\\Projs\\2021-1\\KnV\\DATA\\Dataset\\0324_10K_classified_by_human_learning\\train\\normal\\'

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

B = Counter()
G = Counter()
R = Counter()

# for i, filePath in enumerate(prnFile(PATH, PREFIX_PNG)):
#     img = cv2.imread(filePath, cv2.IMREAD_COLOR) # BGR
#     img = np.transpose(img, (2,0,1)) #(900, 900, 3) -> (3, 900, 900)
#     # print(np.shape(img[0].flatten())) 
#     print(img[0])
#     exit(0)
#     # print(Counter(np.array(img[0].flatten())))
#     # B = (B*(i+1) + Counter(img[0].flatten())) / (i+2)
#     # G = (G*(i+1) + Counter(img[1].flatten())) / (i+2)
#     # R = (R*(i+1) + Counter(img[2].flatten())) / (i+2)
#     B = B + Counter(img[0].flatten())
#     G = G + Counter(img[1].flatten())
#     R = R + Counter(img[2].flatten())
#     if i == 10: 
#         break

#     print(f'{i} / {n_img}')

imsize = 128

x = []
y = []

for i in range(imsize):
    for j in range(imsize):
        x.append(i)
        y.append(j)

bz = []

for i, filePath in enumerate(prnFile(PATH, PREFIX_BMP)):
    img = cv2.imread(filePath, cv2.IMREAD_COLOR) # BGR
    print(np.shape(img))
    img = np.transpose(img, (2,0,1))

    bz = img[0].flatten()
    break


    print(f'{i} / {n_img}')

# B_x = B.keys()
# B_y = np.array(list(B.values())) / 10

# G_x = G.keys()
# G_y = G.values()

# R_x = R.keys()
# R = R.values()


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,bz, '.', markersize=1)
plt.show()

