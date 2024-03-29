
# autoWHUCourse

**autoWHUCourse** 是一个基于selenium模拟用户点击观看用于在WHU学习通网课自动观看脚本

## 描述

在许多场合，我们抽不出一些时间来学习一系列的视频，但又希望它以正常的速率在电脑上进行播放，且自动切换下一集。**autoWHUCourse** 解决了手动管理播放列表的繁琐，自动化这一过程。
## 优点

模拟用户点击，减少被监测到的风险

在完播情况下随机时间切换下一集，减少被监测到的风险

## 开始

开始使用 **autoWHUCourse** 之前，请确保你满足以下条件。
- 就读于WHU
- 了解过python这一编程语言

## 先决条件

- Python 3.6 或更高版本
- pip (Python 包管理器)
- Chrome，https://www.google.com/intl/zh-CN/chrome/ 版本要求：最新版
- ChromeDriver，https://chromedriver.storage.googleapis.com/index.html 版本要求：与Chrome相同
- 根据文件"chromedriver.exe"的解压缩路径更改环境变量

	（1）打开“设置“搜索“环境变量”

	（2）选择”编辑账户的环境变量“

	（3）双击Path

	（4）新建环境变量

	（5）将"chromedriver.exe"的解压缩路径填入

	（6）确定

	### 环境变量设置完成后请不要更改"chromedriver.exe"的路径
- 

## 安装

首先，克隆仓库到本地机器：

```bash
git clone https://github.com/kitepape/ClassOnlineScriptSolution
cd Your/Path/To/this/Project
```

安装所需的依赖：

```bash
pip install -r requirements.txt
```

如果下载速度过慢，可以使用镜像源进行下载

```bash
pip install -i https://pypi.douban.com/simple selenium
```


## 使用说明

（1）打开”武汉大学信息门户“--”MOOC“--”我学的课“--具体课程（如马克思主义基本原理），复制该网站url:

#### 注意：所复制的网址应为http://mooc1.mooc.whu.edu.cn/mycourse/studentcourse.... 

而不应为http://mooc1.mooc.whu.edu.cn/mycourse/studentstudy....

（2）按照需求指示进行操作，输入学习通账号密码

#### 注意：如果你选择保存账号密码，则会在你的工作目录下生成一个txt文件以记录你的账号密码，如果你选择删除则记录功能将失效。

#### 我们不会窃取或保存您的账号密码。

## 贡献

我们欢迎所有形式的贡献，无论是新功能的建议、bug 修复还是文档改进。如果你想为 **autoWHUCourse** 做出贡献，请遵循以下步骤：

1. Fork 仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -am 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建新的 Pull Request

## 许可证

本项目采用 MIT 许可证。

## 联系方式

如果你有任何问题或建议，请通过以下方式联系我：

- 邮箱：joansorrensen@gmail.com

## 致谢

- 感谢所有为 **autoWHUCourse** 做出贡献的开发者。
- 感谢所有提供反馈和支持的用户。
