from django.urls import path
from store import views

urlpatterns = [
    path('home/',views.homeview.as_view(),name='home'),
    path('category/<int:pk>',views.Category_detail.as_view(),name='cat'),
    path('pdetail/<int:pk>',views.product_detail.as_view(),name="pdet"),
    path('addcart/<int:pk>',views.addcartview.as_view(),name="acart"),
    path('delete/<int:pk>',views.deletecartview.as_view(),name="del"),
    path('register/',views.userregisterview.as_view(),name="reg"),
    path('login/',views.signinview.as_view(),name="login"),
    path('logout/',views.singoutview.as_view(),name="logout"),
    path('cartdetail/',views.usercartdetailview.as_view(),name="cartd"),
    path('order/<int:pk>',views.userorderedview.as_view(),name="ord"),
    path('orderview/',views.orderitemsview.as_view(),name="ordv"),
    path('search/',views.Searchview.as_view(),name="search"),
    path('buy/<int:pk>/', views.BuyingView.as_view(), name='buy'),
    path('order/success/', views.order_success, name='order_success'),
    path('buy/<int:pk>/', views.BuyingView.as_view(), name='buy_product'),  # Use the correct view class
   ]

