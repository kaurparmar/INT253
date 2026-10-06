from unicodedata import name
from .forms import MyForm
from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token
# Create your views here.

def my_view(request):
    return HttpResponse("Hello, World!")

def base(request):
    return render(request, 'base.html')
def home(request):
    results=[
        {"Subject":"Data Structures","Grade":'A',"Status":"Pass"},
        {"Subject":"Web Technologies","Grade":'B+',"Status":"Pass"},
        {"Subject":"DBMS","Grade":"A","Status":"Pass"},
    ]

    return render(request,'home.html',{'results':results})

def about(request):
    studentDetails={"name":"Catherine","rollNo":101,"Stream":"CSE","Section":"Tulip"}
    
    return render (request,'about.html',{'details':studentDetails})

def items(request):
    item="chips"
    return HttpResponse(f"<h1 style='color: green;'>Welcome to the Items Page</h1><h3 style='color: red;'>Item: {item}</h3>")


def itemsList(request):
    items = {"chips":"It is 10", "cookies":"It is 15", "soda":"It is 5", "candy":"It is 2"}
    content="<h1>Items are </h1>"
    for item, description in items.items():
        content += f"<li>{item}: {description}</li>"
    return HttpResponse(content)


def marks(request, mark):
    return HttpResponse(f"<h1 style='color: purple;'>The mark is: {mark}</h1>")


def user_profile(request, username):
    return HttpResponse(f"<h1 style='color: orange;'>User Profile for: {username}</h1>")


def Products(request, productId):
    return HttpResponse(f"<h1 style='color: brown;'>Welcome to the Products Page</h1><p>Product ID: {productId}</p>")




def menu(request):
    menuItem1={'name':'Pizza','price':10.99,'description':'Delicious cheese pizza with fresh ingredients.'}
    # menuItem2={'name':'Burger','price':8.99,'description':'Juicy beef burger with lettuce, tomato, and cheese.'}
    # menuItem3={'name':'Pasta','price':12.99,'description':'Classic Italian pasta with marinara sauce and parmesan cheese.'}
    # items=[menuItem1,menuItem2,menuItem3]
    return render(request,'menu.html',{'menuItem':menuItem1})

def menu1(request):
        menuItem1={'name':'Pizza','price':10.99,'description':'Delicious cheese pizza with fresh ingredients.'}
        menuItem2={'name':'Burger','price':8.99,'description':'Juicy beef burger with lettuce, tomato, and cheese.'}
        menuItem3={'name':'Pasta','price':12.99,'description':'Classic Italian pasta with marinara sauce and parmesan cheese.'}
        items=[menuItem1,menuItem2,menuItem3]
        return render(request,'menu1.html',{'items':items})

def baseAbout(request):
    return render(request,'baseAbout.html')




def restaurantHome(request):
    return render(request, 'restaurantHome.html')

def restaurantAbout(request):
    return render(request, 'restaurantAbout.html')

def restaurantMenu(request):
    menu_items = [
        {'name': 'Pizza', 'price': 10.99, 'description': 'Delicious cheese pizza with fresh ingredients.'},
        {'name': 'Burger', 'price': 8.99, 'description': 'Juicy beef burger with lettuce, tomato, and cheese.'},
        {'name': 'Pasta', 'price': 12.99, 'description': 'Classic Italian pasta with marinara sauce and parmesan cheese.'},
    ]
    return render(request, 'restaurantMenu.html', {'menu_items': menu_items})

def simpleForm(request):
    csrf_token=get_token(request)
    if(request.method=="POST"):
        textbox1=request.POST.get("textbox1")
        textbox2=request.POST.get("textbox2")
        return HttpResponse("The names are {textbox1} and {textbox2}")
    else:

        return HttpResponse(
            """
            <form method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <label for="testbox1">Text Box 1</label><br>
            <input type="text" id="textbox1"><br>
            <label for="testbox2">Text Box 2</label><br>
            <input type="text" id="textbox2"><br>
            <button type="submit" value="Submit">Submit</button>
            </form>
            """
    )

def templateForm(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if name and email and password:
            return HttpResponse(f"Form submitted successfully!")
        
    
    return render(request, 'form.html')

def formValidation(request):
    form =MyForm()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        day = request.POST.get("day")
        month = request.POST.get("month")
        year = request.POST.get("year")

        errors = []
        if not name:
            errors.append("Name is required.")
        if not email:
            errors.append("Email is required.")
        if not password:
            errors.append("Password is required.")
        if password != confirm_password:
            errors.append("Passwords do not match.")
        if not day or not month or not year:
            errors.append("Date of birth is required.")

        if errors:
            return render(request, 'form_validation.html', {'errors': errors})
        
        return HttpResponse(f"Form submitted successfully!")

    return render(request, 'signup.html',{'form':form})