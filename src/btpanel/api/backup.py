"""
网站备份 API
"""

from typing import Any

from ..client import BTPanelClient
from .sites import get_site


def get_backups(
    client: BTPanelClient,
    site_name: str,
    page: int = 1,
    limit: int = 5,
) -> dict[str, Any]:
    """
    获取网站备份列表

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @param page: 页码
    @param limit: 每页数量
    @return: 备份列表
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    return client.request(
        "/data?action=getData&table=backup",
        params={
            "search": str(site["id"]),
            "p": str(page),
            "limit": str(limit),
            "type": "0",
        },
    )


def create_backup(
    client: BTPanelClient,
    site_name: str,
) -> dict[str, Any]:
    """
    创建网站备份

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @return: 操作结果
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    return client.request("/site?action=ToBackup", {
        "id": str(site["id"]),
    })


def delete_backup(
    client: BTPanelClient,
    backup_id: str,
) -> dict[str, Any]:
    """
    删除网站备份

    @param client: BTPanelClient 实例
    @param backup_id: 备份 ID
    @return: 操作结果
    """
    return client.request("/site?action=DelBackup", {
        "id": backup_id,
    })


# FTP 管理


def get_ftps(
    client: BTPanelClient,
    page: int = 1,
    limit: int = 15,
    search: str = "",
) -> dict[str, Any]:
    """
    获取 FTP 列表

    @param client: BTPanelClient 实例
    @param page: 页码
    @param limit: 每页数量
    @param search: 搜索关键词
    @return: FTP 列表
    """
    return client.request(
        "/data?action=getData&table=ftps",
        params={
            "p": str(page),
            "limit": str(limit),
            "search": search,
        },
    )


def set_ftp_password(
    client: BTPanelClient,
    ftp_username: str,
    new_password: str,
) -> dict[str, Any]:
    """
    修改 FTP 密码

    @param client: BTPanelClient 实例
    @param ftp_username: FTP 用户名
    @param new_password: 新密码
    @return: 操作结果
    """
    # 获取 FTP ID
    result = get_ftps(client, search=ftp_username)
    ftps = result.get("data", [])
    
    ftp_id = None
    for ftp in ftps:
        if ftp.get("name") == ftp_username:
            ftp_id = ftp.get("id")
            break
    
    if not ftp_id:
        raise ValueError(f"FTP user not found: {ftp_username}")
    
    return client.request("/ftp?action=SetUserPassword", {
        "id": str(ftp_id),
        "ftp_username": ftp_username,
        "new_password": new_password,
    })


def set_ftp_status(
    client: BTPanelClient,
    ftp_username: str,
    status: int,
) -> dict[str, Any]:
    """
    启用/禁用 FTP

    @param client: BTPanelClient 实例
    @param ftp_username: FTP 用户名
    @param status: 状态，0=关闭，1=开启
    @return: 操作结果
    """
    result = get_ftps(client, search=ftp_username)
    ftps = result.get("data", [])
    
    ftp_id = None
    for ftp in ftps:
        if ftp.get("name") == ftp_username:
            ftp_id = ftp.get("id")
            break
    
    if not ftp_id:
        raise ValueError(f"FTP user not found: {ftp_username}")
    
    return client.request("/ftp?action=SetStatus", {
        "id": str(ftp_id),
        "username": ftp_username,
        "status": str(status),
    })