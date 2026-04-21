"""
BT Panel API 客户端
"""

import hashlib
import time
from typing import Any, Optional

import requests


class BTPanelClient:
    """BT Panel API 客户端"""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: int = 30,
    ):
        """
        初始化客户端

        @param base_url: BT Panel 地址，格式 http://ip:8888
        @param api_key: API 密钥，从面板设置获取
        @param timeout: 请求超时时间（秒）
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()

    def _generate_token(self, timestamp: int) -> str:
        """生成认证令牌"""
        api_key_md5 = hashlib.md5(self.api_key.encode()).hexdigest()
        raw = str(timestamp) + api_key_md5
        return hashlib.md5(raw.encode()).hexdigest()

    def request(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
    ) -> Any:
        """
        发送 API 请求

        @param path: API 路径，如 /system?action=GetSystemTotal
        @param params: 额外参数
        @return: API 响应（可能是 dict 或 list）
        """
        timestamp = int(time.time())
        
        data: dict[str, Any] = {
            "request_time": timestamp,
            "request_token": self._generate_token(timestamp),
        }
        if params:
            data.update(params)

        url = f"{self.base_url}/{path.lstrip('/')}"

        resp = self.session.post(url, data=data, timeout=self.timeout)
        resp.raise_for_status()

        result = resp.json()
        
        # BT Panel API 有些接口返回 status:false 但数据正常（如 SSL 查询返回私钥）
        # 只有当 status:false 且有 msg 字段时才报错
        if isinstance(result, dict) and result.get("status") is False and "msg" in result:
            raise BTPanelError(result.get("msg", "Unknown error"))
        
        return result

    def close(self):
        """关闭会话"""
        self.session.close()


class BTPanelError(Exception):
    """BT Panel API 错误"""
    pass