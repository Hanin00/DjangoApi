from django.contrib import admin
from . import models


#관리자 사이트에 모델 등록
admin.site.register(models.Cat)