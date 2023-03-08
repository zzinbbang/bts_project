from .base import * 

ALLOWED_HOSTS = ['www.arinan.site'] # 접속에 쓸 host 주소 입력(ip, dns 등)

CSRF_TRUSTED_ORIGINS = ['https://www.arinan.site'] # csrf 인증을 사용할 domain 주소 입력