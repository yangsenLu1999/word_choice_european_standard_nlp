import random
# import c_apple_db, split_sentence, to_c_aiexercise_options
from dao import c_apple_db, split_sentence, to_c_aiexercise_options
'''
功能：后端提交长字符串，返回字符串中四种实义词的ABCD四个选项，四者之一为正确选项，其余为错误。
单个单词的返回格式为：["单词本身":str,["A选项":str,"B选项":str,"C选项":str,"D选项":str],正确选项的下标:int]:list
整体返回格式为：  [
                ["单词1",["A选项","B选项","C选项","D选项"],正确选项的下标],...["单词n",["A选项","B选项","C选项","D选项"],正确选项的下标]
                ["单词1",["A选项","B选项","C选项","D选项"],正确选项的下标],...["单词n",["A选项","B选项","C选项","D选项"],正确选项的下标]
               ]
'''

'''
将单个单词的返回从["单词本身":str,["A选项":str,"B选项":str,"C选项":str,"D选项":str],正确选项的下标:int]:list转为
{
  "title": "单词",
  "options": [
     {"type": "词性","desc": "释义","is_right": True/False},
     {"type": "词性","desc": "释义","is_right": True/False"},
     {"type": "词性","desc": "释义","is_right": True/False},
     {"type": "词性","desc": "释义","is_right":True/False},
  ]
}
'''
def transfer_single_word_choice_list_to_json(single_word_choice_list:list):
    single_word_choice_json={}
    single_word_choice_json["title"]=single_word_choice_list[0]
    single_word_choice_json["options"]=[]
    Right_Choice_Index=-1
    if single_word_choice_list[2]=='A':
        right_Choice_Index=0
    elif single_word_choice_list[2]=='B':
        right_Choice_Index=1
    elif single_word_choice_list[2]=='C':
        right_Choice_Index=2
    elif single_word_choice_list[2]=='D':
        right_Choice_Index=3
    else:
        print("error生成选项的标号不是ABCD任何一个")
    for choice_index in range(4):
        choice_dict={}
        type_and_desc=single_word_choice_list[1][choice_index].split(".")
        choice_dict["type"]=type_and_desc[0]
        choice_dict["desc"]=type_and_desc[1]
        if choice_index==right_Choice_Index:
            choice_dict["is_right"]=True
        else:
            choice_dict["is_right"]=False
        single_word_choice_json["options"].append(choice_dict)
    return single_word_choice_json

# rear_end_wordtext:后端提交的长字符串；
def get_rear_end_wordtext_to_return_word_choice_list(rear_end_wordtext: str):
    '''
    (1)切分后端传输的字符串rear_end_text
    '''
    splited_text_words_list = split_sentence.wordstokenizer(rear_end_wordtext)
    '''
    (2)在切分后获取的单词字符列表中找到所有的动词、名词、形容词、副词这四种有实际意义的词（即除取介词、代词、关联词等）      get_meaningful_words.py模块
    具体为：
    若单词为名词单数或者名词复数都保留名词单数；
    若单词为单性/多性动词原型或者单性/多性动词三单、~现在分词、~过去式、~过去分词都保留单性/多性动词的原型；
    若单词为形容词原型、形容词不带more的比较级比如happier、happiest，统一保留形容词原型如happy。（若为加more构成的比较级，加most构成的最高级，则会认为是more/most+形容词原型，也会保留形容词原型，不影响。）
    若单词为副词原型，同上。
    特殊情况：
    若该单词有多种解释，比如starting，既可以解释为单性动词start的现在分词形式，又可以解释为名词原型。两种解释均符合保留实际意义单词的要求。若依前者，应存储start；若依后者，应存储starting。
    当前选择两种情况均保留，即存储
    '''

    meaningful_words_list = c_apple_db.get_meaningful_words_list(splited_text_words_list)
    meaningful_words_list_set = set(meaningful_words_list)
    meaningful_words_list = list(meaningful_words_list_set)
    sorted_meaningful_words_list = sorted(meaningful_words_list)
    '''
    (3)查询数据库c_apple下的words_bank表下word对应的pos(单词释义，据产品沟通结果，暂不保留网络释义)  c_apple_db.py模块
    '''
    word_list, meaning_list_s = c_apple_db.get_word_list_and_meaning_list(sorted_meaningful_words_list)
    '''
    (4)#随机分组，默认是5个单词为一组，
    随机生成单词的ABCD四个选项，单个单词的返回格式为：["单词本身":str,["A选项":str,"B选项":str,"C选项":str,"D选项":str],正确选项的下标:int]:list
    '''
    result = []
    meaning_list = []
    for lst in meaning_list_s:
        # if len(lst)==1:
        #     meaning_list.append(lst[0])
        # else:
        random_element = random.choice(lst)
        meaning_list.append(random_element)
            # first_meaning=lst[0]
            # meaning_list.append(first_meaning)
    word_choice_list = to_c_aiexercise_options.generate_options_word_choice_list(word_list, meaning_list)
    result.extend(word_choice_list)
    # print(meaning_list)

    word_choice_json_list = []
    for single_word_choice_list in result:
        # print(single_word_choice_list)
        single_word_choice_json = transfer_single_word_choice_list_to_json(single_word_choice_list)
        word_choice_json_list.append(single_word_choice_json)
    return word_choice_json_list

