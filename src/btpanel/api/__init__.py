"""
BT Panel API 函数
"""

from .system import (
    get_system_total,
    get_disk_info,
    get_network,
)

from .sites import (
    get_websites,
    get_site,
    add_site,
    delete_site,
    start_site,
    stop_site,
)

from .ssl import (
    get_ssl,
    set_ssl,
    http_to_https,
    close_https,
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
    # Sites
    "get_websites",
    "get_site",
    "add_site",
    "delete_site",
    "start_site",
    "stop_site",
    # SSL
    "get_ssl",
    "set_ssl",
    "http_to_https",
    "close_https",
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