# Baidu_Submit

在你fork的仓库下的 `settings` -> `Secrets` -> `New repository secret` 添加如下两个`Secrets`

|  Name   | Value  |
|  :----  | :----  |
| BAIDU_SUBMIT_API | 百度的API提交url如下图 |
| BAIDU_SITEMAP_URL  | 你自己博客的百度sitemap地址 示例： |

BAIDU_SUBMIT_API 示例：http://data.zz.baidu.com/urls?site=https://www.imgyh.com&token=XXXX
BAIDU_SITEMAP_URL 示例：https://www.imgyh.com/baidusitemap.xml


# 防止GitHub Workflow 限制

避免Github Action的限制，添加 `avoid.yml` 每月会自动向仓库提交commit，Workflow应该不会被自动暂停了
