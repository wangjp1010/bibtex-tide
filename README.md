# bibtex-tide

## 1.去除重复参考文献：

[在线工具](https://flamingtempura.github.io/bibtex-tidy/)

在左侧粘贴.bib文件内容，右侧Duplicates勾选What to check中的所有内容，勾选Merge duplicate entries后点击Tidy，自动格式化并去重。

## 2.其他功能

目前bibtex-tide.py中在三个函数中分别实现了保留参考文献特定keys，统一arxiv格式，会议名称缩写功能。

RULES.PY中定义了要保留的keys，文献缩写及正则表达（不断添加完善）。

修改bib文件路径后即可一键运行。
