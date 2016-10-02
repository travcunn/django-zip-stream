DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SECRET_KEY = '8ij$(7l2!w0f8kggntbv=+$bd=^2xs$cl+3v^_##qjw@2py9_3'

INSTALLED_APPS = (
    'django_zip_stream',
)
