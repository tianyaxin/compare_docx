import os, re
root_dir = os.getcwd() + '\\homeworks'
all_dir = os.listdir(root_dir)
with open("file_lists.csv", "a") as file_list:
    file_list.write('学生,检索报告,综述论文,Endnote截图,Endnote压缩库,其他\n')
for stu_dir in all_dir:
    stu = os.listdir("{0}\\{1}".format(root_dir, stu_dir))
    with open("file_lists.csv", "a") as file_list:
        file_list.write(stu_dir)
        report = ''
        review = ''
        pic = ''
        enlx = ''
        other = []
        for i in range(0, len(stu), 1):
            if re.search('cnki|CNKI', stu[i]):
                other.append(stu[i])
            if re.search('检索报告', stu[i]):
                report = stu[i]
            elif re.search('综述论文', stu[i]):
                review = stu[i]
            elif re.search('jpg|jpeg|png|PNG|JPG|JPGE', stu[i]):
                pic = stu[i]
            elif re.search('enlx', stu[i]):
                enlx = stu[i]
            else:
                other.append(stu[i])   
        file_list.write(",{0},{1},{2},{3}".format(report,review,pic,enlx))
        if len(other) == 0:
            pass
        else:
            for j in range(0, len(other),1):
                file_list.write(",{0}".format(other[j]))
        file_list.write("\n")