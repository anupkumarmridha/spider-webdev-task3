"""exhabition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home import views
from home.views import homeView, UserPasswordChangeView, UserEditView,UserProfileView, AddProfileDetailsView
from home.productViews import AddPostView,BidView ,AddComment ,UpdatePostView,ProductDetailsView,DeletePostView,AddCategoryView, CategoryView, CategoryListView, LikeView
urlpatterns = [
    path('', homeView.as_view(), name='homeView'),
    
    #Product Url
    path('Add_Product/', AddPostView.as_view(), name='Add_Product'),
    path('add_comment/<int:pk>', AddComment, name='add_comment'),
    path('bid_product/<int:pk>', BidView, name='bid_product'),
    path('Product/<int:pk>', ProductDetailsView.as_view(), name='Product_Details'),
    path('Product/Edit/<int:pk>', UpdatePostView.as_view(), name='Update_Product'),
    path('Product/Delete/<int:pk>', DeletePostView.as_view(), name='Delete_Product'),
    path('Add_Category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('categoroy_list',CategoryListView , name='category_list'),
    path('like_product/<int:pk>',LikeView , name='like_product'),
    
    #Regestration    
    path('signup/', views.handelSingup, name='handelSingup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    
    #edit profile
    path("view_profile/<int:pk>", UserProfileView.as_view(), name='View_Profile'),
    path("edit_profile", UserEditView.as_view(), name='Edit_Profile'),
    path("add_profile_details/", AddProfileDetailsView.as_view(), name='Add_Profile_Details'),
    path("password/",UserPasswordChangeView.as_view(), name='password_change'),
    #path("Delete_Profile",DeleteUserProfileView.as_view(), name='Delete_Profile'),
]
