from django.core.management import BaseCommand

from site_app.models import Product
from site_app.serializers import ProductSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start demo renderer #1'))

        product = Product.objects.all()
        serializer = ProductSerializer(instance=product, many=True)
        print("Serializer:", serializer)
