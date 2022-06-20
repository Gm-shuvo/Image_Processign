import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

  img = cv2.imread('dog.jpg',0)
  print(img.shape)
  mask = np.zeros((img.shape),dtype = np.uint8)
  r,c = mask.shape
  
  start_point = (650, 5)
  end_point = (1650,c)

  color = (255, 255, 255)
  thickness = 900
  mask = cv2.line(mask, start_point, end_point, color, thickness)

  and_img = cv2.bitwise_and(img,mask)
  
  plt.figure(figsize=(10,8))
  
  plt.subplot(1,3,1)
  plt.imshow(img,cmap='gray')
  plt.title('Original Image')
  
  plt.subplot(1,3,2)
  plt.imshow(mask,cmap='gray')
  plt.title('Mask Image')
  
  plt.subplot(1,3,3)
  plt.imshow(and_img,cmap='gray')
  plt.title('AND Image')
  
  plt.savefig('Masking.png')
  plt.show()
  


if __name__ == "__main__":
  main()