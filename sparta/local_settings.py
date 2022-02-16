# For Production
# SECRET_KEY = "django-insecure-uspu)$wi(do!x3vt#quwvlba)ne=+i=(^r$axqw1r1^6n8rn%w"
# DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "sparta",
        "USER": "root",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "3306",
    }
}



# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.oracle",
#         "NAME": "XE",
#         "USER": "kys",
#         "PASSWORD": "1234",
#         "HOST": "localhost",
#         "PORT": "1521",
#     }
# }