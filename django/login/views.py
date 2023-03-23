from django.shortcuts import render,HttpResponse
def login(request):
    return render(request,'LoginPage.html')
def landingPage(request):
    
    return render(request,'landingPage.html')
def instruction(request):
    return render(request,'instruction.html')