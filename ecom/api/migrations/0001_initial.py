from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="tian8689",
            email="xiaotian8689@yahoo.com",
            is_staff=True,
            is_superuser=True,
            phone="2402779269",
            gender="Male"
            )
        
        user.set_password("Tian1977")
        user.save()

    dependencies = []

    operations = [
        migrations.RunPython(seed_data),
    ]