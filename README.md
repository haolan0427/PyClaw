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

```shell
python main.py
```

效果如下图所示：

![image-20260321164710236](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260321164710236.png)

用户的prompts硬编码在`.py`文件中是不恰当。实现持续对话。

![image-20260321171437548](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260321171437548.png)

增加记忆

![image-20260321172755492](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260321172755492.png)

执行`shell`命令，

<span style="color: red;">缺陷：只能一次性完成某个任务，很难做到分步执行。</span>

<span style="color: green;">在当前目录下新建一个名为 note 的目录，然后进入这个新建的目录并创建一个名为 tmp.txt 文件，输入的内容是：HelloPyClaw，接着从note目录返回到上一级目录，新建一个 note.txt 文件，内容是：今天学了些啥呀？✅</span>

<span style="color: red;">请分步为我完成下面的任务，1.在当前目录下新建一个名为 note 的目录，2.然后进入这个新建的目录并创建一个名为 tmp.txt 文件，输入的内容是：HelloPyClaw，3.接着从note目录返回到上一级目录，新建一个 note.txt 文件，内容是：今天学了些啥呀？❌</span>

![image-20260321185037346](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260321185037346.png)



