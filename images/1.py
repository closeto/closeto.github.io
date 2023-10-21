import os

# 要批量修改文件名的目录路径
directory = "./"

OldFile=[]
NewFile=[]

# 遍历目录下的所有文件
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        # 这里可以编写你的文件名修改逻辑
        # 例如，将文件名中的"old"替换为"new"
        new_filename = filename.replace(" ", "")
        
        # 构建新文件的完整路径
        new_filepath = os.path.join(directory, new_filename)
        
        # 使用os.rename()来重命名文件
        os.rename(os.path.join(directory, filename), new_filepath)
        print(f"{filename} <——————> {new_filename}")