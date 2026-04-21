"""
Hermes BT Panel 插件

通过 BT Panel API 管理服务器。

使用示例:
    from btpanel import BTPanelClient
    from btpanel.api import get_system_total, get_websites
    
    client = BTPanelClient("http://192.168.1.100:8888", "API密钥")
    
    # 系统状态
    stats = get_system_total(client)
    
    # 网站列表
    sites = get_websites(client)
"""

from .client import BTPanelClient, BTPanelError

# Import all API functions
from . import api

# For backwards compatibility, expose main functions
from .api import (
    # System
    get_system_total as system_total,
    get_disk_info as disk_info,
    get_network as network,
    # Sites
    get_websites as websites,
    get_site as site_info,
    add_site as create_site,
    delete_site as remove_site,
    start_site as enable_site,
    stop_site as disable_site,
    # SSL
    get_ssl as ssl_info,
    set_ssl as apply_ssl,
    http_to_https as force_https,
    close_https as disable_force_https,
    # Database
    get_databases as databases,
    set_database_password as change_db_password,
    # Backup
    get_backups as backups,
    create_backup as create_site_backup,
    delete_backup as remove_backup,
    create_database_backup as create_db_backup,
    delete_database_backup as remove_db_backup,
    # FTP
    get_ftps as ftps,
    set_ftp_password as change_ftp_password,
)

__version__ = "0.1.0"

__all__ = [
    "BTPanelClient",
    "BTPanelError",
    "api",
    # Aliases
    "system_total",
    "disk_info",
    "network",
    "websites",
    "site_info",
    "create_site",
    "remove_site",
    "enable_site",
    "disable_site",
    "ssl_info",
    "apply_ssl",
    "force_https",
    "disable_force_https",
    "databases",
    "change_db_password",
    "backups",
    "create_site_backup",
    "remove_backup",
    "create_db_backup",
    "remove_db_backup",
    "ftps",
    "change_ftp_password",
]