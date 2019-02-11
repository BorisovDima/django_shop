from django.contrib import admin
from .models import Product, Category, Brand, Variant


class AdminMixin:
    exclude = ['slug']



class VariantInline(admin.TabularInline):
    model = Variant
    extra = 0

def average_sales(product):
    return str(product.get_sales())

@admin.register(Product)
class ProductAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ('name', 'category', 'brand',  'average_price', 'features', average_sales)
    ordering = ['-variant__sales']
    inlines = [VariantInline]

    def save_related(self, request, form, formsets, change):
        form.save_m2m()
        f = formsets[0].save()
        if not formsets[0].queryset.exists() and not f:
            Variant.objects.create(product=form.instance, price=form.instance.average_price)



@admin.register(Category)
class CategoryAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Brand)
class BrandAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Variant)



