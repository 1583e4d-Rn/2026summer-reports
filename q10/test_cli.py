import sys
import os

# 将 q10/src 目录加入到 Python 搜索路径中
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import pytest
from greetlab.cli import main

def test_blank_name_exits_with_2(monkeypatch):
    # 模拟命令行输入
    monkeypatch.setattr(sys, 'argv', ['sdt-greet', '--name', '   '])
    with pytest.raises(SystemExit) as exc_info:
        main()
    # 验证退出码为 2
    assert exc_info.value.code == 2
