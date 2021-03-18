from django.contrib.auth import get_user_model
import  pandas as pd

def add_user(email):
    User = get_user_model()
    user=User.objects.create_user(email)
    user.username = email
    user.is_superuser=False
    user.is_staff=True
    user.is_active=True
    user.email = email
    user.set_password('andes123')
    user.save()


df = pd.read_csv('data-1615990888293.csv',sep=';')

for email in df.email:
    add_user(email)
    break
