class WordFrequencyStatistics:
    def __init__(self, file_loc, file_name, file_num, file_output, reverse=True):
        self.file_loc = file_loc
        self.file_name = file_name
        self.file_num = file_num
        self.file_output = file_output
        self.reverse = reverse
        self.file_names = self.get_file_names()
        self.contents = self.gather_contents()
        self.contents_nonSymbol = self.replace_symbol()
        self.word_frequency = self.statistic_word_frequency()

    def statistic_word_frequency(self):
        """
        统计词频
        :return: 最终统计字典
        """
        words = self.contents.split()
        word_frequency = {}
        for word in words:
            if word in word_frequency.keys():
                word_frequency[word] += 1
            else:
                word_frequency.setdefault(word, 1)

        word_frequency = sorted(word_frequency.items(), key=lambda word_frequency: word_frequency[1], reverse=
        self.reverse)
        with open(self.file_output + '_word', 'w', encoding='utf-8') as op:
            op.write(str(len(words)) + '\n')
            op.write(str(len(word_frequency)) + '\n')
            for word in word_frequency:
                op.write(str(word) + '\n')

        return word_frequency

    def gather_contents(self):
        """
        将所有分开的文本合并
        :return: 合并后的文本
        """
        contents = ''
        for file_name in self.file_names:
            contents += self.remove_taps(file_name)

        with open(self.file_output + '_doc', 'w', encoding='utf-8') as file:
            file.write(contents)

        return contents

    def get_file_names(self):
        """
        获得存有所有HTML文件的名字的列表（epub文件）
        :return: 装有所有文件名称的列表
        """
        indices = list(range(self.file_num + 1))
        for index in indices:
            index = int(index)
            if index < 10:
                indices[index] = '00' + str(index)
            elif index < 100:
                indices[index] = '0' + str(index)
            else:
                indices[index] = str(index)

        file_base = self.file_loc + self.file_name
        file_names = []
        for index in indices:
            file_name = file_base + index + ".html"
            file_names.append(file_name)

        return file_names

    def remove_taps(self, file_name):
        """
        去掉HTML文件中所有标签
        :param file_name: 要去除标签的文件（确保路径可以匹配）
        :return: 去掉标签后的文本
        """
        import re
        # open the file
        with open(file_name, 'r', encoding='UTF-8') as file:
            contents = file.read()

        # remove the taps
        taps_regex = re.compile('<.*?>')
        taps = taps_regex.findall(contents)  # find all the contents matched by the regex
        for tap in taps:
            contents = contents.replace(tap, '')  # replace all the taps with none

        return contents

    def replace_symbol(self):
        symbols = [',', '.', '!', '?', '(', ')', '-', '=', '+', '_', '&', '^', '%', '$', '#', '@', '<', '>', '/', r'\\',
                   '`', '~', '|', '{', '}', '[', ']', "'", '"']
        contents_non_symbol = self.contents
        for symbol in symbols:
            contents = contents_non_symbol.replace(symbol, '')
        return contents_non_symbol
