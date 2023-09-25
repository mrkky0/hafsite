 

# Create your views here.
import json

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from app.models import Products,Category
from app.forms import SearchForm
from django.core.paginator import Paginator
from django.db.models import Q

# from app.models import Sale, Stats

def index(request):
    category = Category.objects.all()
    context = {'segment': 'index','category':category}
    html_template = loader.get_template('index.html')
 
    return HttpResponse(html_template.render(context, request))


 

def about(request):
    context = {'segment': 'about'}
    html_template = loader.get_template('about.html')

    return HttpResponse(html_template.render(context, request))


def products(request):
    category = Category.objects.all()
    data = Products.objects.all()
    query = request.GET.get('q')
    data_list = []
    
    if query:
        data_list = data.filter(Q(product_name__icontains=query) | Q(product_category__icontains=query)|Q(default_tag__icontains=query))
    
    
    context = {'segment': 'products','data':data,'category':category,'data_list':data_list}
    html_template = loader.get_template('products.html')
    
    
    return HttpResponse(html_template.render(context, request))


def detail(request,id):
    
    data = get_object_or_404(Products,pk=id)
    context = {'segment': 'detail','data':data}
    html_template = loader.get_template('detail.html')

    return HttpResponse(html_template.render(context, request))




def contact(request):
    context = {'segment': 'contact'}
    html_template = loader.get_template('contact.html')

    return HttpResponse(html_template.render(context, request))


def other(request):
    data = Products.objects.all()
    context = {'segment': 'other','data':data}
    html_template = loader.get_template('other.html')
    
    
    return HttpResponse(html_template.render(context, request))

def debug(request):
    
     
    product_list = Products.objects.all()
    query = request.GET.get('q')
    if query:
        product_list = product_list.filter(product_name__icontains =query)
        
    paginator = Paginator(product_list,5)
    
        
    context = {'products_data':product_list } 
    html_template = loader.get_template('debug.html')
    return HttpResponse(html_template.render(context, request))


# def charts_file(request):
#     context = {'segment': 'charts_from_file'}
#     html_template = loader.get_template('charts-from-file.html')

#     with open('sample_data/chart_morris.json', 'r') as f:
#         context['chart_data'] = json.dumps(json.load(f))

#     return HttpResponse(html_template.render(context, request))    

# def charts_input(request):
#     context = {'segment': 'charts_from_input'}
#     html_template = loader.get_template('charts-from-input.html')

#     # -----------------------------------------------
#     # Use data from STATS Table
#     # -----------------------------------------------

#     stats, labels = Stats.get_report()
#     data = [
#         {
#             'y': year,
#             'a': '{:.2f}'.format( stats[year].get('prod1_sales') ), 
#             'b': '{:.2f}'.format( stats[year].get('prod2_sales') ), 
#             'c': '{:.2f}'.format( stats[year].get('prod3_sales') )  
#         } for year in stats
#     ]

#     context['chart_data'] = json.dumps({
#         'element': 'morris-bar-chart',
#         'data': data,
#         'xkey': 'y',
#         'barSizeRatio': 0.70,
#         'barGap': 3,
#         'resize': True,
#         'responsive': True,
#         'ykeys': ['a', 'b', 'c'],  # it can be custom
#         'labels': labels,
#         'barColors': ['0-#1de9b6-#1dc4e9', '0-#899FD4-#A389D4', '#04a9f5']  # it can be custom
#     })

#     return HttpResponse(html_template.render(context, request))

# def charts_load(request):
#     context = {'segment': 'charts_from_load'}
#     html_template = loader.get_template('charts-from-load.html')

#     # -----------------------------------------------
#     # Extract data from Sale table 
#     # -----------------------------------------------

#     sales, labels = Sale.get_sales_report()
#     data = [
#         {
#             'y': year,
#             'a': '{:.2f}'.format(sales[year].get('A')),
#             'b': '{:.2f}'.format(sales[year].get('B')),
#             'c': '{:.2f}'.format(sales[year].get('C'))
#         } for year in sales
#     ]

#     context['chart_data'] = json.dumps({
#         'element': 'morris-bar-chart',
#         'data': data,
#         'xkey': 'y',
#         'barSizeRatio': 0.70,
#         'barGap': 3,
#         'resize': True,
#         'responsive': True,
#         'ykeys': ['a', 'b', 'c'],  # it can be custom
#         'labels': labels,
#         'barColors': ['0-#1de9b6-#1dc4e9', '0-#899FD4-#A389D4', '#04a9f5']  # it can be custom
#     })

#     return HttpResponse(html_template.render(context, request))


 

# def home(request):
#     context = {'segment': 'home'}
#     html_template = loader.get_template('home.html')
    
#     return HttpResponse(html_template.render(context, request))

# def about_us(request):
#     context = {'segment': 'about-us'}
#     html_template = loader.get_template('about-us.html')
    
#     return HttpResponse(html_template.render(context, request))

# def product(request):
    
#     category = ["acat","bcat","ccat"]
     
#     data = Sale.objects.all()
#     return render(request, 'product.html', {'data':data,'category':category})
    
# def spe_product(request,product_id):
       
#     data = get_object_or_404(Sale,pk=product_id)
#     return render(request, 'spe-product.html', {'data':data})
     
        
    
    
       
    
    

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('500.html')
        return HttpResponse(html_template.render(context, request))