# Wake_Leancloud

唤醒Leancloud

方法步骤：

- 首先 `fork` 一份我的代码：https://github.com/imgyh/script

- 修改 `main.py` 里面的 `get_status("https://valine.0941314.xyz/")` 改成你自己的 `Valine` 评论后台管理地址

- 将 `valine_wake_up.yml` 复制到 `.github/workflows/` 路径下

- 之后他就会在北京时间的 7-23 点，每隔25min执行一次 `valine_wake_up.py` 来唤醒一次 `Valine` 的实例。

# 防止GitHub Workflow 限制

避免Github Action的限制，添加 `avoid.yml` 每月会自动向仓库提交commit，Workflow应该不会被自动暂停了
