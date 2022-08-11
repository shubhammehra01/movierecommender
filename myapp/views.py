from copyreg import pickle
from django.shortcuts import render
from datetime import datetime
from xmlrpc.client import DateTime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Contact

from myapp.models import Account
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
import pandas as pd
import requests
import difflib
import pickle as pk
# Create your views here.
def home(request):  
    movie_dict = pk.load(open('movie_dict.pkl','rb'))
    movies = pd.DataFrame(movie_dict)
    result={}
    if request.method=='POST':
        name = request.POST.get('movie_name')
        similar = pk.load(open('similar.pkl','rb'))
        data = [] 
        poster =[]  
        def fetch(movie_id):  
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1c28161e325733b2cbc131577612f3ee&language=en-US'.format(movie_id))
            data = response.json()
            return 'https://image.tmdb.org/t/p/w500'+ data['poster_path']

        def recommend(movie):
            movie_index = movies[movies['title']==movie].index[0]
            distances = similar[movie_index]
            movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
            
            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id
                data.append(movies.iloc[i[0]].title)
                poster.append(fetch(movie_id))
        
        recommend(name)
        if len(data)>4 and len(poster)>4:
            result['MovieName']=data
            result['MoviePoster']=poster

    result['name']=movies['title'].values
    return render(request,'index.html',result)
    

def about(request):
    return render(request,'about.html')

def account(request):
    if request.method == 'POST': 
        email = request.POST.get('email')
        password = request.POST.get('password')
        account = Account(email=email,password=password,date=datetime.today())
        account.save()
        messages.success(request, 'your Details are recieved by us we will contact you shortly')
    return render(request,'account.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        contact = Contact(name=name,email=email,country=country,date=datetime.today())
        contact.save()  
        messages.success(request, 'your Details are received by us we will contact you shortly')
    return render(request,'contact.html')

