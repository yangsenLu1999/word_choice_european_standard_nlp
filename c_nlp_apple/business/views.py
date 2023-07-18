# Create your views here.
from django.http import JsonResponse

# Create your views here.
from django.views import View

from dao.return_european_standard import return_the_european_standard_level_of_words_in_list
from dao.return_word_choice_list import get_rear_end_wordtext_to_return_word_choice_list
from dao.split_sentence import wordstokenizer


class BacK_Word(View):

    def post(self, request):
        essay = self.request.POST.get('essay')
        _json_ = {}
        try:
            t = get_rear_end_wordtext_to_return_word_choice_list(essay)
            _json_['code'] = 200
            _json_['msg'] = '获取成功'
            _json_['data'] = t

        except Exception as e:
            print(e)
            _json_['code'] = -1
            _json_['msg'] = '获取失败'
        return JsonResponse(_json_, safe=False)


class Get_Level(View):

    def post(self, request):
        essay = self.request.POST.get('essay')
        _json_ = {}
        try:
            essay = wordstokenizer(essay)
            t = return_the_european_standard_level_of_words_in_list(essay)
            _json_['code'] = 200
            _json_['msg'] = '获取成功'
            _json_['data'] = t

        except Exception as e:
            print(e)
            _json_['code'] = -1
            _json_['msg'] = '获取失败'
        return JsonResponse(_json_, safe=False)
