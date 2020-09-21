import cv2
import numpy as np

class cell_counting:

    def get_key(self, region, val):
        for key, value in region.items():
            for pix in value:
                if val == pix:
                    return key
        return "key doesn't exist"

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window assigns region names
        takes a input:
        image: binary image
        return: a list of regions"""

        k = 1
        regions = dict()
        row, col = image.shape
        for i in range(row):
            for j in range(col):
                if image[i][j] == 255:
                    if i == 0 and j == 0:
                        regions.setdefault(k, []).append((i, j))
                        k = k + 1
                    elif i == 0:
                        if image[i][j - 1] == 0:
                            regions.setdefault(k, []).append((i, j))
                            k = k + 1
                        else:
                            regions.setdefault((self.get_key(regions, (i, j - 1))), []).append((i, j))
                    elif j == 0:  # left pixel care
                        if image[i - 1][j] == 0:
                            regions.setdefault(k, []).append((i, j))
                            k = k + 1
                        else:
                            regions.setdefault((self.get_key(regions, (i - 1, j))), []).append((i, j))
                    elif image[i - 1][j] == 0 and image[i][j - 1] == 0:
                        regions.setdefault(k, []).append((i, j))
                        k = k + 1
                    elif image[i - 1][j] == 255 and image[i][j - 1] == 255:
                        if self.get_key(regions, (i-1, j)) != self.get_key(regions, (i, j-1)):
                            transfer = regions.pop(self.get_key(regions, (i, j-1)), [])
                            for swap in transfer:
                                regions.setdefault(self.get_key(regions, (i-1, j))).append(swap)
                            regions.setdefault(self.get_key(regions, (i - 1, j))).append((i, j))
                        else:
                            regions.setdefault(self.get_key(regions, (i - 1, j))).append((i, j))
                    elif image[i][j-1] == 255:
                        regions.setdefault(self.get_key(regions, (i, j-1))).append((i, j))
                    elif image[i-1][j] == 255:
                        regions.setdefault(self.get_key(regions, (i-1, j))).append((i, j))
                else:
                    ''' # NO NEED TO DO ANYTHING '''

        # dict.get(key) will give us just the value
        # dict.keys() will give us just keys

        # print(len(regions.keys()))
        return regions
    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        stats = dict()
        k = 0
        i_sum = 0
        j_sum = 0
        for key in region:
            k = k + 1
            i_sum = 0
            j_sum = 0
            stats.setdefault(k, [])
            for pixels in region[key]:
                    i_sum += pixels[0]
                    j_sum += pixels[1]
            center_i = round((i_sum)/len(region[key]))
            center_j = round((j_sum)/len(region[key]))
            stats[k].append((center_i, center_j))
            stats[k].append(len(region.get(key)))
        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        print(stats)

        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        # cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        newimage = np.array(image)
        #newimage = image
        for keys in stats:
           # print('hello')
            stuff = stats[keys]
            center = stuff[0]
            # center looks like (#,#)
            area = stuff[1]
            # print(center,area)
            # area looks like #

            text1 = '*'

            text2 = '.' + str(keys) + ',' + str(area)
            cv2.putText(newimage, text2, (center[1], center[0]), cv2.FONT_HERSHEY_COMPLEX, .25, 127)
        return newimage

