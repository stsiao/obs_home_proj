# b站弹幕姬构建简易说明

> 根据github项目更新自动构建。本仓库文件几乎无需调整。

在github项目的基础上存在4个补丁：

- 00-about-path.diff: 修正原项目的关于文档生成位置、以及关于对话框在非windows系统中无法打开的问题
- 00-conf-path.diff: 修正了默认配置条件下，程序背景、程序图标、设置文件路径有无的问题
- 01-about-to-home.diff: 在00-about-path基础上，将生成文件的位置调整到home中。（openSUSE在opt中较难进行写入操作）
- 01-log-to-home.diff: 修正log生成路径错误，并将路径调整到home中（理由同上）

**两个00已经提交至上游，可能之后需要去除；两个01为针对openSUSE的调整，应始终保留**

存在一个opensuse中无法直接安装的依赖：aiowebsocket。这是直接通过pip下载保存（不安装）后压缩的，之后应该是直接放在程序根目录。但看目前的spec，貌似只在setup之后就没有其他操作了。所以这里有时间需要用一个新机器测试。

---

- [ ] 测试aiowebsocket部署
