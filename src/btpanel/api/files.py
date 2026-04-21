"""
文件操作 API
"""

from typing import Any

from ..client import BTPanelClient


def get_file(
    client: BTPanelClient,
    path: str,
) -> Any:
    """
    读取文件内容

    @param client: BTPanelClient 实例
    @param path: 文件路径，如 /www/wwwroot/site.com/index.php
    @return: 文件内容
    """
    return client.request(
        "/files?action=GetFileBody",
        params={"path": path},
    )


def save_file(
    client: BTPanelClient,
    path: str,
    content: str,
    encoding: str = "utf-8",
) -> Any:
    """
    保存文件内容

    @param client: BTPanelClient 实例
    @param path: 文件路径
    @param content: 文件内容
    @param encoding: 编码，默认 utf-8
    @return: 操作结果
    """
    return client.request(
        "/files?action=SaveFileBody",
        params={
            "path": path,
            "data": content,
            "encoding": encoding,
        },
    )


def get_dir_list(
    client: BTPanelClient,
    path: str,
) -> Any:
    """
    获取目录文件列表

    @param client: BTPanelClient 实例
    @param path: 目录路径
    @return: 文件列表
    """
    return client.request(
        "/files?action=GetDir",
        params={"path": path},
    )