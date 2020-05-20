from django.contrib.auth import get_user_model
import os

User = get_user_model()
User.objects.create_superuser('admin', os.getenv("EMAIL"), os.getenv("MYSQL_ROOT_PASSWORD"))