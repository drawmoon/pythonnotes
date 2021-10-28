# Hey Python

## 模块代理

### Linux

执行以下命令，新建或编辑 `pip.conf` 配置文件：

```bash
mkdir ~/.pip && vim ~/.pip/pip.conf
```

键入以下内容：

```conf
[global]
index-url = https://pypi.doubanio.com/simple
[install]
trusted-host = pypi.doubanio.com
```

### Windows

按下快捷键 `Win + R`，输入 `%APPDATA%` 并回车，新建并进入 `pip` 文件夹，新建并编辑 `pip.ini` 配置文件，键入以下内容：

```ini
[global]
index-url = https://pypi.doubanio.com/simple
[install]
trusted-host = pypi.doubanio.com
```
