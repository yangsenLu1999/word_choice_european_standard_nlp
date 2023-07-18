import re

# 分词，不包含空格
def wordstokenizer(text):
    pattern = r'''(?x)    # set flag to allow verbose regexps
         (?:[A-Z]\.)+[A-Z]?        # abbreviations, e.g. U.S.A.
        | (?:[apm]\.)+
        | [http://|ftp://|https://|www]?[^\u4e00-\u9fa5\s]*?\.[com|net|cn|gov|edu|org][^\u4e00-\u9fa5\s,]* #网址
        | Mr\.
        | Miss\.
        | Mrs\.
        | Ms\.
        | Dr\.
        | Prof\.
        | Madam\.
        | 's\s
        | 't\s
        | 'm\s
        | 're\s
        | 'll\s
        | 've\s
        | 'd\s        
        | o'clock
        | [A-Za-z]+ 

        | \$?\d+\(\.\d+\)?%?  # currency and percentages, e.g. $12.40, 82%
        | [0-9]+\:[0-9]+
        | [0-9]+\.?[0-9]+
        | [0-9,]+
        | \.\.\.            # ellipsis
        | [+\*\/?!？！；:/\][.,，;\"'()\-_`，。：、；‘’“”（）]  # these are separate tokens
       '''

    token = re.findall(pattern, text)
    w_list = []
    for i in range(len(token)):
        if i > 0 and token[i] == "'t ":
            w_list[len(w_list) - 1] += "'t"
        # elif i>0 and token[i]=="'s" and (token[i-1] == 'Let' or token[i-1] == 'let'):
        #     w_list[len(w_list) - 1] += "'s"
        elif token[i] in  ["'s ", "'t ","'m ","'re ","'ll ","'ve ","'d "]:
            w_list.append(token[i].strip())
        else:
            w_list.append(token[i])
    return w_list

def get_words(row:list):
    splited_row=wordstokenizer(row)
    splited_row.sort()
    words_set=set(splited_row)
    words_list=list(words_set)
    return words_list
