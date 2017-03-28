import numpy as np
from matplotlib import pyplot as plt

x = np.array([1024,2048,4096,8192])
y_nb = np.array([62.21,63.91,65.548,68.19])
y_svm = np.array([63.67,64.88,67.91,70.54])

fig = plt.figure()
#plt.xscale('log',basex=2)

#ax1 = fig.add_subplot(211)
plt.plot(x,y_nb,label='naive bayes')
#ax2 = fig.add_subplot(211)
plt.plot(x,y_svm,label='SVM')

plt.suptitle("Classifier Accuracy")
plt.ylabel("Accuracy(%)")
plt.xlabel("Data size")
plt.legend(loc="best")
plt.show()

