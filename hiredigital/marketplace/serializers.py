import datetime

from rest_framework.serializers import ModelSerializer

from marketplace.models import Products, ProductCategory


class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductsSerializer(ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields = ('created_date', 'updated_date', 'created_by')

    def validate_product_price(self, v):
        return round(v, 2)

    def validate_selling_price(self, v):
        return round(v, 2)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['user']
        return super().create(validated_data)

    def save(self, **kwargs):
        kwargs['updated_date'] = datetime.datetime.now()
        return super().save(**kwargs)
