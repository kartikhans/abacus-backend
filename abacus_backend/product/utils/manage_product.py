from product.models import Product
from rest_framework import status


def add_product(data):
    name = data.get('name')
    description = data.get('description')
    category = data.get('category').upper()
    price = data.get('price')
    product_obj = Product.objects.filter(name=name, category=category).first()
    if not product_obj:
        product_obj = Product(name=name, description=description, price=price, category=category)
        product_obj.save()
        result = dict(result='PRODUCT_CREATED_SUCCESSFULLY', product_pid=str(product_obj.uid),
                      status=status.HTTP_200_OK)
    else:
        result = dict(result='PRODUCT_ALREADY_PRESENT', product_pid=str(product_obj.uid),
                      status=status.HTTP_400_BAD_REQUEST)
    return result


def update_product(data):
    uid = data.get('uid')
    name = data.get('name')
    description = data.get('description')
    category = data.get('category')
    price = data.get('price')
    is_deleted = data.get('is_deleted')
    product_obj = Product.objects.filter(uid=uid).first()
    if product_obj:
        product_obj.name = name
        product_obj.description = description
        product_obj.category = category
        product_obj.price = price
        product_obj.is_deleted = is_deleted
        product_obj.save()
        result = dict(result='PRODUCT_UPDATED_SUCCESSFULLY', product_uid=uid, status=status.HTTP_200_OK)
    else:
        result = dict(result='PRODUCT_NOT_FOUND', product_obj=uid, status=status.HTTP_400_BAD_REQUEST)
    return result


def view_product(data):
    uid = data.get('uid')
    product_obj = Product.objects.filter(uid=uid).first()
    if product_obj:
        product_dict = {'name': product_obj.name, 'description': product_obj.description,
                        'category': product_obj.category, 'price': product_obj.price, 'tag': product_obj.tag,
                        'is_deleted': product_obj.is_deleted}
        result = dict(result=product_dict, product_uid=uid, status=status.HTTP_200_OK)
    else:
        result = dict(result='PRODUCT_NOT_FOUND', product_obj=uid, status=status.HTTP_400_BAD_REQUEST)
    return result


def view_all_product():
    product_objs = Product.objects.filter(is_deleted=False)
    final_list = []
    for product_obj in product_objs:
        product_dict = {'name': product_obj.name, 'description': product_obj.description,
                        'category': product_obj.category, 'price': product_obj.price, 'tag': product_obj.tag}
        final_list.append(product_dict)
    result = dict(result=final_list, status=status.HTTP_200_OK)
    return result
