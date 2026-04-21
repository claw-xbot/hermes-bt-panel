"""
数据库管理 API
"""

from typing import Any

from ..client import BTPanelClient


def get_databases(
    client: BTPanelClient,
    page: int = 1,
    limit: int = 15,
    search: str = "",
) -> dict[str, Any]:
    """
    获取数据库列表

    @param client: BTPanelClient 实例
    @param page: 页码
    @param limit: 每页数量
    @param search: 搜索关键词
    @return: 数据库列表
    """
    return client.request(
        "/data?action=getData&table=databases",
        params={
            "p": str(page),
            "limit": str(limit),
            "search": search,
        },
    )


def set_database_password(
    client: BTPanelClient,
    database_name: str,
    new_password: str,
) -> dict[str, Any]:
    """
    修改数据库密码

    @param client: BTPanelClient 实例
    @param database_name: 数据库名称
    @param new_password: 新密码
    @return: 操作结果
    """
    # 获取数据库 ID
    result = get_databases(client, search=database_name)
    databases = result.get("data", [])
    
    db_id = None
    for db in databases:
        if db.get("name") == database_name:
            db_id = db.get("id")
            break
    
    if not db_id:
        raise ValueError(f"Database not found: {database_name}")
    
    return client.request("/database?action=ResDatabasePassword", {
        "id": str(db_id),
        "name": database_name,
        "password": new_password,
    })


def create_database_backup(
    client: BTPanelClient,
    database_name: str,
) -> dict[str, Any]:
    """
    创建数据库备份

    @param client: BTPanelClient 实例
    @param database_name: 数据库名称
    @return: 操作结果
    """
    result = get_databases(client, search=database_name)
    databases = result.get("data", [])
    
    db_id = None
    for db in databases:
        if db.get("name") == database_name:
            db_id = db.get("id")
            break
    
    if not db_id:
        raise ValueError(f"Database not found: {database_name}")
    
    return client.request("/database?action=ToBackup", {
        "id": str(db_id),
    })


def delete_database_backup(
    client: BTPanelClient,
    backup_id: str,
) -> dict[str, Any]:
    """
    删除数据库备份

    @param client: BTPanelClient 实例
    @param backup_id: 备份 ID
    @return: 操作结果
    """
    return client.request("/database?action=DelBackup", {
        "id": backup_id,
    })