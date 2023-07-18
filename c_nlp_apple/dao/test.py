# from dao.split_sentence import wordstokenizer
# if __name__ == '__main__':
#     my_str="<p>The Ebro Delta, in Spain, famous as a battleground during the Spanish Civil War, is now the setting for a different contest, one that is pitting rice farmers against two enemies: the rice-eating giant apple snail, and rising sea levels. What happens here will have a bearing on the future of European rice production and the overall health of southern European wetlands.</p>"
#     print(wordstokenizer(my_str))
#     splited_text_words_list = [word.lower() if word.isalpha() else word for word in wordstokenizer(my_str)]
#     print(splited_text_words_list)

def split_nlp_dev_words_bank_inflection(word_inflection: str):
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

if __name__ == '__main__':
     my_str='过去分词：ensilaged | 现在分词：ensilaging | 第三人称单数：ensilages | '
     result=split_nlp_dev_words_bank_inflection(my_str)
     print(result)