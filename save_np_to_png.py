import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 创建一个示例numpy数组 (假设是一个RGB图像)
# 创建一个100x100的随机RGB图像
img_np = np.random.rand(100, 100, 3)  # 值范围在0-1之间

# 方法1：使用PIL保存
def save_with_pil(img_np, filename):
    # 确保值在0-255范围内
    img_np = (img_np * 255).astype(np.uint8)
    # 转换为PIL图像
    img_pil = Image.fromarray(img_np)
    # 保存为PNG
    img_pil.save(filename)
    print(f"使用PIL保存到: {filename}")

# 方法2：使用matplotlib保存
def save_with_matplotlib(img_np, filename):
    plt.imsave(filename, img_np)
    print(f"使用matplotlib保存到: {filename}")

# 使用两种方法保存图像
save_with_pil(img_np, "output_pil.png")
save_with_matplotlib(img_np, "output_matplotlib.png")

# 如果你有一个灰度图像，可以这样处理：
gray_img = np.random.rand(100, 100)  # 值范围在0-1之间
# 保存灰度图像
plt.imsave("output_gray.png", gray_img, cmap='gray')
print("灰度图像已保存到: output_gray.png") 