import argparse


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    a = p.parse_args()
    if not a.name.strip():
        p.error("--name 不能为纯空白字符")
    print(f"Hello, {a.name}!")
