# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from knowledge_qa_llm.llm.openai import Openai

api = "http://192.168.1.2:1234/v1/chat/completions"
llm = Openai(api_url=api)


prompt = "1+1等于多少"

response = llm(prompt, history=None)
print(response)
