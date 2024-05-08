from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.views import View
import json
from django.http import JsonResponse

# Create your views here.

class RegistrationView(View):

    def get(self,request):
         return render(request,'authenticate/register.html')
    
    def post(self,request):
        #get field values
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        

        context={

        'fieldValues':request.POST
        }
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request,'!!! password must be at least 6 characters')
                    return render(request,'authenticate/register.html',context)
                        
                user=User.objects.create_user(username=username,email=email,password=password)
                user.set_password(password)
                user.save()

                messages.success(request,'Account has been created succesfully')
                
                return redirect('login')
            else:
                    messages.error(request,'!! email exist')
                    return render(request,'authenticate/register.html',context)


      
        

        messages.error(request,'!! username exist')
        return render(request,'authenticate/register.html',context)



class LoginView(View):

    def get(self,request):
         return render(request,'authenticate/login.html')
    def post(self,request):
        #get form values
        username=request.POST['username']
        password=request.POST['password']
        if username and password:
            user=auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                messages.success(request,'welcome back '+ username)
                return redirect('stock-list')
            else:
               
                messages.warning(request,'invalid username or password ')
                return render(request,'authenticate/login.html')
        return render(request,'authenticate/login.html')

    
class UsernameValidationView(View):
    def post(self,request):
        #get the data from the form
        data=json.loads(request.body)
        username=data['username']

        if not str(username).isalnum():
            return JsonResponse({"username_error":"Username should only contain alphanumeric charecters"})
        if User.objects.filter(username=username):
            return JsonResponse({"username_error":"Username exist!!!"})
        return JsonResponse({"username":True})

class EmailValidationView(View):
    def post(self,request):
        #get data from the form
        body=json.loads(request.body)
        email=body['email']
        if User.objects.filter(email=email):
            return JsonResponse({"email_error":"email already exist"})
        return JsonResponse({"email":True})


class LogoutView(View):
    def get(self,request):
        auth.logout(request)
        return redirect('login')