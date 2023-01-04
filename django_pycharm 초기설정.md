## django 설치 및 세팅
### django - Pycharm - MariaDB   
jupyter notebook은 여러 개를 띄워서 작업하기에 불편하여 VSCode 또는 Pycharm 사용하기   
해당 글은 Pycharm 사용함   
Windows Terminal로 miniconda 설치 및 세팅은 [링크](https://github.com/Son-Sumin/ml_dl/blob/main/%EC%B4%88%EA%B8%B0%EC%84%A4%EC%A0%95.md) 참고

1. django 설치   
   - Windows Terminal   
     - 새로운 가상환경 만들기   
      --- conda activate   
      --- conda create -n web-env python=3.8   
      --- conda activate web-env   
      
    - [django](https://www.djangoproject.com/)   
      상단 'download' > 우측 'Previous releases' > Django 3.2.16 (LTS) 사용 예정으므로 확인   
    - [anaconda django](https://anaconda.org/anaconda/django) 명령어 확인   
      (web-env) 확인 후
      --- conda install -c anaconda django=3.2   

2. Pycharm 세팅   
   - Pycharm   
     상단 File > new project > 아래 사진 참고 > ok     
     ![pycharm1](https://user-images.githubusercontent.com/114986832/210559528-cc534c3b-bc70-4ab2-a474-f11c6ac8adf6.png)
     ![pycharm2](https://user-images.githubusercontent.com/114986832/210559581-72eedc49-1853-429b-afda-8741d7dee543.png)
     
     Windows PowerShell 확인 후   
     ---conda activate web-env   
  
     - django 프로젝트 만들기   
      ---django-admin startproject board .   
      ---python manage.py startapp bulletin_board   
      ---ls (상태 확인)
         * django-admin startproject 프로젝트이름 .(현재위치에)   
         * python manage.py startapp app이름   
         * 하나의 프로젝트 안에 여러 개의 application(ex. 인사, 재정 등) 존재함   
           앞으로 manage.py가 app 생성함   
           board라는 프로젝트 안에 bulletin_board app 있음   
           같은 레벨처럼 보이지만 project 안에 app이므로 주의!   
           ![1](https://user-images.githubusercontent.com/114986832/210558986-fc7118c5-1425-4dde-adb2-b19715b5c015.PNG)
           
 3. Pycharm 세팅  
           
