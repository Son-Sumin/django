## django 설치 및 세팅
### django - Pycharm - MariaDB   
jupyter notebook은 여러 개를 띄워서 작업하기에 불편하여 VSCode 또는 Pycharm 사용하기   
해당 글은 Pycharm 사용함   
Windows Terminal로 miniconda 설치 및 세팅은 [링크](https://github.com/Son-Sumin/ml_dl/blob/main/%EC%B4%88%EA%B8%B0%EC%84%A4%EC%A0%95.md) 참고

#### 1. django 설치   
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

#### 2. Pycharm 세팅   
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
           
#### 3. MariaDB 세팅  
  - mysql   
    root DB 확인 후 아래 실행 > 아래 실행 완료 후 메인 페이지에서 MySQL Connections 생성      
       
      <pre>
      <code>
         -- db생성
         create database django_db default character set utf8mb4;

         -- 계정 생성
         -- localhost: 설치한 컴퓨터 / %: anyhost, 방화벽만 뚫어주면 누구나 접근 가능
         create user 'django'@'%' identified by '1234';
         create user 'django'@'localhost' identified by '1234';

         -- 권한 부여
         grant all privileges on django_db.* to 'django'@'%';
         grant all privileges on django_db.* to 'django'@'localhost';

         -- 캐싱되어 있을 수 있으니 실시
         flush privileges;
      </code>
      </pre>

#### 4. ORM 사용 예정 
  - app과 db 인터페이스 시 둘을 연결하여 접근할 수 있게 하는 persistence API 필요(ex. JPA)   
     * 방법1) SQL mapping - mybatis   
     * 방법2) ORM(Object Relational Mapping)
              django는 default로 ORM 제공   
              객체를 생성하여 해당 필드 내용을 객체에 담아 갖고 오는 방법(getter/setter)

<br/><br/>
**향후 scheme 변경 시(column, table 등 관련) 반드시 ORM 통해 변경해야함**   
**아니면 django와 내용 불일치로 인한 충돌 발생함(data CRUD는 )**
