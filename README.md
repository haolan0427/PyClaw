# PyClaw

### 环境依赖：

```shell
pip install -r requirements.txt
```

选用 AI 模型：deepseek-chat

在 python 中使用 DeepSeek 的 SDK，参考文档：[DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)

### 实现版本[v0.0.1](https://github.com/haolan0427/PyClaw/releases/tag/v0.0.1)

就是与模型的一问一答，你问什么，ta 只基于已有的知识回答什么。

效果如下图所示：

![image-20260321164710236](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260321164710236.png)

### 实现版本[v0.0.2](https://github.com/haolan0427/PyClaw/releases/tag/v0.0.2)

用户的 prompts 硬编码在`.py`文件中是不恰当。实现持续对话。

效果如下图所示：

![image-20260321171437548](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260321171437548.png)

### 实现版本[v0.0.3](https://github.com/haolan0427/PyClaw/releases/tag/v0.0.3)

增加记忆。

效果如下图所示：

![image-20260321172755492](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260321172755492.png)

### 实现版本[v0.1.0](https://github.com/haolan0427/PyClaw/releases/tag/v0.1.0)

执行`shell`命令。

<span style="color: red;">缺陷：只能一次性完成某个任务，很难做到分步执行。</span>

<span style="color: green;">在当前目录下新建一个名为 note 的目录，然后进入这个新建的目录并创建一个名为 tmp.txt 文件，输入的内容是：HelloPyClaw，接着从note目录返回到上一级目录，新建一个 note.txt 文件，内容是：今天学了些啥呀？✅</span>

<span style="color: red;">请分步为我完成下面的任务，1.在当前目录下新建一个名为 note 的目录，2.然后进入这个新建的目录并创建一个名为 tmp.txt 文件，输入的内容是：HelloPyClaw，3.接着从note目录返回到上一级目录，新建一个 note.txt 文件，内容是：今天学了些啥呀？❌</span>

效果如下图所示：

![image-20260321185037346](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260321185037346.png)

### 实现版本[v0.1.1](https://github.com/haolan0427/PyClaw/releases/tag/v0.1.1)

将系统最初的提示词封装进 `Agent.md` 文件中，做为系统提示词。

<span style="color: red;">下载视频，经过了很多次的尝试。要使用到 `yt-dlp` 包（我是提前下载好的）。但模型可能会使用 `youtube-dl`、和 `you-get` 这两个包，就会达不到预期的效果。感觉和 AI 模型的能力有关。</span>

效果如下图所示：

![image-20260323011901737](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260323011901737.png)

### 实现版本[v0.1.2](https://github.com/haolan0427/PyClaw/releases/tag/v0.1.2)

增加SKILL，下载视频使用 `yt-dlp` 工具，浏览新闻使用 `curl` 工具。

效果如下图所示：

![image-20260323070341546](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260323070341546.png)

### 最新版本v0.2.0

通过 vibe coding 实现在本地浏览器与 AI-Agent 对话。

效果如下图所示：

![image-20260323085244354](https://raw.githubusercontent.com/haolan0427/tuchuang/master/image-20260323085244354.png)

也开始实现在远程浏览器与 AI-Agent 对话。

效果如下图所示：

<img src="https://raw.githubusercontent.com/haolan0427/tuchuang/master/e9fb9e8da813a651c44e4b2fed0aebc1.jpg" alt="e9fb9e8da813a651c44e4b2fed0aebc1" style="zoom:45%;" />
