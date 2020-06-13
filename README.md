此项目用于完成epub中全部HTML文件读取、标签去除、文本合并、标点符号去除、单词词频统计等功能。

用法：

* 将epub文档后缀名改为zip在解压，找到其中的HTML文件
* 复制文件的路径储存到file_loc变量中
* 复制HTML文件名，注意去掉后缀.html和之前的标号，剩余部分存到变量file_name中
* 将最后一个HTML文件的标号存到file_num变量中
* reverse填True代表降序，反之亦然
* 调用WordFrequencyStatistics.py中的类
* 创建一个对象，参数为上面几个变量
* 即可得到epub文档中内容的TXT版本以及统计结果（包括单词总数、不重复单词数和词频分布）
