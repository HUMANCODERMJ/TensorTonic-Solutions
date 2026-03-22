def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    intensity_array = [0] * 256

    for pixel in image:
        for intensity in pixel:
            intensity_array[intensity] += 1

    return intensity_array