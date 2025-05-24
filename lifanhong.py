import numpy as np
from PIL import Image

# 读取图片
img = Image.open('npy/lfh_origin.png')

# 转换为 512x512
img_resized = img.resize((512, 512), Image.LANCZOS)

# 保存结果
img_resized.save('npy/lfh_512.png')

# 如需转换为 numpy 数组
img_array = np.array(img_resized)

# 创建 512x512 的白色图像（255）
mask = np.ones((512, 512), dtype=np.uint8) * 255

# 计算黑色矩形区域的坐标
left = 317
bottom = 120
width = 115
height = 225
# 注意：PIL和numpy的坐标原点在左上角，y轴向下
# 所以左下角(320,120)转换为左上角(320, 512-120-225)
top = 512 - bottom - height
mask[top:top+height, left:left+width] = 0

# 保存mask为图片
mask_img = Image.fromarray(mask)
mask_img.save('npy/mask.png')

