from __future__ import annotations

import subprocess
from pathlib import Path
from threading import Lock


class AgentService:
    def __init__(self, client, model: str, prompt_paths: list[str]):
        system_prompt = "".join(
            Path(path).read_text(encoding="utf-8") for path in prompt_paths
        )
        self.client = client
        self.model = model
        self.messages = [{"role": "system", "content": system_prompt}]
        self.chat_history: list[dict[str, str]] = []
        self._lock = Lock()

    def get_history(self) -> list[dict[str, str]]:
        with self._lock:
            return [message.copy() for message in self.chat_history]

    def submit(self, user_input: str) -> list[dict[str, str]]:
        with self._lock:
            self.chat_history.append({"role": "user", "content": user_input})
            self.messages.append({"role": "user", "content": user_input})

            while True:
                reply = self._call_model()
                self.chat_history.append({"role": "assistant", "content": reply})
                self.messages.append({"role": "assistant", "content": reply})

                if reply.startswith("完成："):
                    return [message.copy() for message in self.chat_history]

                command = self._extract_command(reply)
                command_output = self._run_command(command)

                self.chat_history.append(
                    {
                        "role": "command",
                        "content": command_output,
                        "command": command,
                    }
                )
                self.messages.append(
                    {
                        "role": "user",
                        "content": f"命令 `{command}` 的执行结果：\n{command_output}",
                    }
                )

    def _call_model(self) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=False,
        )
        return response.choices[0].message.content or ""

    @staticmethod
    def _extract_command(reply: str) -> str:
        if "命令：" not in reply:
            raise ValueError("模型回复中没有找到“命令：”，无法继续执行。")
        return reply.split("命令：", 1)[1].strip()

    @staticmethod
    def _run_command(command: str) -> str:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )
        output = f"{result.stdout}{result.stderr}".strip()
        if not output:
            output = "命令执行完成，但没有输出。"
        if result.returncode != 0:
            output = f"{output}\n\n退出码：{result.returncode}"
        return output
