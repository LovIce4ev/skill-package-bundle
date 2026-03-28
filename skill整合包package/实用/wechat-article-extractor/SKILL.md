---
name: wechat-article-extractor
description: 从微信公众号链接中自动提取标题、正文及所有配图，并保存为带有排版的独立 HTML 文件。适用于用户要求抓取/提取给定微信文章链接、或者“提取公众号文章”、“把这个链接的内容扒下来”等场景。
---

# 微信公众号文章提取器 (WeChat Article Extractor)

这个 Skill 用于从给定的微信公众号文章链接提取主要的正文内容（包括隐藏在 JS 中的图片和视频元信息），并将其生成一个能够独立离线浏览的 `.html` 文件。

## 前置准备：
1. 请先检查环境中是否已经存在能运行此脚本的 Python 虚拟环境，如果没有，则需要在用户工作区根目录下或某适当目录创建一个 `venv`，并安装依赖。
2. 脚本和依赖列表都存放在本 Skill 目录的 `scripts` 文件夹中。你可以在 `scripts/requirements.txt` 中找到它需要的按如下命令安装依赖：
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r [本Skill目录的绝对路径]/scripts/requirements.txt
   ```

## 使用指南 (Workflow)

当用户给出微信公众号链接并请你提取内容时，请遵循以下流程：

### 第一步：创建或激活环境
进入到一个合适的用户工作目录（例如用户的项目根目录或临时工作目录），然后激活上述前置准备中提到的虚拟环境（或直接利用现有环境）。

### 第二步：运行提取命令
找到本 Skill 安装位置自带的 Python 脚本：`[本Skill目录的绝对路径]/scripts/extract.py`。
使用上面激活好的 Python 环境去执行它，并将系统提供的微信文章 URL 作为命令行参数传入：

```bash
# 请将 <wechat_url> 替换为用户真正给出的公众号链接
python3 [本Skill目录的绝对路径]/scripts/extract.py "<wechat_url>"
```

### 第三步：验证与展示
成功运行后，脚本会在当前的**工作目录（你执行命令的地方）**生成一个叫做 `output.html` 的文件。
1. 请用终端命令（通常是直接输出或者 grep 下）查验文件是否成功生成。
2. 调用 macOS 的默认程序帮用户直接在浏览器中打开这个网页（使用命令 `open output.html`）。

## 注意事项：
* 有些微信文章采用“图片消息”或“视频消息”而非传统的“图文消息”模板，本脚本内部已经做了 Fallback 兼容，能够直接去 `window.picture_page_info_list` 提取无损非重复图片，这也是为什么即使看似空的 `js_content` 也能成功提取的原因。
* 脚本生成的 HTML 将自带响应式排版样式，手机端及 PC 浏览器均可适配阅读。
