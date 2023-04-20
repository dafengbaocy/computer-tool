import os
import shutil


def movefile(src_folder, tar_folder):
    files = os.listdir(src_folder)
    for file in files:
        # 将每个文件的完整路径拼接出来
        src_path = src_folder + '\\' + file

        if os.path.isfile(src_path):
            # 移动之后的文件路径
            # 将文件民按点分割 取最后一位 即是目标的路径

            tar_path = tar_folder + '\\' + file.split('.')[-1]
            if not os.path.exists(tar_path):
                os.mkdir(tar_path)
            # 移动文件
            shutil.move(src_path, tar_path)
    os.rmdir(src_folder)


src_folder = input("输入待分类目录：")
tar_folder = input("输入分类后目录：")
files = os.listdir(src_folder)
for file in files:
    # 将每个文件的完整路径拼接出来
    src_path = src_folder + '\\' + file

    if os.path.isfile(src_path):
        # 移动之后的文件路径
        # 将文件民按点分割 取最后一位 即是目标的路径

        tar_path = tar_folder + '\\' + file.split('.')[-1]
        if not os.path.exists(tar_path):
            os.mkdir(tar_path)
        # 移动文件
        shutil.move(src_path, tar_path)

if os.path.exists(src_folder):  # 源文件夹存在才执行
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
    wendang = ["pdf", "docx", "doc"]
    wendang_path = tar_folder + "\\" + "文档"
    tupian = ["jpg"]
    tupian_path = tar_folder + "\\" + "图片"
    yasuobao = ["zip", "rar"]
    yasuobao_path = tar_folder + "\\" + "压缩包"
    anzhuangbao = ["exe"]
    anzhuangbao_path = tar_folder + "\\" + "安装包"
    a = [wendang,tupian,yasuobao,anzhuangbao]
    b = [wendang_path,tupian_path,yasuobao_path,anzhuangbao_path]
    for dir in os.listdir(tar_folder):
        for aa in a:
            c = a.index(aa)
            d = b[c]
            if dir in aa:
                if not os.path.exists(d):
                    shutil.move(tar_folder + "\\" + dir, d + "\\" + dir)
                else:
                    movefile(tar_folder + "\\" + dir, d)