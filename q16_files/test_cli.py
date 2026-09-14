import os
import sys

# 将 q13/src 目录加入到 Python 搜索路径中
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

import pytest

from greetlab.cli import main


def test_blank_name_exits_with_2(monkeypatch):
    # 模拟命令行输入
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as exc_info:
        main()
    # 验证退出码为 2
    assert exc_info.value.code == 2


def test_normal_name(monkeypatch, capsys):
    """测试正常姓名，应输出 Hello 问候语并正常退出。"""
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "Alice"])
    main()

    captured = capsys.readouterr()
    assert "Hello, Alice!" in captured.out


def test_blank_name(monkeypatch, capsys):
    """测试纯空白姓名，应以 SystemExit(2) 结束。"""
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2

    captured = capsys.readouterr()
    assert "error" in captured.err.lower()
