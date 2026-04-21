"""
计划任务 API
"""

from typing import Any

from ..client import BTPanelClient


def get_crons(
    client: BTPanelClient,
) -> Any:
    """
    获取计划任务列表

    @param client: BTPanelClient 实例
    @return: 任务列表
    """
    return client.request("/crontab?action=GetCrontab")


def add_cron(
    client: BTPanelClient,
    name: str,
    type_: str,
    hour: str = "*",
    minute: str = "*",
    week: str = "*",
    day: str = "*",
    month: str = "*",
    s_body: str = "",
) -> Any:
    """
    添加计划任务

    @param client: BTPanelClient 实例
    @param name: 任务名称
    @param type_: 任务类型（backup_site/backup_database/log_cut/shell等）
    @param hour: 小时，* 表示每时
    @param minute: 分钟，* 表示每分
    @param week: 星期，* 表示每天
    @param day: 日期，* 表示每天
    @param month: 月份，* 表示每月
    @param s_body: 脚本内容（type=shell时使用）
    @return: 操作结果
    """
    return client.request(
        "/crontab?action=AddCrontab",
        params={
            "name": name,
            "type": type_,
            "hour": hour,
            "minute": minute,
            "week": week,
            "day": day,
            "month": month,
            "sBody": s_body,
        },
    )


def delete_cron(
    client: BTPanelClient,
    cron_id: str,
) -> Any:
    """
    删除计划任务

    @param client: BTPanelClient 实例
    @param cron_id: 任务 ID
    @return: 操作结果
    """
    return client.request(
        "/crontab?action=DelCrontab",
        params={"id": cron_id},
    )


def run_cron(
    client: BTPanelClient,
    cron_id: str,
) -> Any:
    """
    执行计划任务（立即执行一次）

    @param client: BTPanelClient 实例
    @param cron_id: 任务 ID
    @return: 操作结果
    """
    return client.request(
        "/crontab?action=StartTask",
        params={"id": cron_id},
    )