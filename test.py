#!/usr/bin/env python3
"""
BT Panel CLI 测试脚本
用法: python3 test.py [命令]

示例:
  python3 test.py status       # 系统状态
  python3 test.py sites      # 网站列表
  python3 test.py ssl xbot.my  # SSL状态
"""
import sys
sys.path.insert(0, 'src')

from btpanel import BTPanelClient
from btpanel.api import *

API_URL = "http://192.168.69.102:6888"
API_KEY = "Wj3hhUltH9sXZueDU8Oy6KoYSwsiFkRe"

def main():
    client = BTPanelClient(API_URL, API_KEY)
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'help'
    
    if cmd == 'status':
        r = get_network(client)
        print(f"面板: {r.get('title')}")
        print(f"系统: {r.get('simple_system')}")
        print(f"CPU: {r.get('cpu', [])[3]}")
        print(f"内存: {r.get('mem', {}).get('memNewRealUsed')} / {r.get('mem', {}).get('memNewTotal')}")
        print(f"网站: {r.get('site_total')}个")
        print(f"数据库: {r.get('database_total')}个")
    
    elif cmd == 'sites':
        sites = get_websites(client).get('data', [])
        print(f"网站列表 ({len(sites)}个):")
        for s in sites:
            print(f"  - {s['name']} [{s['status']}]")
    
    elif cmd == 'ssl':
        domain = sys.argv[2] if len(sys.argv) > 2 else 'xbot.my'
        r = get_ssl(client, domain)
        has = 'key' in r and r['key'].startswith('-----BEGIN')
        print(f"{domain}: {'✅ 有证书' if has else '❌ 无'}")
    
    else:
        print(__doc__)

if __name__ == '__main__':
    main()