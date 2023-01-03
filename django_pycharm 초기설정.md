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
