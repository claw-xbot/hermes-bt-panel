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
    get_task_count as task_count,
    check_panel_update as check_update,
    # Sites
    get_websites as websites,
    get_site as site_info,
    add_site as create_site,
    delete_site as remove_site,
    start_site as enable_site,
    stop_site as disable_site,
    set_site_php_version as set_php_version,
    get_site_domains as site_domains,
    add_domain as add_site_domain,
    delete_domain as remove_site_domain,
    get_site_logs as site_logs,
    set_site_notes as set_site_ps,
    get_site_types as site_types,
    get_php_versions as php_versions,
    set_site_edate as set_site_expire,
    get_rewrite_list as rewrite_list,
    get_dir_user_ini as dir_user_ini,
    set_dir_user_ini as set_dir_user_ini,
    open_site_logs as open_site_logs,
    set_site_path as set_site_path,
    set_site_run_path as set_site_run_path,
    set_site_password as set_site_password,
    close_site_password as close_site_password,
    get_limit_net as get_limit_net,
    set_limit_net as set_limit_net,
    close_limit_net as close_limit_net,
    get_index as get_index,
    set_index as set_index,
    # SSL
    get_ssl as ssl_info,
    set_ssl as apply_ssl,
    http_to_https as force_https,
    close_https as disable_force_https,
    close_ssl as disable_ssl,
    # Database
    get_databases as databases,
    set_database_password as change_db_password,
    create_database_backup as create_db_backup,
    delete_database_backup as remove_db_backup,
    # Backup
    get_backups as backups,
    create_backup as create_site_backup,
    delete_backup as remove_backup,
    # FTP
    get_ftps as ftps,
    set_ftp_password as change_ftp_password,
    set_ftp_status as set_ftp_status,
    # Docker
    get_containers as containers,
    get_container_stats as container_stats,
    start_container as start_container,
    stop_container as stop_container,
    restart_container as restart_container,
    remove_container as remove_container,
    get_images as images,
    pull_image as pull_image,
    remove_image as remove_image,
    get_container_logs as container_logs,
    # Cron
    get_crons as crons,
    add_cron as add_cron,
    delete_cron as remove_cron,
    run_cron as run_cron,
    # Files
    get_file as read_file,
    save_file as write_file,
    get_dir_list as list_dir,
    # System Settings
    get_panel_config as panel_config,
    set_panel_config as set_panel_config,
    get_public_config as public_config,
    get_ssl_status as panel_ssl_status,
    set_panel_password as change_panel_password,
    get_panel_logs as panel_logs,
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
    "task_count",
    "check_update",
    "websites",
    "site_info",
    "create_site",
    "remove_site",
    "enable_site",
    "disable_site",
    "set_php_version",
    "site_domains",
    "add_site_domain",
    "remove_site_domain",
    "site_logs",
    "set_site_ps",
    "site_types",
    "php_versions",
    "set_site_expire",
    "rewrite_list",
    "dir_user_ini",
    "set_dir_user_ini",
    "open_site_logs",
    "set_site_path",
    "set_site_run_path",
    "set_site_password",
    "close_site_password",
    "get_limit_net",
    "set_limit_net",
    "close_limit_net",
    "get_index",
    "set_index",
    "ssl_info",
    "apply_ssl",
    "force_https",
    "disable_force_https",
    "disable_ssl",
    "databases",
    "change_db_password",
    "create_db_backup",
    "remove_db_backup",
    "backups",
    "create_site_backup",
    "remove_backup",
    "ftps",
    "change_ftp_password",
    "set_ftp_status",
    "containers",
    "container_stats",
    "start_container",
    "stop_container",
    "restart_container",
    "remove_container",
    "images",
    "pull_image",
    "remove_image",
    "container_logs",
    "crons",
    "add_cron",
    "remove_cron",
    "run_cron",
    "read_file",
    "write_file",
    "list_dir",
    "panel_config",
    "set_panel_config",
    "public_config",
    "panel_ssl_status",
    "change_panel_password",
    "panel_logs",
]
