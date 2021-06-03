### 说明：
1. 需要Windows下在Python3环境下运行；
2. 仅支持对扩展名为docx的Word文档进行比较查重；
3. “compare_docx.py”运行前需安装python-docx模块：“pip install python-docx”;

### 流程：
4. 在“get_all_file_list.py”和“compare_docx.py”两个脚本文件相同目录下，新建文件夹“homeworks”，在此文件夹内放置学生的作业文件夹，学生的作业文件夹下是具体的文件，即结构为：
---get_all_file_list.py
---compare_docx.py
---homeworks
    ---学生作业文件夹1
	    ---检索报告.docx
	    ---综述论文.docx
	    ……
    ---学生作业文件夹2
      ---检索报告.docx
      ……
……
5. 运行“get_all_file_list.py”脚本，得到“file.lists.csv”文件，查看学生的文件夹及文件的命名情况，确保学生的检索报告文件名中含有“检索报告”字样，综述论文文件名中含有“综述论文”字样，且两者都是扩展名为docx的word文档，否则需将其打开并另存为docx文档。
6. 运行“compare_docx.py”脚本，得到“检索报告_result.csv”和“检索报告_details.txt”两个文件。其中“检索报告_result.csv”是一个二维表格，小数点保留两位的数值是对应行和列两个学生的检索报告的“相同语句字符数与其中一个学生（总字符数较少的学生）检索报告的总字符数的%比值”；“检索报告_details.txt”是比对的详细结果。
7. 修改“compare_docx.py”脚本的第4行“compare_index = '检索报告'”，将“检索报告”修改成“综述论文”，再次运行这个脚本，将得到“综述论文_result.csv”和“综述论文_details.txt”两个文件。

Enjoy！
