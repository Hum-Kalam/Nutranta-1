# Generated by Django 4.2.1 on 2023-05-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutranta_app', '0003_remove_product_discounted_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('vegetables', 'vegetables'), ('fruits', 'fruits'), ('dairy', 'dairy'), ('fish', 'fish'), ('eggs', 'eggs'), ('bread', 'bread'), ('cereal', 'cereal'), ('rice', 'rice'), ('pasta', 'pasta'), ('nuts', 'nuts'), ('beans', 'beans'), ('oil', 'oil'), ('butter', 'butter'), ('margarine', 'margarine'), ('salad dressing', 'salad dressing'), ('sugar', 'sugar'), ('honey', 'honey'), ('jam', 'jam'), ('jelly', 'jelly'), ('syrup', 'syrup'), ('cookies', 'cookies')], max_length=50),
        ),
    ]