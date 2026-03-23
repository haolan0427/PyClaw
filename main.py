import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from agent_service import AgentService
from web_ui import run_web_ui

load_dotenv()


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
    )
    agent_service = AgentService(
        client=client,
        model="deepseek-chat",
        prompt_paths=[
            str(base_dir / "Agent.md"),
            str(base_dir / "SKILL.md"),
        ],
    )
    host = os.environ.get("PYCLAW_HOST", "0.0.0.0")
    port = int(os.environ.get("PYCLAW_PORT", "4270"))
    run_web_ui(agent_service=agent_service, host=host, port=port)


if __name__ == "__main__":
    main()
