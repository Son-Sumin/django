## django를 활용한 Project와 App 생성 시 세팅
- 추후 해당 Project 접근   
  File > Settings > Project: PycharmProject > Python Interpreter > 내가 작업했던 환경으로 Interpreter 선정
- 실행   
  Pycharm terminal에서   
  (내가 작업한 가상환경 이름) 확인
  ---python manage.py runserver
<br>

### 1) ./board/settings.py 
<pre>
<code>
  # Application definition
  # app 추가시 하나씩 추가
  INSTALLED_APPS = [
     ...,
    'bulletin_board.apps.BulletinBoardConfig',
  ]


  # Database
  # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'django_db',
          'USER': 'django',
          'PASSWORD': '1234',
          'PORT': '3307',
      }
  }

  import pymysql
  pymysql.version_info={1, 4, 2, 'final', 0}
  pymysql.install_as_MySQLdb()


  # Internationalization
  # https://docs.djangoproject.com/en/3.2/topics/i18n/
  LANGUAGE_CODE = 'en-us'
  TIME_ZONE = 'Asia/Seoul'
  USE_I18N = True
  USE_L10N = True
  USE_TZ = False
</code>
</pre>

- Pycharm terminal   
  web-env 확인 후   
  ---python manage.py migrate
  ---python manage.py createsuperuser
  ---python manage.py runserver
<br>

<pre>
<code>
  # settings.py 상단에 아래 추가
  from pathlib import Path
  import os

  # 이 경우 BASE_DIR = BullentinProject
  TEMPLATES = [
      {
    'DIRS': [os.path.join(BASE_DIR, 'templates')],  
      }
  ]
</code>
</pre>
<br>

### 2) ./bulletin_board/models.py
<pre>
<code>
  from django.db import models
  from django.utils.timezone import now

  # Create your models here.
  class Bulletin(models.Model):
      title = models.CharField(max_length=100)
      content = models.CharField(max_length=2000)
      writeDate = models.DateTimeField(default=now, editable=False)
      name = models.CharField(max_length=50)
      passwd = models.CharField(max_length=50)

      def __str__(self):
          return self.title
</code>
</pre>
<br>

### 3) ./bulletin_board/admin.py
<pre>
<code>
  from django.contrib import admin
  from bulletin_board.models import Bulletin
  # Register your models here.

  admin.site.register(Bulletin)
</code>
</pre>

- Pycharm terminal   
  web-env 확인 후   
  ---python manage.py makemigrations  (스크립트 자동 생성)   
  ---python manage.py migrate  (scheme 변경된 내용 적용)
