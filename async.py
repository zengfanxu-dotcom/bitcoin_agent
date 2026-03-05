import asyncio

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console
from RoundRobinGroupChat import create_team_chat


async def run_software_development_team():
    model_client = OpenAIChatCompletionClient(
        model="deepseek-chat",
        api_key="sk-a938a596e3d148ca9d0a63fd79de501e",
        base_url="https://api.deepseek.com/v1",
        model_info={
            "family": "deepseek",
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "max_tokens": 4096,
        },
    )
    team_chat = create_team_chat(model_client)

    task = """我们需要开发一个比特币价格显示应用，具体要求如下：
            核心功能：
            - 实时显示比特币当前价格（USD）
            - 显示24小时价格变化趋势（涨跌幅和涨跌额）
            - 提供价格刷新功能

            技术要求：
            - 使用 Streamlit 框架创建 Web 应用
            - 界面简洁美观，用户友好
            - 添加适当的错误处理和加载状态

            请团队协作完成这个任务，从需求分析到最终实现。"""

    result = await Console(team_chat.run_stream(task=task))
    return result


if __name__ == "__main__":
    result = asyncio.run(run_software_development_team())
