import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

messages = [{"role": "system", "content": """
你的任务是完成用户的任务，只能选择下面其中一种格式进行回复：
1. 如果是需要执行命令的任务，则输出'命令：XXX'，其中XXX为命令本身
2. 如果是不需要执行命令的任务，则输出'完成：XXX'，XXX为你的总结信息
"""}]

while True:
    user_input = input("User：\n") # 用户输入
    messages.append({"role": "user", "content": user_input}) # 持续记忆
    print("\n-------- Agent Loop Start --------\n")
    while True:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages = messages,
            stream = False
        )
        reply = response.choices[0].message.content # 模型回复
        messages.append({"role": "assistant", "content": reply})

        print(f"【AI】{reply}")

        if reply.startswith("完成："): # 如果任务完成则结束任务，并输出结果
            print("\n-------- Agent Loop End --------\n")
            break
        
        command = reply.strip().split("命令：")[1].strip() # 提取命令
        command_result = os.popen(command).read() # 执行shell命令并获取结果

        content = f"【Agent】已执行 {command}"
        print(content)
        messages.append({"role": "assistant", "content": content})


   
