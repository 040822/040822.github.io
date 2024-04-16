import os
from PIL import Image

def compress_images(directory, quality):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否为图片
        if filename.endswith('.png'):
            # 获取文件大小，单位是字节
            file_size = os.path.getsize(os.path.join(directory, filename))
            # 如果文件大小大于500KB，进行压缩
            if file_size > 500 * 1024:
                # 打开图片
                img = Image.open(os.path.join(directory, filename))
                # 如果图片是RGBA模式，将其转换为RGB模式
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                # 压缩图片
                img.save(os.path.join(directory, filename), 'JPEG', quality=quality)
    print('图片压缩完成')

# 使用示例
path = 'D:\wx\office\\ahaic\\040822.github.io\\040822\source\_posts\番剧测评'
quality = 80
compress_images(path, quality)