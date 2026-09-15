import skimage.io as io
import matplotlib.pyplot as plt

w = io.imread(r"C:\Users\CJCU\Desktop\test\wombats.png")

plt.imshow(w, cmap='gray')