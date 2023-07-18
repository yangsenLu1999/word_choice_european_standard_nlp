development_documentation='''
C端-AI学习-背单词-习题的选项
举例：
某考试共有单词A个，某生已掌握单词B个，此时该生需背单词（A-B）个。
背单词功能一组背C个，共搭配C个正确选项和3C个错误选项。
1.正确选项：从（A-B）中随机取C个单词，生成正确选项，
2.错误选项：从（A-B-C）中随机取3C个单词，生成错误选项，
3.从单词释义中生成选项：
（1）当单词只有唯一词性和意思时：取唯一词性和意思
（2）当单词词性和意思有多组时：考虑排序，在前两个词性和意思中随机取一组
'''
import random

def split_list(lst, word_number_in_a_group=5):
    return [lst[i:i + word_number_in_a_group] for i in range(0, len(lst), word_number_in_a_group)]

def generate_options_word_choice_list(word_list:list,meaning_list:list,option_list=['A', 'B', 'C', 'D']):
    # 生成单词选项列表
    word_choice_list = []
    for i, word in enumerate(word_list):
        # 从词义列表中选择三个随机选项
        options = random.sample(meaning_list[:i] + meaning_list[i + 1:], 3)
        # 将正确答案添加到选项列表中
        options.append(meaning_list[i])
        # 随机打乱选项的顺序
        random.shuffle(options)
        # 如果选项中有两个或多个相同的元素，则重新生成选项，直到满足要求
        while len(set(options)) < 4:
            options = random.sample(meaning_list[:i] + meaning_list[i + 1:], 3)
            options.append(meaning_list[i])
            random.shuffle(options)
        # 将单词和选项列表添加到word_choice_list中
        word_choice_list.append([word, options, option_list[options.index(meaning_list[i])]])
        # word_choice_list.append([word, options, option_list.index(option_list[options.index(meaning_list[i])]) ])

    # print(word_choice_list)
    return word_choice_list
# if __name__ == '__main__':
#     # print(development_documentation)
#     # word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
#     # meaning_list = ['苹果', '香蕉', '樱桃', '枣子', '接骨木']
#     # # 选项列表
#     # option_list = ['A', 'B', 'C', 'D']
#     word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
#     meaning_list = ['苹果', '香蕉', '樱桃', '枣子', '接骨木', '无花果', '葡萄', '哈密瓜', '猕猴桃', '柠檬']
#     word_choice_list=generate_options_word_choice_list(word_list,meaning_list)
#     print(word_choice_list)
