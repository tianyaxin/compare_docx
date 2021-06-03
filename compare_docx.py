import os, re
from docx import Document

compare_index = '检索报告'  # 设定比较的文档文件名的关键词
min_segment = 5  # 设定比较语句的最少字符数

# 获取word文档信息，包括段落数、语句数、字符数、语句内容列表共四个信息。
def get_file_info(wordname):
    d = Document(wordname)
    paras = []
    segs = []
    chars_num = 0
    for para in d.paragraphs:
        if len(para.text) > 0:
            paras.append(para.text)
            chars_num += len(para.text)
            para_split = re.split(',|\.|\?\;|!|，|。|？|！', para.text)
            for s in para_split:
                if len(s) > 2:
                    segs.append(s.replace(' ', ""))
    paras_num = len(paras)
    segs_num = len(segs)
    file_info=[paras_num, segs_num, chars_num, segs]
    return file_info


def compare_docx(stu1, segs1, segs1_count, stu2, segs2, segs2_count):
    same_list = []
    for i in range(len(segs1)):
        if len(segs1[i]) < min_segment:
            continue
        for j in range(len(segs2)):
            if len(segs2[j]) < min_segment:
                continue
            if segs1[i] in segs2[j]:
                same_list.append(segs1[i])
            elif segs2[j] in segs1[i]:
                same_list.append(segs2[j])
    d = {}
    l = d.fromkeys(same_list)
    l = l.keys()
    same_list = list(l)
    same_count = sum([len(s) for s in same_list])
    segs1_ratio = round((same_count / segs1_count) * 100, 2)
    segs2_ratio = round((same_count / segs2_count) * 100, 2)
    detail1 = '_{0}_与_{1}_比对结果'.format(stu1, stu2).center(80, '*')
    detail2 = '\n{0}字符数为{1}个，相同率为{2}%'.format(stu1, segs1_count, segs1_ratio)
    detail3 = '\n{0}字符数为{1}个，相同率为{2}%'.format(stu2, segs2_count, segs2_ratio)
    detail4 = "\n详细结果如下：\n"
    write_details(detail1)
    write_details(detail2)
    write_details(detail3)
    write_details(detail4)
    for i in range(len(same_list)):
        detail5 = '第{0}个重复内容是：{1}\n'.format(i+1, same_list[i])
        write_details(detail5)
    detail6 = "\n"
    write_details(detail6)
    if segs1_ratio > segs2_ratio:
        return segs1_ratio
    else:
        return segs2_ratio

# 输出到比较结果的二维显示csv文件
def write_result(info):
    write_file_name = compare_index + "_result.csv"
    with open(write_file_name, 'a') as compare_result:
        compare_result.write(info)

root_dir = os.getcwd() + '\\homeworks'
all_dir = os.listdir(root_dir)  # 获取学生文件夹列表

# 输出到比较结果的详细信息的txt文件
def write_details(info):
    write_file_name = compare_index + "_details.txt"
    with open (write_file_name, 'a', encoding = 'utf-8') as compare_details:
        compare_details.write(info)

# 获取比较文件列表
compare_file_list = []
for stu_dir in all_dir:
    c_file=''
    stu = os.listdir("{0}\\{1}".format(root_dir, stu_dir))  # 获取学生文件夹内文件列表
    for i in range(len(stu)):
        if re.search(compare_index, stu[i]):
            c_file = "{0}\\{1}\\{2}".format(root_dir, stu_dir, stu[i])
    compare_file_list.append(c_file)


# 比较文件循环
output1 = compare_index + "比对结果(重复率%),段落数,语句数,字节数," + ",".join(all_dir)
write_result(output1)
for i in range(0, len(all_dir) - 1, 1): 
    output2 = ""  
    if compare_file_list[i] == "":
        output2 = "\n" + all_dir[i] + "该生无" + compare_index
    else:
        first = get_file_info(compare_file_list[i])
        output2 = "\n" + all_dir[i] + "," + str(first[0]) + "," + str(first[1]) + "," + str(first[2]) + ','*(i+1)
    write_result(output2)
    if compare_file_list[i] != "":
        for j in range(i+1, len(all_dir), 1):
            output3 = ""
            if compare_file_list[j] == "":
                output3 = ","
            else:
                second = get_file_info(compare_file_list[j])
                compare_data = compare_docx(all_dir[i], first[3], first[2], all_dir[j], second[3],second[2])
                output3 = "," + "{0}".format(compare_data)
            write_result(output3)
last = get_file_info(compare_file_list[-1])
output4 = "\n" + all_dir[-1] + "," + str(last[0]) + "," + str(last[1]) + "," + str(last[2])
write_result(output4)