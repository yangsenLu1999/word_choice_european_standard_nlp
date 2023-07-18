import re

from apple.models import Words_Bank

'''  
将单词的释义进行切分（使用'|'进行切分）和分组,除去网络释义
'''
def split_c_apple_words_bank_pos(word_pos: str):
    splited_pos_list_without_network_meaning = []
    meanings = word_pos.split('|')
    '''
    除去网络释义
    '''
    for meaning in meanings:
        if "网络" in meaning:
            continue
        elif meaning == "":
            continue
        else:
            splited_pos_list_without_network_meaning.append(meaning)
    '''
    对于除去网络意思仍然是至少三个意思，只保留前两个。
    '''
    if len(splited_pos_list_without_network_meaning) >= 3:
        splited_pos_list_without_network_meaning = splited_pos_list_without_network_meaning[:2]
    return splited_pos_list_without_network_meaning


# def split_c_apple_words_bank_inflection(word_inflection: str):
#     try:
#         pattern = r"[:| ]"  # 正则表达式，匹配冒号、下划线和空格
#         return re.split(pattern, str(word_inflection))
#     except Exception as e:
#         print(e)
#         return word_inflection

def split_c_apple_words_bank_inflection(word_inflection: str):
    use_colon_split_results_list=[]
    if  word_inflection:
        # 将字符串按照" | "分割成多个部分，并存储在列表中
        # 存储使用|进行分词的结果的列表
        use_pip_split_results_list = word_inflection.split(" | ")
        #存储使用：进行分词的结果的列表
        use_colon_split_results_list = []
        for result in use_pip_split_results_list:
            use_colon_split_results_list.extend(result.split("："))
        for i in range(len(use_colon_split_results_list)):
            use_colon_split_results_list[i] = use_colon_split_results_list[i].strip()
    return use_colon_split_results_list

'''
读取c_apple_words_bank表中的所有词，将词存入对应地词典中。
'''


def read_c_apple_words_bank(dictionary_of_c_apple_words_bank):
    result = Words_Bank.objects.all()
    try:
        for row in result:
            dictionary_of_c_apple_words_bank[row.word] = {
                "pos": split_c_apple_words_bank_pos(row.pos),
                "inflection": row.inflection
            }
    except Exception as e:
        print(e)

        # 返回字典对象
    return dictionary_of_c_apple_words_bank


'''
{
"word1": ["单词1释义1"...]
"word2": ["单词2释义1"...]
}
'''

dictionary_of_c_apple_words_bank_empty = {}
dictionary_of_c_apple_words_bank = read_c_apple_words_bank(dictionary_of_c_apple_words_bank_empty)

'''
传入一个列表，将列表中所有的单词,在dictionary_of_c_apple_words_bank中进行查询。
'''


def get_word_list_and_meaning_list(sorted_meaningful_words_list: list):
    word_list = []
    meaning_list_s = []
    for word in sorted_meaningful_words_list:
        for i in dictionary_of_c_apple_words_bank:
            if word == i:
                word_list.append(word)
                meaning_list_s.append(dictionary_of_c_apple_words_bank[word]["pos"])
                break
            else:
                continue
    # return "word_not_in_database"
    return word_list, meaning_list_s


def get_meaningful_words_list(word_list):
    meaningful_words_list = []
    for word in word_list:
        for i in dictionary_of_c_apple_words_bank:
            try:
                if word == i:
                    meaningful_words_list.append(word)
                    break
                elif word in split_c_apple_words_bank_inflection(dictionary_of_c_apple_words_bank[i]["inflection"]):
                    meaningful_words_list.append(i)
                    break
                else:
                    continue
            except Exception as e:
                print(e)
    meaningful_words_set = set(meaningful_words_list)
    meaningful_words_list.clear()
    meaningful_words_list = list(meaningful_words_set)
    return meaningful_words_list
