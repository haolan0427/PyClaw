# 模拟OpenClaw

### 1. 在python中使用DeepSeek的SDK
参考文档：[DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
安装OpenAI SDK

```shell
pip install openai
pip install python-dotenv
```

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "下午好呀！请问你叫啥名字呀？"},
    ],
    stream=False
)

print(response.choices[0].message.content)
```

将`.env-example`文件重命名为`.env`，填入你的API

在`.env`文件中写入你的

在终端执行

```shell
python main.py
```

