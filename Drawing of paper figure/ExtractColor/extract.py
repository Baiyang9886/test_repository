from haishoku.haishoku import Haishoku
image = './test.png'
haishoku = Haishoku.loadHaishoku(image)

# palette函数输出配色色号
print(haishoku.palette)

haishoku.showPalette(image)