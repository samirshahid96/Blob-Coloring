import numpy as np
import matplotlib
from matplotlib import pyplot as plt


class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        R, C = image.shape
        # print(image[34][45])
        # print(R, C)
        hist = [0]*256
        for i in range(R):
            for j in range(C):
                hist[image[i][j]] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        ismax1 = 0
        ismax2 = 0
        for t1 in range(10, round(len(hist)/2)):
            ismax1 += hist[t1]
            '''if hist[t1] > hist[ismax1]:
                ismax1 = t1'''
        for t2 in range(round(len(hist)/2), len(hist) - 10):
            ismax2 += hist[t2]
            '''  if hist[t2] > hist[ismax2]:
                ismax2 = t2'''
        peak1 = ismax1/len(hist)
        peak2 = ismax2/len(hist)
        threshold = round((peak2 + peak1)/2)
        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        bin_img = image.copy()
        r, c = image.shape
        # print(r, c)
        threshold = 20
        "self.find_optimal_threshold(self.compute_histogram(image))"
        for i in range(r):
            for j in range(c):
                if bin_img[i][j] > threshold:
                    bin_img[i][j] = 0
                elif bin_img[i][j] <= threshold:
                    bin_img[i][j] = 255

        return bin_img


