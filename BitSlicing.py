import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
  img = cv2.imread('dog.jpg',0)
  r,c = img.shape
  img2 = np.zeros((r,c),dtype = np.uint8)
  
  for i in range(8):
    x = (1 << i)
    for j in range(r):
      for k in range(c):
        img2[j,k] = img[j][k] & x
    
    plt.subplot(2,4,i+1)
    plt.imshow(img2,cmap = 'gray')
    plt.title('Bit Slice '+str(i)+' Image')
    
  plt.savefig('sliceFig.png')
    
  plt.show()
  
if __name__ == '__main__':
  main()