from apple.models import European_Standard_Level
from business.models import Save_Word

'''
输入：['单词1'，'单词2'，'单词3'，...,'单词n']
输出：[{"word":"单词1","level":"单词1的欧标"}，{"word":"单词2","level":"单词2的欧标"}，{"word":"单词3","level":"单词3的欧标"}，...，{{"word":"单词n","level":"单词n的欧标"}]
'''


def return_the_european_standard_level_of_words_in_list(words_list: list):
    # 将返回的单词和欧标存在列表中返回[{"word1": "单词", "level": "欧标等级"}, {"word2": "单词", "level": "欧标等级"}, ...{"wordn": "单词", "level": "欧标等级"}]
    word_european_standard_level_dict_list = []
    # 逐个遍历列表中的单词，在数据库c-apple下的apple_european_standard_level表中查找单词的欧标
    # European_Standard_Level_objects=European_Standard_Level.objects.all()
    words_set=set(words_list)
    words_list=list(words_set)
    for word_input in words_list:
        # 如果能在表中查到当前单词的欧标，则将{"word":"单词","level":"单词的欧标"}存入list
        word_input=word_input.lower()
        word_found = European_Standard_Level.objects.filter(word=word_input.strip())
        if word_found.exists():
            word_european_standard_level_dict = {}
            word_european_standard_level_dict["word"] = word_input.strip()
            word_european_standard_level_dict["level"] = word_found.first().level
            if word_european_standard_level_dict not in word_european_standard_level_dict_list:
                word_european_standard_level_dict_list.append(word_european_standard_level_dict)
        else:
            Save_Word.objects.create(word=word_input.strip())
            print("找不到单词{}".format(word_input.strip()))
            # 继续顺位查询另一个单词
            continue
    # 返回[{"word":"单词1","level":"单词1的欧标"}，{"word":"单词2","level":"单词2的欧标"}，{"word":"单词3","level":"单词3的欧标"}，...，{{"word":"单词n","level":"单词n的欧标"}]
    return word_european_standard_level_dict_list
