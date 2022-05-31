from .faust import app
from .settings import MY_APPS

if __name__ == '__main__':
    app.discover(*MY_APPS, ignore=['rest_framework'])
    app.main()