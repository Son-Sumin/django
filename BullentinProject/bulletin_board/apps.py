from django.apps import AppConfig

# startapp 할 때마다 자동으로 추가가 됨

class BulletinBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bulletin_board'
