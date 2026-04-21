# Hermes BT Panel 插件

让 Hermes Agent 能管理你的 BT Panel 服务器。

## 这是什么

Hermes Agent 是一个 AI 助手，可以执行命令、读写文件等。  
这个插件让 Hermes 能通过 BT Panel API 管理服务器（网站、SSL、数据库等）。

## 快速开始

### 1. 安装

```bash
cd /root/workspaces/hermes-bt-panel
pip install requests
```

### 2. 配置 API

编辑 `src/btpanel/__init__.py` 里的连接信息：
- `API_URL`: BT Panel 地址，如 `http://192.168.69.102:6888`
- `API_KEY`: 从面板「设置 → API 接口」获取

### 3. 测试

```bash
python3 test.py status   # 系统状态
python3 test.py sites  # 网站列表
python3 test.py ssl xbot.my  # SSL状态
```

## Hermes 工具是什么

Hermes 有「工具」（tools）—— 让 AI 能做的事情。比如：

- `terminal()` - 执行��令
- `read_file()` - 读文件
- `patch()` - 修改文件

BT Panel 插件就是把「调用 BT Panel API」做成一个工具，这样 Hermes 就能用自然语言帮你管服务器，比如：

- "帮我看看服务器状态"
- "给我列出所有网站"
- "xbot.my 的 SSL 证书什么时候到期"

## 项目结构

```
hermes-bt-panel/
├── src/btpanel/          # 核心库
│   ├── client.py         # API 客户端
│   └── api/            # API 函数
│       ├── system.py    # 系统状态
│       ├── sites.py     # 网站管理
│       ├── ssl.py      # SSL证书
│       ├── docker.py    # Docker容器
│       └── cron.py     # 计划任务
├── test.py              # CLI测试
└── openspec/            # 项目规范
```

## 可用的 API 函数

| 模块 | 函数 | 说明 |
|------|------|------|
| system | get_system_total, get_disk_info, get_network | 系统状态 |
| sites | get_websites, get_site, add_site, delete_site, start_site, stop_site | 网站管理 |
| ssl | get_ssl, set_ssl, http_to_https | SSL证书 |
| database | get_databases, set_database_password | 数据库 |
| docker | get_containers, start_container, stop_container | Docker容器 |
| cron | get_crons, add_cron, delete_cron | 计划任务 |
| files | get_file, save_file | 文件操作 |

## 下一步

需要把这个注册成 Hermes 工具，这样 Hermes 才能调用它。  
这一步需要改 Hermes 的配置文件，暂时先跳过。

先用 `test.py` 测试核心功能是否正常。