import os
import shutil

def copy_files(src_dir, dest_dir, excluded_extensions):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if not any(file.endswith(ext) for ext in excluded_extensions):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, os.path.relpath(src_file, src_dir))
                dest_file_dir = os.path.dirname(dest_file)
                
                if not os.path.exists(dest_file_dir):
                    os.makedirs(dest_file_dir)
                
                shutil.copy2(src_file, dest_file) #直接覆盖同名文件
                print(f"Copied {src_file} to {dest_file}")

# Example usage
src_directory = r'H:\BaiduSyncdisk\040822_obsidian\post' # 源文件夹
dest_directory = r'H:\BaiduSyncdisk\040822.github.io\040822\source\_posts' # 目标文件夹
excluded_extensions = ['.md.edtz', '.edtz']  # Add the extensions you want to exclude

copy_files(src_directory, dest_directory, excluded_extensions)