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
    # 注意: 面板 11.5.0 中 /panel?action=GetPanelConfig 返回 404
    # 使用 /panel/public/get_public_config 获取公共配置
    return client.request("/panel/public/get_public_config")


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
    # 注意: 面板 11.5.0 中此接口可能不可用
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
    # 注意: 面板 11.5.0 中 /panel?action=GetSSL 返回 404
    # 此接口可能不可用
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
    # 注意: 面板 11.5.0 中此接口可能不可用
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
    # 注意: 面板 11.5.0 中 /panel?action=GetLogs 返回 404
    # 使用 /data?action=getData&table=logs 获取日志
    return client.request(
        "/data?action=getData&table=logs",
        params={
            "p": str(page),
            "limit": str(limit),
        },
    )