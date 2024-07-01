from app.models.product import Product
import json

def add_product(product_data):
    product = Product(**product_data)
    product.save()
    return {'message': 'Product added successfully', 'id': str(product.id)}

def get_product(product_id):
    product = Product.objects(id=product_id).first()
    if product:
        return product.to_json()
    else:
        return {'message': 'Product not found'}

def get_all_products():
    products = Product.objects().all()
    data = [product.to_json() for product in products]
    return data, 200

def update_product(product_id, data):
    try:
        product = Product.objects.get(id=product_id)
        product.update(**data)
        return {'message': 'Product updated successfully'}
    except Product.DoesNotExist:
        return {'error': 'Product not found'}

def delete_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return {'message': 'Product deleted successfully'}
    except Product.DoesNotExist:
        return {'error': 'Product not found'}
