import numpy as np
from skimage.feature import local_binary_pattern
def caluLBP(images, eps = 1e-7):
    [z, y, x] = np.shape(images)
    result = []
    for i in range(z):
        curImage = images[i, :, :]
        r = 3
        points = 8*3
        lbp = local_binary_pattern(curImage, points, r, 'uniform')
        n_bins = 26
        (hists, _) = np.histogram(lbp, n_bins)
        histogram = hists.astype("float")
        histogram /= (histogram.sum() + eps)
        result.append(histogram)
    return result
