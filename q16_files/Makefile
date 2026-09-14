.PHONY: check build clean

# check: 调用质量门禁脚本
check:
	./check.sh

# build: 构建 wheel
build:
	python3 -m build

# clean: 清理构建产物和缓存
clean:
	rm -rf dist/ build/ *.egg-info .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
