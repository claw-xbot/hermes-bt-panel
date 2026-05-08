"""
网站管理 API
"""

from typing import Any, Optional

from ..client import BTPanelClient


def get_websites(
    client: BTPanelClient,
    page: int = 1,
    limit: int = 15,
    search: str = "",
) -> dict[str, Any]:
    """
    获取网站列表

    @param client: BTPanelClient 实例
    @param page: 页码
    @param limit: 每页数量
    @param search: 搜索关键词
    @return: 网站列表数据
    """
    return client.request(
        "/data?action=getData&table=sites",
        params={
            "p": str(page),
            "limit": str(limit),
            "search": search,
        },
    )


def get_site(client: BTPanelClient, site_name: str) -> Optional[dict[str, Any]]:
    """
    获取指定网站信息

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @return: 网站信息，不存在返回 None
    """
    result = get_websites(client, search=site_name)
    sites = result.get("data", [])
    for site in sites:
        if site.get("name") == site_name:
            return site
    return None


def add_site(
    client: BTPanelClient,
    domain: str,
    php_version: str = "00",
    path: Optional[str] = None,
    ftp: bool = False,
    ftp_username: Optional[str] = None,
    ftp_password: Optional[str] = None,
    sql: bool = False,
    sql_username: Optional[str] = None,
    sql_password: Optional[str] = None,
    coding: str = "utf8mb4",
) -> dict[str, Any]:
    """
    创建网站

    @param client: BTPanelClient 实例
    @param domain: 主域名
    @param php_version: PHP 版本，如 73, 74, 80, 81
    @param path: 网站目录，默认 /www/wwwroot/domain
    @param ftp: 是否开启 FTP
    @param ftp_username: FTP 用户名
    @param ftp_password: FTP 密码
    @param sql: 是否创建数据库
    @param sql_username: 数据库用户名
    @param sql_password: 数据库密码
    @param coding: 数据库编码，默认 utf8mb4
    @return: 创建结果
    """
    import json
    
    webname = json.dumps({
        "domain": domain,
        "domainlist": [],
        "count": 0,
    })
    
    site_path = path or f"/www/wwwroot/{domain}"
    
    params = {
        "webname": webname,
        "path": site_path,
        "type": "PHP",
        "type_id": "0",
        "port": "80",
        "version": php_version,
        "ftp": "true" if ftp else "false",
        "sql": "true" if sql else "false",
    }
    
    if ftp and ftp_username and ftp_password:
        params["ftp_username"] = ftp_username
        params["ftp_password"] = ftp_password
    
    if sql and sql_username and sql_password:
        params["datauser"] = sql_username
        params["datapassword"] = sql_password
        params["codeing"] = coding
    
    return client.request("/site?action=AddSite", params)


def delete_site(
    client: BTPanelClient,
    site_name: str,
    delete_ftp: bool = False,
    delete_database: bool = False,
    delete_path: bool = False,
) -> dict[str, Any]:
    """
    删除网站

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @param delete_ftp: 是否删除 FTP
    @param delete_database: 是否删除数据库
    @param delete_path: 是否删除网站目录
    @return: 删除结果
    """
    # 先获取站点 ID
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    params = {
        "id": str(site["id"]),
        "webname": site_name,
        "ftp": "true" if delete_ftp else "false",
        "database": "true" if delete_database else "false",
        "path": "true" if delete_path else "false",
    }
    
    return client.request("/site?action=DeleteSite", params)


def start_site(client: BTPanelClient, site_name: str) -> dict[str, Any]:
    """
    启用网站

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @return: 操作结果
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    return client.request("/site?action=SiteStart", {
        "id": str(site["id"]),
        "name": site_name,
    })


def stop_site(client: BTPanelClient, site_name: str) -> dict[str, Any]:
    """
    停用网站

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @return: 操作结果
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    return client.request("/site?action=SiteStop", {
        "id": str(site["id"]),
        "name": site_name,
    })


def set_site_php_version(
    client: BTPanelClient,
    site_name: str,
    php_version: str,
) -> dict[str, Any]:
    """
    修改网站 PHP 版本

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @param php_version: PHP 版本，如 73, 74, 80, 81
    @return: 操作结果
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    return client.request("/site?action=SetPHPVersion", {
        "id": str(site["id"]),
        "siteName": site_name,
        "version": php_version,
    })


def get_site_domains(client: BTPanelClient, site_name: str) -> dict[str, Any]:
    """
    获取网站域名列表

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @return: 域名列表
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    return client.request(
        "/data?action=getData&table=domain",
        params={
            "search": str(site["id"]),
            "list": "true",
        },
    )


def add_domain(
    client: BTPanelClient,
    site_name: str,
    domain: str,
) -> dict[str, Any]:
    """
    添加网站域名

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @param domain: 新增域名
    @return: 操作结果
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    return client.request("/site?action=AddDomain", {
        "id": str(site["id"]),
        "webname": site_name,
        "domain": domain,
    })


def delete_domain(
    client: BTPanelClient,
    site_name: str,
    domain: str,
    port: int = 80,
) -> dict[str, Any]:
    """
    删除网站域名

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @param domain: 要删除的域名
    @param port: 端口
    @return: 操作结果
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")
    
    return client.request("/site?action=DelDomain", {
        "id": str(site["id"]),
        "webname": site_name,
        "domain": domain,
        "port": str(port),
    })


def get_site_logs(client: BTPanelClient, site_name: str) -> dict[str, Any]:
    """
    获取网站日志

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @return: 日志内容
    """
    return client.request("/site?action=GetSiteLogs", {
        "siteName": site_name,
    })


def set_site_notes(
    client: BTPanelClient,
    site_name: str,
    notes: str,
) -> dict[str, Any]:
    """
    修改网站备注

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @param notes: 备注内容
    @return: 操作结果
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")

    return client.request("/data?action=setPs&table=sites", {
        "id": str(site["id"]),
        "ps": notes,
    })


# 以下是官方文档中有但尚未实现的接口

def get_site_types(client: BTPanelClient) -> Any:
    """
    获取网站分类列表

    @param client: BTPanelClient 实例
    @return: 分类列表
    """
    return client.request("/site?action=get_site_types")


def get_php_versions(client: BTPanelClient) -> Any:
    """
    获取已安装的 PHP 版本列表

    @param client: BTPanelClient 实例
    @return: PHP 版本列表
    """
    return client.request("/site?action=GetPHPVersion")


def set_site_edate(
    client: BTPanelClient,
    site_name: str,
    edate: str,
) -> Any:
    """
    设置网站到期时间

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @param edate: 到期时间，格式 2025-01-01，永久：0000-00-00
    @return: 操作结果
    """
    site = get_site(client, site_name)
    if not site:
        raise ValueError(f"Site not found: {site_name}")

    return client.request("/site?action=SetEdate", {
        "id": str(site["id"]),
        "edate": edate,
    })


def get_rewrite_list(
    client: BTPanelClient,
    site_name: str,
) -> Any:
    """
    获取可选的预定义伪静态列表

    @param client: BTPanelClient 实例
    @param site_name: 网站域名
    @return: 伪静态规则列表
    """
    return client.request("/site?action=GetRewriteList", {
        "siteName": site_name,
    })


def get_dir_user_ini(
    client: BTPanelClient,
    site_id: int,
    site_path: str,
) -> Any:
    """
    获取防跨站配置/运行目录/日志开关状态

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @param site_path: 网站根目录
    @return: 配置信息
    """
    return client.request("/site?action=GetDirUserINI", {
        "id": str(site_id),
        "path": site_path,
    })


def set_dir_user_ini(
    client: BTPanelClient,
    site_path: str,
) -> Any:
    """
    设置防跨站状态（自动取反）

    @param client: BTPanelClient 实例
    @param site_path: 网站根目录
    @return: 操作结果
    """
    return client.request("/site?action=SetDirUserINI", {
        "path": site_path,
    })


def open_site_logs(
    client: BTPanelClient,
    site_id: int,
) -> Any:
    """
    开启网站访问日志

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @return: 操作结果
    """
    return client.request("/site?action=logsOpen", {
        "id": str(site_id),
    })


def set_site_path(
    client: BTPanelClient,
    site_id: int,
    new_path: str,
) -> Any:
    """
    修改网站根目录

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @param new_path: 新的网站根目录
    @return: 操作结果
    """
    return client.request("/site?action=SetPath", {
        "id": str(site_id),
        "path": new_path,
    })


def set_site_run_path(
    client: BTPanelClient,
    site_id: int,
    run_path: str,
) -> Any:
    """
    设置网站运行目录

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @param run_path: 基于网站根目录的运行目录，如 /public
    @return: 操作结果
    """
    return client.request("/site?action=SetSiteRunPath", {
        "id": str(site_id),
        "runPath": run_path,
    })


def set_site_password(
    client: BTPanelClient,
    site_id: int,
    username: str,
    password: str,
) -> Any:
    """
    设置网站密码访问

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @param username: 用户名
    @param password: 密码
    @return: 操作结果
    """
    return client.request("/site?action=SetHasPwd", {
        "id": str(site_id),
        "username": username,
        "password": password,
    })


def close_site_password(
    client: BTPanelClient,
    site_id: int,
) -> Any:
    """
    关闭网站密码访问

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @return: 操作结果
    """
    return client.request("/site?action=CloseHasPwd", {
        "id": str(site_id),
    })


def get_limit_net(
    client: BTPanelClient,
    site_id: int,
) -> Any:
    """
    获取流量限制配置（仅支持 nginx）

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @return: 流量限制配置
    """
    return client.request("/site?action=GetLimitNet", {
        "id": str(site_id),
    })


def set_limit_net(
    client: BTPanelClient,
    site_id: int,
    perserver: int,
    perip: int,
    limit_rate: int,
) -> Any:
    """
    开启或保存流量限制配置（仅支持 nginx）

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @param perserver: 并发限制
    @param perip: 单 IP 限制
    @param limit_rate: 流量限制 (KB)
    @return: 操作结果
    """
    return client.request("/site?action=SetLimitNet", {
        "id": str(site_id),
        "perserver": str(perserver),
        "perip": str(perip),
        "limit_rate": str(limit_rate),
    })


def close_limit_net(
    client: BTPanelClient,
    site_id: int,
) -> Any:
    """
    关闭流量限制（仅支持 nginx）

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @return: 操作结果
    """
    return client.request("/site?action=CloseLimitNet", {
        "id": str(site_id),
    })


def get_index(
    client: BTPanelClient,
    site_id: int,
) -> Any:
    """
    获取默认文档信息

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @return: 默认文档列表
    """
    return client.request("/site?action=GetIndex", {
        "id": str(site_id),
    })


def set_index(
    client: BTPanelClient,
    site_id: int,
    index: str,
) -> Any:
    """
    设置默认文档

    @param client: BTPanelClient 实例
    @param site_id: 网站 ID
    @param index: 默认文档，逗号分隔，如 index.php,index.html
    @return: 操作结果
    """
    return client.request("/site?action=SetIndex", {
        "id": str(site_id),
        "Index": index,
    })