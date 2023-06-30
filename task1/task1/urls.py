"""
URL configuration for task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from testapp import  views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.CategorycreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryupdateAPIView.as_view(), name='category-update'),
    path('categories/<int:pk>/', views.CategorydeleteAPIView.as_view(), name='category-delete'),
    path('products/', views.ProductCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductUpdateAPIView.as_view(), name='product-update'),
    path('products/<int:pk>/', views.ProductDestroyAPIView.as_view(), name='product-delete'),
]
