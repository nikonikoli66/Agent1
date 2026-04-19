import time
import streamlit as st
from agent.react_agent import ReactAgent

# 页面配置
st.set_page_config(
    page_title="智扫通 · 智能客服",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式 - 轻奢粉红主题
st.markdown("""
<style>
    /* 全局样式 */
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
    }
    
    /* 主容器样式 */
    .main > div {
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* 标题样式 */
    h1 {
        font-family: 'Georgia', 'Times New Roman', serif;
        color: #880e4f !important;
        font-weight: 300 !important;
        letter-spacing: 4px !important;
        text-align: center;
        padding: 20px 0 10px 0 !important;
        margin-bottom: 0 !important;
        text-shadow: 2px 2px 4px rgba(136, 14, 79, 0.1);
    }
    
    /* 标题装饰 */
    h1::before, h1::after {
        content: " ✦ ";
        color: #d81b60;
        font-size: 0.7em;
        opacity: 0.7;
    }
    
    /* 分割线样式 */
    hr {
        margin: 10px auto 30px auto !important;
        width: 100px !important;
        border: none !important;
        height: 2px !important;
        background: linear-gradient(90deg, transparent, #f06292, #d81b60, #f06292, transparent) !important;
    }
    
    /* 聊天消息容器 */
    div[data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.75) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-radius: 20px !important;
        padding: 15px 20px !important;
        margin: 10px 0 !important;
        box-shadow: 0 4px 15px rgba(216, 27, 96, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
    }
    
    /* 用户消息特殊样式 */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.85), rgba(252, 228, 236, 0.85)) !important;
        border-right: 4px solid #d81b60 !important;
    }
    
    /* 助手消息特殊样式 */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.8), rgba(248, 187, 208, 0.8)) !important;
        border-left: 4px solid #f48fb1 !important;
    }
    
    /* 头像样式 */
    [data-testid="stChatMessageAvatarUser"] {
        background: linear-gradient(135deg, #d81b60, #f06292) !important;
        border-radius: 50% !important;
        padding: 8px !important;
        box-shadow: 0 2px 8px rgba(216, 27, 96, 0.3) !important;
    }
    
    [data-testid="stChatMessageAvatarAssistant"] {
        background: linear-gradient(135deg, #ad1457, #e91e63) !important;
        border-radius: 50% !important;
        padding: 8px !important;
        box-shadow: 0 2px 8px rgba(216, 27, 96, 0.3) !important;
    }
    
    /* 输入框样式 */
    div[data-testid="stChatInput"] {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-radius: 30px !important;
        border: 1px solid rgba(216, 27, 96, 0.2) !important;
        padding: 5px 10px !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 15px rgba(216, 27, 96, 0.15) !important;
    }
    
    div[data-testid="stChatInput"] textarea {
        color: #4a0024 !important;
        font-size: 16px !important;
    }
    
    div[data-testid="stChatInput"] textarea::placeholder {
        color: #ad1457 !important;
        opacity: 0.6 !important;
    }
    
    div[data-testid="stChatInput"] button {
        background: linear-gradient(135deg, #d81b60, #f06292) !important;
        border-radius: 50% !important;
        color: white !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-testid="stChatInput"] button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 4px 12px rgba(216, 27, 96, 0.4) !important;
    }
    
    /* 加载动画样式 */
    .stSpinner {
        color: #d81b60 !important;
    }
    
    .stSpinner > div {
        border-top-color: #d81b60 !important;
    }
    
    /* 文本颜色 */
    p, span, div {
        color: #4a0024 !important;
    }
    
    /* 用户消息文本 */
    [data-testid="stChatMessageContent"] {
        color: #4a0024 !important;
        line-height: 1.6 !important;
        font-size: 15px !important;
    }
    
    /* 底部水印 */
    .footer {
        text-align: center;
        margin-top: 30px;
        padding: 15px;
        color: #ad1457 !important;
        opacity: 0.6;
        font-size: 12px;
        letter-spacing: 2px;
    }
    
    /* 滚动条美化 */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(252, 228, 236, 0.3);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #f48fb1, #f06292);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #f06292, #d81b60);
    }
    
    /* 欢迎提示 */
    .welcome-hint {
        text-align: center;
        padding: 40px 20px;
        color: #ad1457 !important;
        font-size: 14px;
        letter-spacing: 1px;
        opacity: 0.7;
    }
</style>
""", unsafe_allow_html=True)

# 标题区域
st.markdown('<h1>智扫通 · 智能客服</h1>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

# 初始化 session state
if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()

if "message" not in st.session_state:
    st.session_state["message"] = []

# 消息展示区域
chat_container = st.container()

with chat_container:
    # 如果没有消息，显示欢迎提示
    if len(st.session_state["message"]) == 0:
        st.markdown("""
        <div class="welcome-hint">
            ✦ 欢迎使用智扫通智能客服 ✦<br/>
            <span style="font-size: 12px; opacity: 0.6;">随时为您提供贴心服务</span>
        </div>
        """, unsafe_allow_html=True)

    # 显示历史消息
    for message in st.session_state["message"]:
        with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🌸"):
            st.write(message["content"])

# 用户输入区域
prompt = st.chat_input(placeholder="✨ 输入您的问题，智扫通为您解答...")

if prompt:
    # 显示用户消息
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    # 生成助手回复
    response_messages = []
    with st.chat_message("assistant", avatar="🌸"):
        with st.spinner("🌸 正在为您思考..."):
            res_stream = st.session_state["agent"].execute_stream(prompt)

            def capture(generator, cache_list):
                full_response = ""
                for chunk in generator:
                    cache_list.append(chunk)
                    full_response += chunk
                    for char in chunk:
                        time.sleep(0.01)
                        yield char
                cache_list.append(full_response)

            # 流式输出
            full_response = st.write_stream(capture(res_stream, response_messages))

    # 保存完整响应到 session state
    if response_messages:
        st.session_state["message"].append({
            "role": "assistant",
            "content": response_messages[-1] if len(response_messages) > 1 else full_response
        })

    st.rerun()

# 底部装饰
st.markdown("""
<div class="footer">
    ✦ 智扫通 · 智慧清洁 贴心服务 ✦
</div>
""", unsafe_allow_html=True)