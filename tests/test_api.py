"""
BT Panel API 测试
"""
import pytest
import os
import sys

sys.path.insert(0, 'src')

from btpanel import BTPanelClient
from btpanel.api import (
    get_system_total,
    get_network,
    get_websites,
    get_ssl,
    get_databases,
    get_ftps,
)
from btpanel.client import BTPanelError


API_URL = os.getenv("BT_API_URL", "http://192.168.69.102:6888")
API_KEY = os.getenv("BT_API_KEY", "Wj3hhUltH9sXZueDU8Oy6KoYSwsiFkRe")


@pytest.fixture
def client():
    return BTPanelClient(API_URL, API_KEY)


class TestSystem:
    """系统状态测试"""
    
    def test_get_network(self, client):
        r = get_network(client)
        assert 'cpu' in r
        assert 'mem' in r
    
    def test_get_system_total(self, client):
        r = get_system_total(client)
        assert r is not None


class TestSites:
    """网站管理测试"""
    
    def test_get_websites(self, client):
        r = get_websites(client)
        assert 'data' in r
        sites = r['data']
        assert isinstance(sites, list)
    
    def test_sites_have_required_fields(self, client):
        r = get_websites(client)
        sites = r['data']
        if sites:
            s = sites[0]
            assert 'name' in s
            assert 'path' in s
            assert 'status' in s


class TestSSL:
    """SSL证书测试"""
    
    def test_get_ssl(self, client):
        r = get_websites(client)
        sites = r['data']
        if sites:
            domain = sites[0]['name']
            ssl = get_ssl(client, domain)
            # 返回可能有 key 也可能没有
            assert isinstance(ssl, dict)


class TestDatabase:
    """数据库测试"""
    
    def test_get_databases(self, client):
        r = get_databases(client)
        assert 'data' in r


class TestFTP:
    """FTP测试"""
    
    def test_get_ftps(self, client):
        r = get_ftps(client)
        assert 'data' in r


class TestClient:
    """客户端测试"""
    
    def test_invalid_token(self):
        with pytest.raises(BTPanelError):
            client = BTPanelClient(API_URL, "invalid_key")
            get_network(client)
    
    def test_invalid_url(self):
        with pytest.raises(Exception):
            client = BTPanelClient("http://invalid:6888", API_KEY)
            get_network(client)