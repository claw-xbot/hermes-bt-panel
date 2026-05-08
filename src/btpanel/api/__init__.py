"""
BT Panel API 函数
"""

from .system import (
    get_system_total,
    get_disk_info,
    get_network,
    get_task_count,
    check_panel_update,
)

from .sites import (
    get_websites,
    get_site,
    add_site,
    delete_site,
    start_site,
    stop_site,
    set_site_php_version,
    get_site_domains,
    add_domain,
    delete_domain,
    get_site_logs,
    set_site_notes,
    # 新增
    get_site_types,
    get_php_versions,
    set_site_edate,
    get_rewrite_list,
    get_dir_user_ini,
    set_dir_user_ini,
    open_site_logs,
    set_site_path,
    set_site_run_path,
    set_site_password,
    close_site_password,
    get_limit_net,
    set_limit_net,
    close_limit_net,
    get_index,
    set_index,
)

from .ssl import (
    get_ssl,
    set_ssl,
    http_to_https,
    close_https,
    close_ssl,
)

from .database import (
    get_databases,
    set_database_password,
    create_database_backup,
    delete_database_backup,
)

from .backup import (
    get_backups,
    create_backup,
    delete_backup,
    get_ftps,
    set_ftp_password,
    set_ftp_status,
)

from .docker import (
    get_containers,
    get_container_stats,
    start_container,
    stop_container,
    restart_container,
    remove_container,
    get_images,
    pull_image,
    remove_image,
    get_container_logs,
)

from .cron import (
    get_crons,
    add_cron,
    delete_cron,
    run_cron,
)

from .files import (
    get_file,
    save_file,
    get_dir_list,
)

from .system_settings import (
    get_panel_config,
    set_panel_config,
    get_public_config,
    get_ssl_status,
    set_panel_password,
    get_panel_logs,
)

__all__ = [
    # System
    "get_system_total",
    "get_disk_info",
    "get_network",
    "get_task_count",
    "check_panel_update",
    # Sites
    "get_websites",
    "get_site",
    "add_site",
    "delete_site",
    "start_site",
    "stop_site",
    "set_site_php_version",
    "get_site_domains",
    "add_domain",
    "delete_domain",
    "get_site_logs",
    "set_site_notes",
    "get_site_types",
    "get_php_versions",
    "set_site_edate",
    "get_rewrite_list",
    "get_dir_user_ini",
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
    # SSL
    "get_ssl",
    "set_ssl",
    "http_to_https",
    "close_https",
    "close_ssl",
    # Database
    "get_databases",
    "set_database_password",
    "create_database_backup",
    "delete_database_backup",
    # Backup
    "get_backups",
    "create_backup",
    "delete_backup",
    # FTP
    "get_ftps",
    "set_ftp_password",
    "set_ftp_status",
    # Docker
    "get_containers",
    "get_container_stats",
    "start_container",
    "stop_container",
    "restart_container",
    "remove_container",
    "get_images",
    "pull_image",
    "remove_image",
    "get_container_logs",
    # Cron
    "get_crons",
    "add_cron",
    "delete_cron",
    "run_cron",
    # Files
    "get_file",
    "save_file",
    "get_dir_list",
    # System Settings
    "get_panel_config",
    "set_panel_config",
    "get_public_config",
    "get_ssl_status",
    "set_panel_password",
    "get_panel_logs",
]
