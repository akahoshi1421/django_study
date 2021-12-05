from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse, JsonResponse
from django_study.models import Tweet
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def top(request):
    data = {
        "test": "ジャスティス！！",
    }
    l = [1, 2, 3, 4 , 5, 6, 7]
    result = []
    for n in l:
        if n % 2 == 0:
            result.append("いえーい!!")
        else:
            result.append(n)
    
    data["test2"] = result

    return render(request, "index.html", data)

def topRedirect(request):
    return redirect("top")

def number(request, number_id):
    return HttpResponse(number_id)

def top2(request):
    return HttpResponse("Hello World!(その2)")

def form(request):
    data = {}
    if request.method == "POST":
        if "content" in request.POST:
            content = request.POST["content"]
            data["result"] = mark_safe(content)
        return render(request, "form.html", data)

    else:
        return render(request, "form.html", data)

def tweets(request):
    if not "logined" in request.session:
        return redirect("login")

    data = {}
    if request.method == "POST":
        user = request.POST["user"]
        content = request.POST["content"]
        result = Tweet(user = user, content = content)
        result.save()
    
    
    tweets_result = Tweet.objects.all()
    data["tweets_result"] = tweets_result
    return render(request, "tweets.html", data)

def search(request):
    data = {}
    if request.method == "POST":
        content = request.POST["search"]
        try:
            result = Tweet.objects.get(id = content)
            data["result"] = result
        except:
            pass
    return render(request, "result.html", data)

def search2(request):
    data = {}
    if request.method == "POST":
        content = request.POST["user_search"]

        if "reverse" in request.POST:
            results = Tweet.objects.filter(user = content).order_by("-id")
        else:
            results = Tweet.objects.filter(user = content)
        
        data["results"] = results
    return render(request, "result2.html", data)

def editDelete(request):
    data = {}
    if request.method == "POST":
        content = request.POST["id_search"]
        try:
            result = Tweet.objects.get(id = content)
            if request.POST["which"] == "edit":
                text = request.POST["content"]
                result.content = text
                result.save()
            
            else:
                result.delete()

        except:
            pass
        
    return redirect("tweets")

def login(request):
    if request.method == "POST":
        if request.POST["password"] == "password":
            request.session["logined"] = True
            return redirect("tweets")
    
    else:
        if not "logined" in request.session:
            return render(request, "login.html")
        
        else:
            return redirect("tweets")

@csrf_exempt
def apiuser(request):
    if request.method == "POST":
        user_data = request.POST["user"]
        content = Tweet.objects.filter(user__startswith = user_data)
        l = []
        for a in content:
            if not a.user in l:
                l.append(a.user)
        
        data = {"users": l}
        return JsonResponse(data)
    
    else:
        return HttpResponse("ERROR")
        

    
