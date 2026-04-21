"""
系统信息 API
"""

from typing import Any

from ..client import BTPanelClient


def get_system_total(client: BTPanelClient) -> dict[str, Any]:
    """
    获取系统基础统计

    @param client: BTPanelClient 实例
    @return: CPU/内存/磁盘/负载等信息
    """
    return client.request("/system?action=GetSystemTotal")


def get_disk_info(client: BTPanelClient) -> dict[str, Any]:
    """
    获取磁盘分区信息

    @param client: BTPanelClient 实例
    @return: 各分区磁盘使用情况
    """
    return client.request("/system?action=GetDiskInfo")


def get_network(client: BTPanelClient) -> dict[str, Any]:
    """
    获取实时网络状态

    @param client: BTPanelClient 实例
    @return: 网络流量、CPU、内存实时数据
    """
    return client.request("/system?action=GetNetWork")


def get_task_count(client: BTPanelClient) -> dict[str, Any]:
    """
    检查是否有安装任务

    @param client: BTPanelClient 实例
    @return: 任务数量
    """
    return client.request("/ajax?action=GetTaskCount")


def check_panel_update(client: BTPanelClient) -> dict[str, Any]:
    """
    检查面板更新

    @param client: BTPanelClient 实例
    @return: 更新信息
    """
    return client.request("/ajax?action=UpdatePanel")