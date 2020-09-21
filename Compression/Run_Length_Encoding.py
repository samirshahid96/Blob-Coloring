import numpy as np

class rle:

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        r, c = binary_image.shape
        list = []
        if binary_image[0][0] == 255:
            flag = 0
            list.append(1)
        else:
            flag = 255
            list.append(0)
        count = 0
        for i in range(r):
            for j in range(c):
                if binary_image[i][j] != flag:
                    count = count + 1
                else:
                    list.append(count)
                    count = 0
                    if flag == 255:
                        flag = 0
                    else:
                        flag = 255
        return list  # np.zeros(100) #replace zeros with rle_code

    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        # height = row
        # width = column
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        image = np.zeros((height, width), np.uint8)
        color = 0
        if rle_code[0] == 1:
            color = 255
        else:
            color = 0
        index = 1
        for i in range(height):
            for j in range(width):
                if index == len(rle_code):
                    return image
                else:
                    if rle_code[index] != 0:
                        image[i][j] = color
                        rle_code[index] = rle_code[index] - 1
                    else:
                        if color == 255:
                            color = 0
                            index = index + 1
                        else:
                            color = 255
                            index = index + 1
        return  image #replace zeros with image reconstructed from rle_Code





        




