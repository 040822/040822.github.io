import requests
import os
import json

# 配置信息
repo_url = "https://api.github.com/repos/040822/picx-images-hosting/git/trees/master?recursive=1"  # GitHub仓库的API URL
base_url = "https://github.com/040822/picx-images-hosting/raw/master/"  # 图片的基础URL
output_md_file = "source\_data\photos_git.yml"  # 输出的Markdown文件名

# 发送GET请求
response = requests.get(repo_url)

# 解析JSON
data = json.loads(response.text)

# 获取所有图片文件名
image_filenames = [item['path'] for item in data['tree'] if item['path'].endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))]

# 创建Markdown文件
with open(output_md_file, 'w', encoding='utf-8') as md_file:
    for filename in image_filenames:
        # 构建图片的URL
        url = base_url + filename
        filename = filename.split("/")[-1]
        filename = filename.split("p0")[0]+"p0"
        # 构建Markdown格式的条目
        md_entry = f"- url: {url}\n  name: {filename}\n\n"
        # 写入文件
        md_file.write(md_entry)

print(f"Markdown file '{output_md_file}' has been created with {len(image_filenames)} entries.")