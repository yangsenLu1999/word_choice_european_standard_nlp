from apple.models import European_Standard_Level
from business.models import Save_Word
from dao import c_apple_db

'''
输入：输入一篇essay，进行tokenizer之后的单词、符号列表
输出：[{"word":"单词1","level":"单词1的欧标"}，{"word":"单词2","level":"单词2的欧标"}，{"word":"单词3","level":"单词3的欧标"}，...，{{"word":"单词n","level":"单词n的欧标"}]
找不到的单词存入business_save_word
'''
def return_the_european_standard_level_of_words_in_list(tokenizered_list: list):
    '''
    (1）tokenizered_list是tokenizer之后的单词、符号列表
    '''
    '''
    (2)
    在切分后获取的单词字符列表中找到所有的动词、名词、形容词、副词这四种有实际意义的词（即除取介词、代词、关联词等）      get_meaningful_words.py模块
    具体为：
    若单词为名词单数或者名词复数都保留名词单数；
    若单词为单性 / 多性动词原型或者单性 / 多性动词三单、~现在分词、~过去式、~过去分词都保留单性 / 多性动词的原型；
    若单词为形容词原型、形容词不带more的比较级比如happier、happiest，统一保留形容词原型如happy。（若为加more构成的比较级，加most构成的最高级，则会认为是more / most + 形容词原型，也会保留形容词原型，不影响。）
    若单词为副词原型，同上。
    特殊情况：
    若该单词有多种解释，比如starting，既可以解释为单性动词start的现在分词形式，又可以解释为名词原型。两种解释均符合保留实际意义单词的要求。若依前者，应存储start；若依后者，应存储starting。
    当前选择两种情况均保留，即存储
    '''
    # 将列表中的英文单词全部转成小写
    splited_text_words_list = [word.lower() if word.isalpha() else word for word in tokenizered_list]
    print("splited_text_words_list:",splited_text_words_list)
    #查找）splited_text_words_list中的实义词，将所有的实义存入  meaningful_words_list
    meaningful_words_list = c_apple_db.get_meaningful_words_list(splited_text_words_list)
    #对查到的实义词进行去重
    meaningful_words_list_set = set(meaningful_words_list)
    meaningful_words_list = list(meaningful_words_list_set)
    sorted_meaningful_words_list = sorted(meaningful_words_list)
    print("sorted_meaningful_words_list:", sorted_meaningful_words_list)
    '''
    输入：['单词1'，'单词2'，'单词3'，...,'单词n']
    输出：[{"word":"单词1","level":"单词1的欧标"}，{"word":"单词2","level":"单词2的欧标"}，{"word":"单词3","level":"单词3的欧标"}，...，{{"word":"单词n","level":"单词n的欧标"}]
    '''
    # 将返回的单词和欧标存在列表中返回[{"word1": "单词", "level": "欧标等级"}, {"word2": "单词", "level": "欧标等级"}, ...{"wordn": "单词", "level": "欧标等级"}]
    word_european_standard_level_dict_list = []
    # 逐个遍历列表中的单词，在数据库c-apple下的apple_european_standard_level表中查找单词的欧标
    # European_Standard_Level_objects=European_Standard_Level.objects.all()
    for word_input in  sorted_meaningful_words_list:
        # 如果能在表中查到当前单词的欧标，则将{"word":"单词","level":"单词的欧标"}存入list
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

