import cv2
import numpy as np
import matplotlib.pyplot as plt
import io
import random


def createMassObjectDataset(num_dataset:int, num_class:int, size:int):
  X=[]
  y=[]
  for i in range(num_dataset):
    # ポリゴン図形を出力
    points = [[0.55, 0], [1, 0.83], [0.27, 1], [0.0, 0.9], [0.55, 0]]
    points = [[random.randint(0,10), random.randint(0,10)] for i in range(random.randint(1,num_class))]
    patch = patches.Polygon(xy=points, closed=True)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.add_patch(patch)
    ax.autoscale()
#     ax.grid()
#     plt.show()
    # プロット画像を直接メモリで渡す                                                   
    buf = io.BytesIO() # bufferを用意
    plt.savefig(buf, format='png') # bufferに保持
    enc = np.frombuffer(buf.getvalue(), dtype=np.uint8) # bufferからの読み出し
    dst = cv2.imdecode(enc, 1) # デコード
    dst = dst[:,:,::-1] # BGR->RGB
#     plt.clf()
    X = X.append(dst)
    y = y.append(len(points))
    return X, y
