from django.urls import path, re_path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Charts Views Routing

    # Charts from file
    # path('charts-file'  , views.charts_file , name='charts-file'  ),
    # path('charts-input' , views.charts_input, name='charts-input' ),
    # path('charts-load'  , views.charts_load,  name='charts-load'  ),
    
    # path('home'  , views.home,  name='home'  ),
    # path('about-us'  , views.about_us,  name='about-us'  ),
    # path('product'  , views.product,  name='product'  ),
    # path('spe-product/<product_id>'  , views.spe_product,  name='spe-product'  ),
     
    

    # The home page
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('product', views.products, name='product'),
    path('details/<int:id>', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('debug', views.debug, name='debug'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
 