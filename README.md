# Online Office for FHC

“凤凰OA”，仅限内部使用

# 一、简述

这是一个用来承载非核心业务的在线办公系统，如签到、请假、奖惩管理、教学交流、业务申请等。财务等重要核心业务不囊括其中。

# 二、项目实现

## 2.1 技术栈



## 2.2 功能设计



## 三、部署实践

### 3.1 虚拟环境



```shell
apt install python3-pip -y
// 更换清华大学pip源
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install --upgrade pip
    
pip3 install virtualenv
virtualenv venv
source venv/bin/active
. venv/bin/deactive 或者 deactive

screen -S oa
screen -ls
screen -r oa
```

### 3.2 celery部署





### 3.3 redis部署





### 3.4 MySQL部署





### 3.5 Nginx部署

