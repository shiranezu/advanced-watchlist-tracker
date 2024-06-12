from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Watchlist, Item
from .forms import WatchlistForm, ItemForm

@login_required(login_url='tracker:login')
def watchlist_list(request):
    watchlists = Watchlist.objects.filter(user=request.user)
    return render(request, 'tracker/watchlist_list.html', {'watchlists': watchlists})

@login_required(login_url='tracker:login')
def watchlist_detail(request, pk):
    watchlist = Watchlist.objects.get(pk=pk, user=request.user)
    items = watchlist.items.all()
    return render(request, 'tracker/watchlist_detail.html', {'watchlist': watchlist, 'items': items})

@login_required(login_url='tracker:login')
def add_watchlist(request):
    if request.method == 'POST':
        form = WatchlistForm(request.POST)
        if form.is_valid():
            watchlist = form.save(commit=False)
            watchlist.user = request.user
            watchlist.save()
            return redirect('watchlist_list')
    else:
        form = WatchlistForm()
    return render(request, 'tracker/add_watchlist.html', {'form': form})

@login_required(login_url='tracker:login')
def add_item(request, watchlist_id):
    watchlist = Watchlist.objects.get(pk=watchlist_id, user=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.watchlist = watchlist
            item.save()
            return redirect('watchlist_detail', pk=watchlist_id)
    else:
        form = ItemForm()
    return render(request, 'tracker/add_item.html', {'form': form, 'watchlist': watchlist})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('watchlist_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '':
            return render(request, 'auth/login.html')
        elif password == '':
            return render(request, 'auth/login.html')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'auth/login.html')

