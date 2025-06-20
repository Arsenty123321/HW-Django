from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """
        Получает данные из кэша, если пуст, то кеширует возврат из БД.
    """

    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)

    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products, 60 * 15)
    return products
