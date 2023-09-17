#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import ContactForm,RegisterUserForm,PasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
# Create your views here.
import requests,time,datetime
from .models import StudentContact
from .models import StudentContact,CompoundV

def run_query(q):
    request = requests.post('https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))
query = """
    {
    markets(first: 7) {
    borrowRate
    cash
    collateralFactor
    exchangeRate
    interestRateModelAddress
    name
    reserves
    supplyRate
    symbol
    id
    totalBorrows
    totalSupply
    underlyingAddress
    underlyingName
    underlyingPrice
    underlyingSymbol
    reserveFactor
    underlyingPriceUSD
  }
}
"""


def LoginStudent(request):
    if request.method=="POST":
        user_email=request.POST['email']
        password=request.POST['password']
        try:
            usernames = User.objects.get(email=user_email)
            user=authenticate(request,username=usernames.username,password=password)
            if user is not None :
                login(request,user)
                return redirect('dashboard')
            else:
                messages.success(request,('There was an error logging in, check credential and TRY AGAIN...'))
                return redirect('Studentlogin')
        except User.DoesNotExist:
            pass
    else:
        return render(request,'login.html',{})

def signup(request):
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        contactform =  ContactForm(request.POST)
        if form.is_valid() and contactform.is_valid():
            form.save()
            edith=  contactform.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            edith.user = request.user
            edith.save()
            messages.success(request,('Account created successfully...'))
            return redirect('dashboard')
        else:
            messages.success(request,"An Error Occured..... ")
    else:        
        form = RegisterUserForm() 
        contactform = ContactForm()      
    return render(request,'signup.html',{'form':form,"form2":contactform})

def log_outStudent(request):
    logout(request)
    return redirect('studentlogin')


def Dashboard(request):
    if request.user.is_authenticated == True:
        i=1
        result = run_query(query)
        for obj in result["data"].values():
            for i in range(1,7):
                #pprint(obj[i]['id'])
                populateDB = CompoundV.objects.create(borrowRate=str(obj[i]['borrowRate']),
                                                        cash=obj[i]['cash'],
                                                        collateralFactor=obj[i]['collateralFactor'],
                                                        exchangeRate=obj[i]['exchangeRate'],
                                                        interestRateModelAddress=obj[i]['interestRateModelAddress'],
                                                        name=obj[i]['name'],
                                                        reserves=obj[i]['reserves'],
                                                        supplyRate=obj[i]['supplyRate'],
                                                        symbol=obj[i]['symbol'],
                                                        ids=obj[i]['id'],
                                                        totalBorrows=obj[i]['totalBorrows'],
                                                        totalSupply=obj[i]['totalSupply'],
                                                        underlyingAddress=obj[i]['underlyingAddress'],
                                                        underlyingName=obj[i]['underlyingName'],
                                                        underlyingPrice=obj[i]['underlyingPrice'],
                                                        underlyingSymbol=obj[i]['underlyingSymbol'],
                                                        reserveFactor=obj[i]['reserveFactor'],
                                                        underlyingPriceUSD=obj[i]['underlyingPriceUSD']
                                                    )
                populateDB.save()
        data = CompoundV.objects.all()
        for dates in data:
            tnow = datetime.datetime.now()
            tdata_b = dates.dateCreated
            delta = tnow - tdata_b.replace(tzinfo=None)
            minute = (delta.total_seconds())/(60)
            if minute > 5:
                dates.delete()
        supply = list([round(float(obj.totalSupply)) for obj in data])
        reserve = list([round(float(obj.reserves)) for obj in data])
        borrow = list([round(float(obj.totalBorrows)) for obj in data])
        supplyrate = sum(list([float(obj.supplyRate) for obj in data]))
        cash = list([round(float(obj.cash)) for obj in data])
        totalQuery = len(borrow)
        fetchtime = time.strftime("%H:%M:%S",time.localtime())
        totalObject = totalQuery*18
        tablename = [obj.name for obj in data]
        content= {"supply":supply,"data":data,"supplyrate":supplyrate,"time":fetchtime,
                  "reserve":reserve,"borrow":borrow,"totalQuery":totalQuery,
                  "tablename":tablename,"totalObject":totalObject,"cash":cash}
        return render(request,"index.html",content)
    else:
        messages.success(request,"please login")
        return redirect("studentlogin")
    
