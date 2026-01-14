from django.urls import path
from app import views

urlpatterns = [
    path('category', views.ParentCategoryListApiView.as_view()),
    path('category/<slug:slug>/', views.ChildrenCategoryByCategorySlug.as_view()),
    path('category/<slug:slug>/<slug:child_slug>/', views.ProductListByChildCategorySlug.as_view()),
    path('category/create/', views.CategoryCreateApiView.as_view()),
    path('create/product/', views.ProductCreateApiView.as_view()),
    path('products/', views.ProductListAPiView.as_view()),
]
