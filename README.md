# purch-info-spider
purchasing information spider

该项目为`招标信息网站`信息采集工具。
采集到的信息保存在`output`文件夹内，每个网站按配置文件中的网站名称单独保存，所有信息会同步储存在`All.csv`文件和sqlite3数据库中。
抓取时可以跳过数据库中已存在的信息。
支持设置关键词进行信息筛选并保存在`筛选结果.csv`文件中。

## 开发环境
Python 3.8.2

## 使用的第三方库
configparser
selenium
colorlog

## 其他需求
chromedriver  +  chrome
或
geckodriver  + firefox

可使用install.py脚本自动下载最新版本webdriver和浏览器。
webdriver版本需与浏览器版本一致。

## 使用方法
参考spider.conf.example模板文件建立自己的配置文件spider.conf，可设置多组关键词进行结果过滤。
第一次使用的时候执行`python install.py`可自动安装第三方库和下载webdriver、浏览器。如需更新，再次运行即可。
在website_data.conf文件中配置网站抓取规则后执行`python spider.py`即可。

可使用`python spider.py n`的方式单独抓取配置文件中的网站，n为配置文件中网站的顺序号，从0开始计算。

可使用`python re_filter.py`的方式对抓取结果重新进行过滤。

## 其他相关说明
之所以Chrome浏览器默认不使用浏览器无头模式，是因为Chrome在无头模式下经常抓取出错，不确定是什么原因，有兴趣的可以自己开启试试，在spider.py文件中取消相关代码的注释即可。
