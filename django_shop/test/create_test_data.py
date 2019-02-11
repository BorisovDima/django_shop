#
# from shop.apps.core.models import Product, Variant, Brand, Category
# from django.core.files.base import ContentFile
# import random
# image = open('/home/borisov/Downloads/preview.jpeg','rb').read()
# image = ContentFile(image)
# for i in range(200):
#       category = random.choice(Category.objects.all())
#       brand = random.choice(Brand.objects.all())
#       product = Product.objects.create(category=category, brand=brand,
#                                        name='test product N %s' % i, average_price=(i+1)*2,
#                                        description='Test description N %s' % i, features='Test features N %s' % i)
#       product.image.save('test_photo%s.jpg' % i, image)
#       product.image2.save('test_photo%s.jpg' % i, image)
#       product.image3.save('test_photo%s.jpg' % i, image)
#       for i in range(1, 6):
#            ch = ['S', 'M', 'L', 'XL','2XL', '3XL',  '4XL',]
#            var = Variant.objects.create(product=product, count=i*3, price=20*i, size=ch[i])
#
