# -*- coding: UTF-8 -*
from functools import wraps
from flask import abort
from flask.ext.login import current_user

from .models import Permission

# 检查用户权限的自定义修饰器
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permissions):
                abort(403)
            return f(*args, **kwargs)
        return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)