# 🤖 Agent1 - 智能AI客服系统

## 📋 项目概述

**Agent1** 是一个基于 Streamlit 框架开发的智能AI客服系统，专为智能扫地机器人产品设计的客户服务平台。系统采用 RAG（检索增强生成）架构，结合 Claude AI 大模型，为用户提供智能、流畅的客服对话体验。

## 🏗️ 系统架构

### 核心组件
- **Streamlit前端**: 现代化Web界面，响应式设计
- **ReactAgent**: 基于ReAct范式的智能体推理引擎
- **RAG服务**: 检索增强生成，提供精准答案
- **向量数据库**: 知识库语义搜索
- **配置管理**: 灵活的系统配置
- **工具系统**: 可扩展的功能工具集

## 📁 项目结构

```
C:\Users\Administrator\IdeaProjects\Agent1/
├── app.py                          # 主应用入口
├── agent/                          # AI智能体模块
│   ├── react_agent.py             # ReAct智能体实现
│   └── tools/                     # 工具集
│       ├── agent_tools.py         # 智能体工具
│       └── middleware.py          # 中间件
├── config/                         # 配置文件
├── model/                         # AI模型管理
│   └── factory.py                 # 模型工厂
├── rag/                           # RAG服务
│   ├── rag_service.py             # RAG服务实现
│   └── vector_store.py            # 向量存储
├── utils/                         # 工具类
│   ├── config_handler.py          # 配置处理
│   ├── file_handler.py            # 文件处理
│   ├── logger_handler.py          # 日志管理
│   ├── path_tool.py               # 路径工具
│   └── prompt_loader.py           # 提示词加载
├── data/                          # 数据目录
├── logs/                          # 日志目录
├── prompts/                       # 提示词模板
├── rag/                           # RAG知识库
└── utils/                         # 通用工具
```

## ✨ 核心功能

### 🤖 智能对话
- **自然语言理解**: 精准识别用户意图
- **上下文感知**: 保持对话连贯性
- **多轮对话**: 支持复杂交互流程
- **实时响应**: 流式输出体验

### 📚 知识库管理
- **RAG检索**: 基于语义的知识检索
- **向量搜索**: 高效相似度匹配
- **动态更新**: 支持知识库热更新
- **多源数据**: 支持多种文档格式

### 🛠️ 工具系统
- **可扩展架构**: 插件式工具管理
- **函数调用**: 支持外部API调用
- **中间件**: 请求/响应处理管道
- **错误处理**: 健壮的异常管理

### 🎨 用户界面
- **现代化设计**: 粉色渐变主题
- **响应式布局**: 适配各种设备
- **实时聊天**: 流畅的对话体验
- **加载动画**: 优雅的状态提示

## 🚀 快速开始

### 环境要求
- Python 3.8+
- pip 包管理器

### 安装步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd Agent1
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **配置环境**
```bash
# 复制配置文件
cp config/config.yaml.example config/config.yaml

# 编辑配置文件，设置API密钥等
vim config/config.yaml
```

4. **启动应用**
```bash
streamlit run app.py
```

5. **访问应用**
打开浏览器访问 `http://localhost:8501`

## ⚙️ 配置说明

### 主要配置文件
- `config/config.yaml`: 主配置文件
- `prompts/`: 提示词模板目录
- `data/`: 知识库数据目录

### 配置项说明
```yaml
# 示例配置
streamlit:
  page_title: "智扫通 · 智能客服"
  page_icon: "🌸"
  layout: "wide"

model:
  provider: "anthropic"
  model_name: "claude-3-sonnet-20240229"
  temperature: 0.7

rag:
  vector_store: "faiss"
  embedding_model: "text-embedding-3-small"
  top_k: 5
```

## 🔧 开发指南

### 添加新工具
在 `agent/tools/agent_tools.py` 中定义新工具：

```python
@tool
def my_new_tool(param1: str, param2: int) -> str:
    """工具描述"""
    # 工具实现
    return result
```

### 自定义提示词
在 `prompts/` 目录下创建新的提示词模板：

```
system: |
  你是一个专业的AI客服助手...

user: |
  {{ user_input }}
```

### 扩展RAG知识库
将文档放入 `data/` 目录，系统会自动处理：

```bash
# 支持格式：txt, pdf, docx, md等
cp my_document.pdf data/
```

## 📊 性能优化

### 缓存策略
- 对话历史缓存
- 知识库向量缓存
- 模型响应缓存

### 监控指标
- 响应时间
- 吞吐量
- 错误率
- 用户满意度

## 🔒 安全考虑

- API密钥管理
- 用户数据保护
- 访问控制
- 输入验证

## 📝 日志管理

日志文件位于 `logs/` 目录：
- `app.log`: 应用运行日志
- `error.log`: 错误日志
- `access.log`: 访问日志

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交代码
4. 创建 Pull Request

## 📄 许可证

MIT License

## 🔗 相关资源

- [Streamlit文档](https://docs.streamlit.io)
- [Claude AI](https://www.anthropic.com)
- [RAG技术](https://arxiv.org/abs/2005.11401)

## 📞 联系方式

- 项目地址: [GitHub Repository]
- 问题反馈: [Issues]
- 邮箱: [Contact Email]

---

**💡 提示**: 本系统采用模块化设计，便于扩展和定制，可根据具体业务需求进行调整。

*Last updated: 2026-04-21*