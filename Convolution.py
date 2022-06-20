import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():

    img = cv2.imread('dog.jpg', 0)
    r, c = img.shape
    grayscale2 = np.zeros((r, c), dtype=np.uint8)
    grayscale3 = np.zeros((r, c), dtype=np.uint8)

    kernel1 = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, -1]
    ], dtype=np.float32)

    kernel2 = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ], dtype=np.float32)

    grayscale2 = cv2.filter2D(img, -1, kernel1)
    grayscale3 = cv2.filter2D(img, -1, kernel2)

    plt.figure(figsize=(10, 8))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original grayscale Image')

    plt.subplot(1, 3, 2)
    plt.imshow(grayscale2, cmap='gray')
    plt.title('Sobel Filtered Image')

    plt.subplot(1, 3, 3)
    plt.imshow(grayscale3, cmap='gray')
    plt.title('Laplacian Filtered Image')

    plt.savefig('ConvFig.png')
    plt.show()


if __name__ == "__main__":
    main()
