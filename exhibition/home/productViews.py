from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render, redirect
from home.forms import PostProductForm, EditProductForm
from home.models import Product,Category, Comment, Bid
from home.views import homeView

class AddPostView(CreateView):
    model=Product
    form_class=PostProductForm
    template_name='product/add_product.html'

def BidView(request,pk):
    if request.method=='POST':
        bid_price=request.POST.get("bid_price")
        author=request.user
        productId=request.POST.get("productId")
        
        product=Product.objects.get(pk=productId)
        bid_price=Bid(bid_price=bid_price, author=author, product=product)
        bid_price.save()
        messages.success(request, "your Bid has successfully added")
        return redirect(reverse('Product_Details', args=[str(pk)]))

def AddComment(request,pk):
    if request.method=="POST":
        comment=request.POST.get("comment")
        author=request.user
        productId=request.POST.get("productId")

        product=Product.objects.get(pk=productId)
        comment=Comment(body=comment, author=author, product=product)
        comment.save()
        messages.success(request, "your comment has successfully added 🥰")
        return redirect(reverse('Product_Details', args=[str(pk)]))

class ProductDetailsView(DetailView):
    model=Product
    template_name='product/product_details.html'

    def get_context_data(self, *args, **kwargs):
        context=super(ProductDetailsView, self).get_context_data(*args, **kwargs)
        product_post = get_object_or_404(Product, id=self.kwargs['pk'])
        liked=False
        if product_post.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        total_likes=product_post.total_likes()
        context['total_likes']=total_likes
        context['liked']=liked
        return context
    


def LikeView(request,pk):
    product_post=get_object_or_404(Product, id=request.POST.get('product_id'))
    liked=False
    if product_post.likes.filter(id=request.user.id).exists():
        product_post.likes.remove(request.user)
        liked=False
    else:
        product_post.likes.add(request.user)
        liked=True
    return redirect(reverse('Product_Details', args=[str(pk)]))

class UpdatePostView(UpdateView):
    model=Product
    form_class=EditProductForm
    template_name='product/update_product.html'

class DeletePostView(DeleteView):
    model=Product
    template_name='product/delete_product.html'
    success_url=reverse_lazy('homeView')

class AddCategoryView(CreateView):
    model=Category
    template_name='product/add_category.html'
    fields='__all__'

def CategoryView(request, cats):
    category_posts=Product.objects.filter(category=cats.replace('_', ' '))
    return render(request, 'product/categories.html',{'cats':cats.replace('_',' ').title(),'category_posts':category_posts})


def CategoryListView(request):
    cats_menu_list=Category.objects.all()
    return render(request, 'product/categories_list.html', {'cats_menu_list':cats_menu_list})