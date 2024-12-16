from django.urls import path
from .views import store_home, product_details, register, calc_total_price_per_user_selection

app_name = "store"
urlpatterns = [
    path('', store_home, name="store_home"),
    path('<slug:slug>', product_details, name="product_details"),
    path('register/', register, name='register'),
    path('register/<str:tut_name>', register, name='register_specific'),
    path('selection_price/', calc_total_price_per_user_selection, name='calc_total_price_per_user_selection'),

]
