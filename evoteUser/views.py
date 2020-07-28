from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth 
from . models import UserDetail,VoteCase,Candidates
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

           
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST.get('pass'))
        print(request.POST['username'],request.POST.get('pass'))
        print(user)
        if user is not None :
            auth.login(request,user)
            return redirect(loginIntro)
        else:
            print("invalid  details")
    return render(request,'login.html')

          
       
def register(request):
    if request.method == 'POST':
        if request.POST.get('pass1')==request.POST.get("pass2"):
            try:
                
                user = User.objects.get(username=request.POST['username'])

                return render(request,'register.html',{'error':'Username exsists'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST.get('pass1'))
                phone = request.POST['phone']
                uid = request.POST['uid']
                usrdetail = UserDetail(phone=phone,uid=uid,user=user)
                usrdetail.save()

               
                print("signed up.....")
            return render (request,'login.html')
    return render (request,'register.html')  


@login_required(login_url='/login')
def loginIntro(request):
    return render (request,'login_intro.html')

@login_required(login_url='/login') 
def createVoteCase(request):
    id = createVoteCaseId(request=request)
    return render (request,'create_vote_case.html', {'id':id})

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect(login)


    # curd opeartions 
@csrf_exempt
def addVoteCase(request):
    if request.method=='POST':  
        vid = request.POST.get('vid')
        votecase_name = request.POST.get('name')
        controller = request.POST.get('controller')
        desc = request.POST.get('desc')
        votecase = VoteCase( username =request.user.username,vcid=vid,
        case_name =votecase_name,controller =controller,desc=desc)
        votecase.save()
        # return redirect(loginIntro)
        return JsonResponse({
            "status":"success"
        })

# cross site scripting has been disabled.

@csrf_exempt
def addCandidate(request):
    if request.method=='POST':
        votecaseid = request.POST.get('caseid')
        votecase = VoteCase.objects.get(vcid=votecaseid)
        cname = request.POST.get('cname')
        desc=request.POST.get('description')
        #img = request.POST.get('cimage')
        candidates = Candidates(votecase=votecase,cname=cname,desc=desc,image="no image found")
        candidates.save()
        data = {
            "status":" success"
        }    
        return  JsonResponse(data)


#creating unique vote case  id for each case
def createVoteCaseId(request):
    return request.user.username+ str(datetime.now().hour)  + str(datetime.now().minute) + str(datetime.now().microsecond)
    
@login_required(login_url='/login')
def viewVoteCase(request):
    if request.method =='POST':
        code = request.POST.get('code')
        votecase = VoteCase.objects.get(vcid=code)
        candidates = Candidates.objects.all().filter(votecase=votecase)
       
        return render(request,'viewVoteCase.html',
        {
            "votecase":votecase,
            "candidates":candidates
        })
        
