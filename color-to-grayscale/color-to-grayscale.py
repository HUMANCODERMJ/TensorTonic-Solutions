def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    ans = []
    for row in image:
        temp = []
        for pixel in row:
            Y=0.299*pixel[0]+0.587*pixel[1]+0.114*pixel[2]
            temp.append(Y)
        ans.append(temp)

    return ans
    
# [
# [[255, 0, 0], [0, 255, 0]], 
# [[0, 0, 255], [255, 255, 255]]
# ]