"""
SSL 证书 API
"""

from typing import Any

from ..client import BTPanelClient
from .sites import get_site


def get_ssl(client: BTPanelClient, site_name: str) -> dict[str, Any]:
    """
    获取 SSL 状态和证书详情

    @param client: BTPanelClient 实例
    @param site_name: 域名
    @return: SSL 证书信息
    """
    return client.request("/site?action=GetSSL", {
        "siteName": site_name,
    })


def set_ssl(
    client: BTPanelClient,
    site_name: str,
    cert: str,
    private_key: str,
    cert_type: str = "1",
) -> dict[str, Any]:
    """
    设置 SSL 证书

    @param client: BTPanelClient 实例
    @param site_name: 域名
    @param cert: 证书 PEM 内容
    @param private_key: 私钥内容
    @param cert_type: 证书类型，默认 1
    @return: 操作结果
    """
    return client.request("/site?action=SetSSL", {
        "siteName": site_name,
        "key": private_key,
        "csr": cert,
        "type": cert_type,
    })


def http_to_https(client: BTPanelClient, site_name: str) -> dict[str, Any]:
    """
    开启强制 HTTPS

    @param client: BTPanelClient 实例
    @param site_name: 域名
    @return: 操作结果
    """
    return client.request("/site?action=HttpToHttps", {
        "siteName": site_name,
    })


def close_https(client: BTPanelClient, site_name: str) -> dict[str, Any]:
    """
    关闭强制 HTTPS

    @param client: BTPanelClient 实例
    @param site_name: 域名
    @return: 操作结果
    """
    return client.request("/site?action=CloseToHttps", {
        "siteName": site_name,
    })


def close_ssl(client: BTPanelClient, site_name: str) -> dict[str, Any]:
    """
    关闭 SSL

    @param client: BTPanelClient 实例
    @param site_name: 域名
    @return: 操作结果
    """
    return client.request("/site?action=CloseSSLConf", {
        "siteName": site_name,
    })