from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .metrics import get_product_metrics, get_sales_metrics, get_daily_sales_data, get_daily_sales_quantity_data, get_graphic_product_category_metric, get_graphic_product_brand_metric
import json


@login_required(login_url='login')
def home(request):
    product_metrics = get_product_metrics()
    sales_metrics = get_sales_metrics()
    daily_sales_data = get_daily_sales_data()
    graphic_product_category_metric = get_graphic_product_category_metric()
    graphic_product_brand_metric = get_graphic_product_brand_metric()
    daily_sales_quantity_data = get_daily_sales_quantity_data()
    

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
    }


    return render(request, 'home.html', context)