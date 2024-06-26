# Generated by Django 5.0.4 on 2024-04-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_cart', '0002_remove_menuitem_toppings_remove_cartitem_toppings_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='menu_cart.topping'),
        ),
    ]
