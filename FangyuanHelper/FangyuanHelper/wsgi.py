"""
WSGI config for FangyuanHelper project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# import sys
#
# sys.path.append('D:/myproject/zufang_helper/FangyuanHelper/FangyuanHelper')
#
# sys.path.append('D:/myproject/zufang_helper/FangyuanHelper')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FangyuanHelper.settings")

application = get_wsgi_application()
