# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import json
from typing import List, Optional

import requests


class Openai:
    def __init__(self, api_url: str = None):
        self.api_url = api_url

    def __call__(self, prompt: str, history: Optional[List] = None, **kwargs):
        if not history:
            history = []

        data = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        if kwargs:
            temperature = kwargs.get("temperature", 0.1)
            top_p = kwargs.get("top_p", 0.7)
            max_length = kwargs.get("max_length", 4096)

            data.update(
                {"temperature": temperature, "top_p": top_p, "max_length": max_length}
            )
        # 设置请求头
        headers = {
            "Content-Type": "application/json"
        }
        print(json.dumps(data))
        req = requests.post(self.api_url, data=json.dumps(data),headers=headers, timeout=60)
        try:
            rdata = req.json()
            if rdata["choices"] !='':
                return rdata["choices"][0]["message"]["content"]
            return "网络出错"
        except Exception as e:
            return f"网络出错:{e}"


if __name__ == "__main__":
    prompt = "你是谁？"
    history = []
    t = Openai()

    res = t(prompt, history)
    print(res)
