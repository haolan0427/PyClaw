import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
agentmd = open("./Agent.md", "r").read()
skillmd = open("./SKILL.md", "r").read()
messages = [{"role": "system", "content": agentmd + skillmd}]

while True:
    user_input = input("User：\n") # 用户输入
    messages.append({"role": "user", "content": user_input}) # 持续记忆
    print("\n-------- Loop Start --------\n")
    while True:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages = messages,
            stream = False
        )
        reply = response.choices[0].message.content # 模型回复
        messages.append({"role": "assistant", "content": reply})

        print(f"AI{reply}")

        if reply.startswith("完成："): # 如果任务完成则结束任务，并输出结果
            print("\n-------- Loop End --------\n")
            break
        
        command = reply.strip().split("命令：")[1].strip() # 提取命令
        command_result = os.popen(command).read() # 执行shell命令并获取结果

        content = f"AI已执行 {command}"
        print(command_result)
        messages.append({"role": "assistant", "content": command_result})


   
