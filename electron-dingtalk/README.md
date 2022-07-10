# electron钉钉构建简易说明

> 本项目为Electron构建，受限于OBS服务无法联网，本项目需要在本地构建好后压缩，在OBS直接打包。这里主要记录获取—压缩的过程

1. 在GitHub项目里，Releases中下载最新的source code(tar.gz)，解压
2. 进入解压后的文件夹，通过下面命令构建程序
    1. 安装依赖 `npm install`
    2. 打包源码 `npm run build`
    3. 生成安装包 `npm run pack`
3. 通过上述命令，会在release中生成最终项目
4. 将其中的linux-unpacked文件夹进行压缩，得到可以上传到OBS项目的tar.gz源文件
