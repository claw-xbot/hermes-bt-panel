---
name: hermes-bt-panel
description: Hermes BT Panel 插件 - 让 AI Agent 管理宝塔面板。通过 BT Panel API 管理服务器（网站、SSL、数据库、Docker、计划任务等）。
tags: [btpanel, baota, server, management, ssl, docker, website]
version: 0.1.0
author: claw-xbot
license: MIT
---

# Hermes BT Panel 插件

通过 BT Panel API 管理服务器。

## 安装

```bash
# 克隆仓库
cd /root/workspaces
git clone https://github.com/claw-xbot/hermes-bt-panel.git

# 测试连接
cd hermes-bt-panel
python3 test.py status
```

## 配置

编辑 `src/btpanel/__init__.py` 或在代码中传入：

```python
from btpanel import BTPanelClient

client = BTPanelClient(
    base_url="http://192.168.69.102:6888",
    api_key="你的API密钥"
)
```

API 密钥获取：面板 → 设置 → API 接口

## 使用示例

```python
from btpanel import BTPanelClient
from btpanel.api import get_network, get_websites, get_ssl

client = BTPanelClient("http://IP:6888", "API密钥")

# 系统状态
stats = get_network(client)

# 网站列表
sites = get_websites(client)

# SSL 状态
ssl = get_ssl(client, "example.com")
```

## 可用 API 模块

| 模块 | 函数数 | 说明 |
|------|--------|------|
| system | 3 | 系统状态、磁盘、网络 |
| sites | 14 | 网站增删改查 |
| ssl | 5 | SSL 证书管理 |
| database | 4 | 数据库管理 |
| backup | 8 | 备份和 FTP |
| docker | 10 | Docker 容器 |
| cron | 4 | 计划任务 |
| files | 3 | 文件读写 |
| system_settings | 6 | 面板设置 |

## CLI 测试

```bash
python3 test.py status          # 系统状态
python3 test.py sites         # 网站列表
python3 test.py ssl example.com # SSL 状态
```

## 作为 Hermes 工具使用

在 Hermes 对话中直接调用：

```
帮我看看服务器状态
列出所有网站
xbot.my 的 SSL 证书什么时候到期
```

需要先配置 `src/btpanel/__init__.py` 里的连接信息。