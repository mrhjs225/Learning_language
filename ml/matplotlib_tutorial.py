import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
x=np.arange(0,6,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
plt.plot(x,y1, label="sin")
plt.plot(x,y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin&cos")
plt.legend()
plt.show()

# img = imread("C:/Users/mrhjs/Desktop/Programming/tower.jpg")

# plt.imshow(img)
# plt.show()
plt.plot([1,2,3,4], [1,4,9,16], "ro")
plt.axis([0,6,0,20])
plt.show()

plt.plot(x, y1, x, y2, x, y3)
plt.show()