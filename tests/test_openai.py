# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from knowledge_qa_llm.llm.openai import openai

api = "http://192.168.1.2:1234/v1/chat/completions"
llm = openai(api_url=api)


prompt = "杭州有哪些景点？"

response = llm(prompt, history=None)
print(response)
