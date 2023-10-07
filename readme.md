## 预期结果

![1696658500933.jpg](__doc%2F1696658500933.jpg)

## step 01 server 环境准备
根目录下
```shell
cd server
```
### 1.1 初始化
```shell
sh __shell/init.sh
```
### 1.2 安装依赖
```shell
sh __shell/install.sh
```
## step 02 启动开发环境
根目录下
```shell
cd app
```
### 2.1 安装依赖
```
npm install
```
### 2.2 启动开发环境
```shell
npm run start:dev 
```
![1696659201617.jpg](__doc%2F1696659201617.jpg)

## step 03 构建打包
构建结果存储在根目录下 __dist目录
### 3.1 构建 python app
```shell
cd server
sh __shell/build.sh
```
构建结果如下（__dist目录下）
```shell
.
└── server
    └── app
        ├── _internal
        │   ├── Python -> Python.framework/Versions/3.10/Python
        │   ├── Python.framework
        │   ├── __static
        │   ├── base_library.zip
        │   ├── flask-3.0.0.dist-info
        │   ├── lib-dynload
        │   ├── libcrypto.1.1.dylib
        │   ├── liblzma.5.dylib
        │   ├── libmpdec.3.dylib
        │   ├── libreadline.8.dylib
        │   ├── libssl.1.1.dylib
        │   ├── markupsafe
        │   └── werkzeug-3.0.0.dist-info
        └── app

```

### 3.1 构建 electron
根目录下
```
cd app
npm run dist
```
构建结果如下（__dist目录下）
```shell
.
├── server
│   └── app
│       ├── _internal
│       └── app
└── target
    ├── builder-effective-config.yaml
    ├── electron-python-app-1.0.0-universal.dmg
    ├── electron-python-app-1.0.0-universal.dmg.blockmap
    └── mac-universal
        └── electron-python-app.app

```