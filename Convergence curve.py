import scipy.sparse as sp
#import gym
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from math import floor

data = np.loadtxt('./save/network_scalefree_60-90/reward_data_save_0-400.txt')
data_2 = np.loadtxt('./save/network_scalefree_60-90/reward_data_save_400-600.txt')
data_=np.concatenate((data,data_2), axis=0)
#data_=data_[:,50:]
ave=np.average(data_, axis=1)
x=np.linspace(1,600,600)
MAX= np.max(data_, axis=1)
MIN = np.min(data_, axis=1)

plt.figure(figsize=(12, 5), dpi=200)

plt.subplot(121)
plt.plot(x, ave, '-', color='orange')
plt.fill_between(x, MIN, MAX,color='orange', alpha=0.2)
plt.title('SHATTER-OODA-node-unweighted', fontsize=11,y=0.9)
plt.ylabel("ANOC")
plt.xlabel("Number of training iterations/250")


data_weighted = np.loadtxt('./save/network_scalefree_60-90/reward_data_cost_save_0-400.txt')
data_weighted_2 = np.loadtxt('./save/network_scalefree_60-90/reward_data_cost_save_400-600.txt')
# data_weighted_3 = np.loadtxt('./save/network_scalefree_60-90/reward_data_cost_save_200-300.txt')
data_weighted_=np.concatenate((data_weighted,data_weighted_2), axis=0)
# data_weighted_=data_weighted_[:,50:]
ave_weighted=np.average(data_weighted_, axis=1)
x=np.linspace(1,600,600)
MAX_weighted= np.max(data_weighted_, axis=1)
MIN_weighted = np.min(data_weighted_, axis=1)

plt.subplot(122)
plt.plot(x, ave_weighted, '-', color='orange')
plt.fill_between(x, MIN_weighted, MAX_weighted,color='orange', alpha=0.2)
plt.title('SHATTER-OODA-node-weighted', fontsize=11,y=0.9)
plt.ylabel("ANOC")
plt.xlabel("Number of training iterations/250")
plt.savefig('./save/train.png', format='png', bbox_inches='tight')
plt.show()
print('')

