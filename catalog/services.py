from django.core.cache import cache

from catalog.models import Product, Category
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

def get_categories_from_cache():
    """
        Получает данные из кэша, если пуст, то кеширует возврат из БД.
    """

    if not CACHE_ENABLED:
        return Category.objects.all()

    key = "category_list"
    categories = cache.get(key)

    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories, 60 * 15)
    return categories

def get_products_from_category(category_id):
    """
        Возвращает список продуктов из категории.
    """

    return Product.objects.filter(category_id=category_id)
