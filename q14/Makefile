# 声明伪目标，防止目录下有同名文件导致 make 误判
.PHONY: all clean

# 默认目标：依赖于两个最终产物
all: stats.txt report.txt

# stats.txt 依赖于源数据 data.csv 和脚本 stats.py
stats.txt: data.csv stats.py
	python3 stats.py

# report.txt 依赖于中间产物 stats.txt、脚本 build_report.py 以及模板文件 report.md
report.txt: stats.txt build_report.py report.md
	python3 build_report.py

# 清理规则：只删除生成的产物，不删除源文件
clean:
	rm -f stats.txt report.txt
