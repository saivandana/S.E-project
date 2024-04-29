#product description including the name, description.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20230322_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
    ]
