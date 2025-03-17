from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from store.models import Category,Product,cart,Order
from store.forms import userregisterform,userloginform,userorderform
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class homeview(ListView):
    model = Category
    template_name = "store\index.html"
    context_object_name = "categories"  
    

class registerview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"store\register.html") 

class Category_detail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.filter(category_id=id)
        name=Category.objects.get(id=id)
        return render(request,"store/category_detail.html",{"data":data,"name":name})
    
class product_detail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        return render(request,"store/p_detail.html",{"data":data})
    
class userregisterview(CreateView):
    template_name = "store/reg.html"
    form_class = userregisterform
    model = User
    success_url = reverse_lazy("home")  

class signinview(View):
    def get(self,request,*args,**kwargs):
        x=userloginform()
        return render(request,"store/login.html",{"form":x}) 
    

    def post(self,request,*args,**kwargs):
        x=userloginform(request.POST)
        if x.is_valid():
            print(x.cleaned_data)
            u_name=x.cleaned_data.get("username")
            pwd=x.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("home")
            else:
                print("kickout")   
        return redirect("reg")         
     

class singoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")
    
class addcartview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        cart.objects.create(item=data,user=request.user)
        print("added succesfully")
        return redirect("home")

class deletecartview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cart.objects.get(id=id).delete()
        return redirect("home")
    

@method_decorator(signin_required, name="dispatch")   
class usercartdetailview(View):
    def get(self, request, *args, **kwargs):
        data = cart.objects.filter(user=request.user)
        total_price = sum(item.item.selling_price * item.qty for item in data)
        return render(request, "store/cart.html", {"data": data, "total_price": total_price}) 



class userorderedview(View):
    def get(self,request,*args,**kwargs):
        form=userorderform()
        return render (request,"store/orderpage.html",{"form":form})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")        
        data=Product.objects.get(id=id)
        form=userorderform(request.POST)
        if form.is_valid():
            qs=form.cleaned_data.get("address")
            Order.objects.create(address=qs,orderitem=data,customer=request.user)
            return redirect("home")
        return redirect("acart")
    
@method_decorator(signin_required,name="dispatch") 
class orderitemsview(View):
    def get(self,request,*args,**kwargs):
        data=Order.objects.filter(customer=request.user)
        return render(request,"store/orderview.html",{"data":data}) 


class Searchview(View):
    def get(self,request,*args,**kwargs):
        query=request.GET.get('q')
        if query:
            result = Product.objects.filter(name__icontains=query)

        else:
            result = None

        return render(request,"store/search.html",{"result":result})   


@method_decorator(signin_required,name="dispatch") 
class BuyingView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Product.objects.get(id=id)
        form = userorderform()
        return render(request, "store/buy.html", {"product": product, "form": form})
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Product.objects.get(id=id)
        form = userorderform(request.POST)
        
        if form.is_valid():
            address = form.cleaned_data.get("address")
            order = Order.objects.create(
                orderitem=product,
                customer=request.user,
                address=address,
                price=product.selling_price
            )
            return redirect("order_success")
        
        return render(request, "store/buy.html", {"product": product, "form": form})
    

from django.shortcuts import render

def order_success(request):
    return render(request, 'store/order_success.html')

def buy_product(request, product_id):
    if request.method == "POST":
        return redirect('order_success')
    return render(request, 'store/buy.html', {'product': product_id})

