import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import options.options_development_envirnment as ode

# 网站的基本配置

# 后台界面的大标题

ADMIN_SITE_TITLE_1 = '网站管理后台'
# 后台界面的小标题
ADMIN_SITE_TITLE_2 = '后台'

# 数据库类型
DATABASE_MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ode.DATABASES_NAME,
        'USER': ode.DATABASES_USER,
        'PASSWORD': ode.DATABASES_PASSWORD,
        'HOST': ode.DATABASES_SERVER_IP,
        'PORT': ode.DATABASES_SERVER_PORT
    }
}
DATABASE_SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SIMPLEUI_LOGO = 'static/images/favicon.png'
