from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm,signupform,changepasswordform
from django.urls import reverse
from django.contrib.auth.models import User
from testapp.models import pollsmodel
# from testapp.forms import pollsform
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeview(request):
    x=False
    uname=None
    z=False
    cric=0
    foot=0
    kabb=0
    tenn=0
    y=None
    # total=pollsmodel.objects.count()
    # cric=((pollsmodel.objects.filter(game='cricket').count())/total)*100 or 0
    # foot=((pollsmodel.objects.filter(game='football').count())/total)*100 or 0
    # kabb=((pollsmodel.objects.filter(game='kabaddi').count())/total)*100 or 0
    # tenn=((pollsmodel.objects.filter(game='tennis').count())/total)*100 or 0
    if pollsmodel.objects.count():
        total=pollsmodel.objects.count()
        cric=((pollsmodel.objects.filter(game='cricket').count())/total)*100
        foot=((pollsmodel.objects.filter(game='football').count())/total)*100
        kabb=((pollsmodel.objects.filter(game='kabaddi').count())/total)*100
        tenn=((pollsmodel.objects.filter(game='tennis').count())/total)*100
    if request.user.is_authenticated and request.user.is_active:
        uname=request.session['uname']
        # uname=request.GET.get('username')
        if pollsmodel.objects.filter(uname=uname):
            h=pollsmodel.objects.filter(uname=uname)
            if h[0].game:
                z=True
    if request.method=='POST':
        if request.user.is_authenticated and request.user.is_active:
            # pollsmodel.objects.filter(uname=uname)[0].vote=None
            if pollsmodel.objects.filter(uname=uname):
                # z=True
                return HttpResponseRedirect(request.path_info)
                # return HttpResponse('already voted')
            if request.POST['action']:
                y=request.POST['action']
                # request.session['y']=y
                # y=request.session['y']
                mod=pollsmodel.objects.all().create(uname=uname,game=y,vote=1)
                if pollsmodel.objects.count():
                    total=pollsmodel.objects.count()
                    cric=((pollsmodel.objects.filter(game='cricket').count())/total)*100
                    foot=((pollsmodel.objects.filter(game='football').count())/total)*100
                    kabb=((pollsmodel.objects.filter(game='kabaddi').count())/total)*100
                    tenn=((pollsmodel.objects.filter(game='tennis').count())/total)*100

                # mod.uname=uname
                # mod.game=y
                # mod.vote=1
                # for obj in mod:
                #     obj.save()
                uemail=User.objects.filter(username=uname).values_list('email',flat=True)[0]

                subject="Hema Polls"
                message='Hello \nThanks for Participating in the poll \nYou have voted '+ y.capitalize()
                if y=='cricket':
                    message=message+'\nPlease join this link https://chat.whatsapp.com/LhjCKfYXTYpJsS21GoFO5y to get more updates about Cricket'
                send_mail(subject, message, 'punithdjango@gmail.com',[uemail], fail_silently=False)
                x=True

        else:
            return HttpResponseRedirect(reverse('account:login'))

    return render(request,'testapp/polls/home.html',{'x':x,'uname':uname,'z':z,'cric':cric,'foot':foot,'kabb':kabb,'tenn':tenn,'y':y})


def loginview(request):
    h=False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
            username=cd['username'],
            password=cd['password'])
            if user is not None:
            # if user:
                if user.is_active:
                    uname=cd['username']
                    request.session['uname']=uname
                    # request.session.set_expiry(120)
                    login(request, user)
                    return redirect('proj:home')
                else:
                    return HttpResponse('Your account has been disabled,contact admin <br> click here to go <a href="{%  url "proj:home" %}">home</a>')
            else:
                # return HttpResponse('Invalid login')
                f=False
                h=True
                if not User.objects.filter(username=cd['username']):
                    f=True
                    h=False
                return render(request, 'account/login.html', {'form': form,'h':h,'f':f})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def logoutview(request):
    logout(request)
    return render(request,'testapp/polls/logout.html')

def signupview(request):
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            form.save()

            username=form.cleaned_data.get('username')
            password1=form.cleaned_data.get('password1')
            cd = form.cleaned_data
            user = authenticate(username=username, password=password1)
            uname=cd['username']
            request.session['uname']=uname
            # request.session.set_expiry(120)
            login(request, user)
            return redirect('proj:home')
    return render(request,'account/signup.html',{'form':form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = changepasswordform(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!',extra_tags='alert')
            return redirect('proj:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})

def csrffailureview(request, reason=""):
    a='<a href="/logout">Logout</a> and Login again</h3>'
    return HttpResponse("<h1>From CSRF:Don't try to reset password or login to another account when you are logged in</h1><br><h3>Please "+a )
