"""
Docker 容器 API
"""

from typing import Any

from ..client import BTPanelClient


def get_containers(
    client: BTPanelClient,
    page: int = 1,
    limit: int = 15,
) -> Any:
    """
    获取容器列表

    @param client: BTPanelClient 实例
    @param page: 页码
    @param limit: 每页数量
    @return: 容器列表
    """
    return client.request(
        "/docker?action=GetContainerList",
        params={
            "p": str(page),
            "limit": str(limit),
        },
    )


def get_container_stats(
    client: BTPanelClient,
    container_id: str,
) -> Any:
    """
    获取容器详细信息

    @param client: BTPanelClient 实例
    @param container_id: 容器 ID 或名称
    @return: 容器详情
    """
    return client.request(
        "/docker?action=GetContainerInfo",
        params={"id": container_id},
    )


def start_container(
    client: BTPanelClient,
    container_id: str,
) -> Any:
    """
    启动容器

    @param client: BTPanelClient 实例
    @param container_id: 容器 ID
    @return: 操作结果
    """
    return client.request(
        "/docker?action=StartContainer",
        params={"id": container_id},
    )


def stop_container(
    client: BTPanelClient,
    container_id: str,
) -> Any:
    """
    停止容器

    @param client: BTPanelClient 实例
    @param container_id: 容器 ID
    @return: 操作结果
    """
    return client.request(
        "/docker?action=StopContainer",
        params={"id": container_id},
    )


def restart_container(
    client: BTPanelClient,
    container_id: str,
) -> Any:
    """
    重启容器

    @param client: BTPanelClient 实例
    @param container_id: 容器 ID
    @return: 操作结果
    """
    return client.request(
        "/docker?action=RestartContainer",
        params={"id": container_id},
    )


def remove_container(
    client: BTPanelClient,
    container_id: str,
    force: bool = False,
) -> Any:
    """
    删除容器

    @param client: BTPanelClient 实例
    @param container_id: 容器 ID
    @param force: 强制删除
    @return: 操作结果
    """
    return client.request(
        "/docker?action=RemoveContainer",
        params={
            "id": container_id,
            "force": "true" if force else "false",
        },
    )


def get_images(
    client: BTPanelClient,
) -> Any:
    """
    获取本地镜像列表

    @param client: BTPanelClient 实例
    @return: 镜像列表
    """
    return client.request("/docker?action=GetImageList")


def pull_image(
    client: BTPanelClient,
    image: str,
    tag: str = "latest",
) -> Any:
    """
    拉取镜像

    @param client: BTPanelClient 实例
    @param image: 镜像名，如 nginx
    @param tag: 标签，默认 latest
    @return: 操作结果
    """
    return client.request(
        "/docker?action=PullImage",
        params={"image": f"{image}:{tag}"},
    )


def remove_image(
    client: BTPanelClient,
    image_id: str,
) -> Any:
    """
    删除镜像

    @param client: BTPanelClient 实例
    @param image_id: 镜像 ID
    @return: 操作结果
    """
    return client.request(
        "/docker?action=RemoveImage",
        params={"id": image_id},
    )


def get_container_logs(
    client: BTPanelClient,
    container_id: str,
    lines: int = 100,
) -> Any:
    """
    获取容器日志

    @param client: BTPanelClient 实例
    @param container_id: 容器 ID
    @param lines: 日志行数
    @return: 日志内容
    """
    return client.request(
        "/docker?action=GetContainerLogs",
        params={
            "id": container_id,
            "lines": str(lines),
        },
    )