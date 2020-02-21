
def yiq(rgb):
    matrix = (0.299,0.587,0.114, 0.596,-0.274,-0.322, 0.211, -0.523, 0.312)
    y = matrix[0] * rgb[0] + matrix[1] * rgb[1] + matrix[2] * rgb[2]
    i = matrix[3] * rgb[0] + matrix[4] * rgb[1] + matrix[5] * rgb[2]
    q = matrix[6] * rgb[0] + matrix[7] * rgb[1] + matrix[8] * rgb[2]

    return (round(y,4),round(i,4), round(q,4))


