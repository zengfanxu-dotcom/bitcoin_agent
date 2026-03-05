import os
from autogen_ext.models.openai import OpenAIChatCompletionClient

def create_openai_model_client():
    """创建并配置 OpenAI 模型客户端"""
    return OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL_ID", "deepseek"),
        api_key=os.getenv("sk-11730309a7ce488bb5ca0a8200097f96"),
        base_url=os.getenv("LLM_BASE_URL", "https://api.deepseek.com")
    )
