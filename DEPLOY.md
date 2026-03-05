# AI 软件开发团队 - 部署指南

## 本地运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
# 复制 .env.example 为 .env 并填入你的 API Key
cp .env.example .env

# 3. 运行
streamlit run app.py
```

---

## 部署到 Streamlit Cloud（推荐，最简单）

### 步骤：

1. **准备代码**
   - 确保 `app.py` 和 `requirements.txt` 已创建
   - 创建 `.env.example`（不包含真实 API Key）：
   ```
   LLM_API_KEY=
   LLM_MODEL_ID=deepseek-chat
   LLM_BASE_URL=https://api.deepseek.com/v1
   ```

2. **上传到 GitHub**
   - 创建一个新仓库
   - 上传所有文件（除了 `.env` 和 `__pycache__`）
   - `.gitignore` 已经配置好了会自动忽略

3. **部署**
   - 访问 https://share.streamlit.io
   - 用 GitHub 登录
   - 点击 "New app"
   - 选择你的仓库和分支
   - Main file 填 `app.py`
   - 点击 "Deploy"

4. **配置 API Key**
   - 部署完成后，点击右上角 "Settings"
   - 找到 "Secrets" 
   - 添加：
     ```
     LLM_API_KEY = 你的API密钥
     LLM_MODEL_ID = deepseek-chat
     LLM_BASE_URL = https://api.deepseek.com/v1
     ```
   - 点击 "Save"
   - 点击 "Redeploy"

---

## 部署到 Railway

### 步骤：

1. **上传到 GitHub**
   - 同上

2. **创建 Railway 项目**
   - 访问 https://railway.app
   - 用 GitHub 登录
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择你的仓库

3. **配置环境变量**
   - 点击 "Variables" 标签
   - 添加：
     ```
     LLM_API_KEY = 你的API密钥
     LLM_MODEL_ID = deepseek-chat
     LLM_BASE_URL = https://api.deepseek.com/v1
     PORT = 8501
     ```

4. **部署**
   - Railway 会自动检测并部署
   - 等待完成后，点击生成的链接访问

---

## 部署到 Heroku

### 步骤：

1. **安装 Heroku CLI**
   - 下载安装：https://devcenter.heroku.com/articles/heroku-cli

2. **登录**
   ```bash
   heroku login
   ```

3. **创建应用**
   ```bash
   heroku create 你的应用名称
   ```

4. **配置环境变量**
   ```bash
   heroku config:set LLM_API_KEY=你的API密钥
   heroku config:set LLM_MODEL_ID=deepseek-chat
   heroku config:set LLM_BASE_URL=https://api.deepseek.com/v1
   ```

5. **部署**
   ```bash
   heroku git:remote -a 你的应用名称
   git push heroku main
   ```

---

## 常见问题

### Q: 部署后无法运行？
A: 检查环境变量是否配置正确，特别是 LLM_API_KEY

### Q: 显示 "Model info required" 错误？
A: 确保 model_info 配置正确，或者切换到 OpenAI 模型

### Q: 如何修改端口？
A: Streamlit Cloud 和 Railway 会自动分配端口，不需要手动设置
