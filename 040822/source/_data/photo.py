import os
from urllib.parse import urljoin
from PIL import Image

def make_md():
    # 配置信息
    image_directory = "D:\wx\office\\ahaic\\040822.github.io\\040822\source\images\pixiv"  # 图片所在目录路径
    base_url = "D:\wx\office\\ahaic\\040822.github.io\\040822\source\images\pixiv\\"  # 图片的基础URL
    output_md_file = "D:\wx\office\\ahaic\\040822.github.io\\040822\source\_data\photos.yml"  # 输出的Markdown文件名

    # 获取所有图片文件名
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')  # 图片扩展名
    image_filenames = [f for f in os.listdir(image_directory) if f.endswith(image_extensions)]

    # 创建Markdown文件
    with open(output_md_file, 'w', encoding='utf-8') as md_file:
        for filename in image_filenames:
            # 构建图片的URL
            url = base_url+filename
            # 构建Markdown格式的条目
            md_entry = f"- url: {url}\n  name: {filename}\n\n"
            # 写入文件
            md_file.write(md_entry)

    print(f"Markdown file '{output_md_file}' has been created with {len(image_filenames)} entries.")



def compress_images(directory, quality, output_directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否为图片
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.webp') or filename.endswith('.gif'):
            # 获取文件大小，单位是字节
            file_size = os.path.getsize(os.path.join(directory, filename))
            # 如果文件大小大于1MB，进行压缩
            if file_size > 1024 * 1024:
                # 打开图片
                img = Image.open(os.path.join(directory, filename))
                # 如果图片是RGBA模式，将其转换为RGB模式
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                # 压缩图片
                img.save(os.path.join(output_directory, filename), 'JPEG', quality=quality)
    print('图片压缩完成')

if __name__ == '__main__':
    path = 'D:\wx\图片\逼乎\pixiv'
    output_directory = 'D:\wx\office\\ahaic\\040822.github.io\\040822\source\images\pixiv'
    quality = 80
    compress_images(path, quality, output_directory)
    make_md()