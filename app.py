import streamlit as st
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console
from RoundRobinGroupChat import create_team_chat


def get_model_client():
    """获取模型客户端，支持本地和云端部署"""
    if hasattr(st, 'secrets') and "LLM_API_KEY" in st.secrets:
        api_key = st.secrets.LLM_API_KEY
        model = st.secrets.LLM_MODEL_ID if "LLM_MODEL_ID" in st.secrets else "deepseek-chat"
        base_url = st.secrets.LLM_BASE_URL if "LLM_BASE_URL" in st.secrets else "https://api.deepseek.com/v1"
    else:
        api_key = os.getenv("LLM_API_KEY", "")
        model = os.getenv("LLM_MODEL_ID", "deepseek-chat")
        base_url = os.getenv("LLM_BASE_URL", "https://api.deepseek.com/v1")
    
    if not api_key:
        st.error("请配置 LLM_API_KEY 环境变量")
        return None
    
    return OpenAIChatCompletionClient(
        model=model,
        api_key=api_key,
        base_url=base_url,
        model_info={
            "family": "deepseek",
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "max_tokens": 4096,
        },
    )

st.set_page_config(page_title="AI软件开发团队", page_icon="🤖", layout="wide")

st.title("🤖 AI 软件开发团队")

st.markdown("""
这是一个由 AI Agent 组成的软件开发团队，包括：
- **产品经理** - 需求分析和项目规划
- **工程师** - 代码实现
- **代码审查员** - 代码质量审查
- **用户代理** - 验证和测试
""")

if "task" not in st.session_state:
    st.session_state.task = ""
if "output" not in st.session_state:
    st.session_state.output = ""
if "running" not in st.session_state:
    st.session_state.running = False

task_input = st.text_area(
    "输入开发任务描述：",
    value=st.session_state.task,
    height=150,
    placeholder="例如：开发一个比特币价格显示应用..."
)

col1, col2 = st.columns([1, 4])
with col1:
    run_button = st.button("🚀 开始执行", disabled=st.session_state.running)
with col2:
    clear_button = st.button("🗑️ 清除输出")

if clear_button:
    st.session_state.output = ""
    st.session_state.task = ""
    st.rerun()

if run_button and task_input:
    st.session_state.running = True
    st.session_state.task = task_input

    async def run_team():
        model_client = get_model_client()
        if model_client is None:
            return
        
        team_chat = create_team_chat(model_client)
        
        output_lines = []
        
        async for message in team_chat.run_stream(task=task_input):
            if hasattr(message, 'content'):
                line = f"**{message.source}**: {message.content}\n"
            else:
                line = str(message) + "\n"
            output_lines.append(line)
            st.session_state.output = "\n".join(output_lines)
        
        return st.session_state.output

    try:
        result = asyncio.run(run_team())
        st.session_state.output = result
    except Exception as e:
        st.error(f"运行出错: {str(e)}")
    finally:
        st.session_state.running = False
        st.rerun()

if st.session_state.output:
    st.divider()
    st.subheader("📋 执行结果")
    st.markdown(st.session_state.output)

if st.session_state.running:
    st.info("⏳ 正在执行任务，请稍候...")
