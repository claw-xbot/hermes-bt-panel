"""
系统设置 API
"""

from typing import Any

from ..client import BTPanelClient


def get_panel_config(
    client: BTPanelClient,
) -> Any:
    """
    获取面板配置

    @param client: BTPanelClient 实例
    @return: 面板配置信息
    """
    return client.request("/panel?action=GetPanelConfig")


def set_panel_config(
    client: BTPanelClient,
    config: dict[str, Any],
) -> Any:
    """
    修改面板配置

    @param client: BTPanelClient 实例
    @param config: 配置项字典
    @return: 操作结果
    """
    return client.request(
        "/panel?action=SetPanelConfig",
        params=config,
    )


def get_public_config(
    client: BTPanelClient,
) -> Any:
    """
    获取面板公共配置

    @param client: BTPanelClient 实例
    @return: 公共配置信息
    """
    return client.request("/panel/public/get_public_config")


def get_ssl_status(
    client: BTPanelClient,
) -> Any:
    """
    获取面板SSL状态

    @param client: BTPanelClient 实例
    @return: SSL状态
    """
    return client.request("/panel?action=GetSSL")


def set_panel_password(
    client: BTPanelClient,
    password: str,
) -> Any:
    """
    修改面板密码

    @param client: BTPanelClient 实例
    @param password: 新密码
    @return: 操作结果
    """
    return client.request(
        "/panel?action=SetPassword",
        params={"password": password},
    )


def get_panel_logs(
    client: BTPanelClient,
    page: int = 1,
    limit: int = 100,
) -> Any:
    """
    获取面板日志

    @param client: BTPanelClient 实例
    @param page: 页码
    @param limit: 每页数量
    @return: 日志列表
    """
    return client.request(
        "/panel?action=GetLogs",
        params={
            "p": str(page),
            "limit": str(limit),
        },
    )