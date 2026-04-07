import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pgstats", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="indexstats",
            name="stats",
            field=models.JSONField(
                encoder=django.core.serializers.json.DjangoJSONEncoder
            ),
        ),
        migrations.AlterField(
            model_name="tablestats",
            name="stats",
            field=models.JSONField(
                encoder=django.core.serializers.json.DjangoJSONEncoder
            ),
        ),
    ]
