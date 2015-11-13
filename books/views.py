#from django.shortcuts import render
# -*- coding: utf-8 -*-
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Author, Book
def start(request):
    #返回起始的搜索界面
    return render_to_response('start.html')
def showall(request):
    ##显示数据库内所有图书
    books = Book.objects.filter()
    return render_to_response('showall.html',{'books':books})
def search(request):
    #在数据库中搜索对应作者的书
    if 'q' in request.GET:
        q = request.GET['q']
        author = Author.objects.filter(Name=q)
        books = Book.objects.filter(AuthorID=author)
        return render_to_response('search_results.html',locals())
    else:
        return render_to_response('start.html', {'error': True})
def detail(request):
    #返回显示图书详细信息的界面
    q = request.GET['ISBN']
    book = Book.objects.get(ISBN=q)
    return render_to_response('detail.html',locals())
def delete(request):
    #删除图书
    q = request.GET['ISBN']
    book = Book.objects.get(ISBN=q)
    name = book.AuthorID.Name
    author = Author.objects.filter(Name=name)
    books = Book.objects.filter(AuthorID=author)
    book.delete()
    return render_to_response('search_results.html',{'q':name,'books' :books})
@csrf_exempt
def create(request):
    #创建新图书或者更新图书信息
    if request.method == 'POST':
        post = request.POST
        error = []
        if Book.objects.filter(Title = post["Title"]):
            return render_to_response('create.html', {'error': True})
        else:
            if Author.objects.filter(Name = post["Author"]):
                author = Author.objects.get(Name = post["Author"])
                ISBN = post["ISBN"]
                AuthorID = author
                Title = post["Title"]
                Publisher = post["Publisher"]
                PublishDate= post["PublishDate"]
                Price= post["Price"]
                if not ISBN or not author or not Title or not Publisher or not PublishDate or not Price:
                    if not ISBN:
                        error.append('ISBN没有填写')
                    if not author:
                        error.append('作者没有填写')
                    if not Title:
                        error.append('书名没有填写')
                    if not Publisher:
                        error.append('出版商没有填写')
                    if not PublishDate:
                        error.append('出版日期没有填写')
                    if not Price:
                        error.append('价格没有填写')
                    return render_to_response('create.html', {'Error': error})
                else:
                    newbook = Book(ISBN=ISBN, AuthorID=AuthorID, Title=Title, Publisher=Publisher, PublishDate=PublishDate, Price=Price)
                    newbook.save()
            else:
                return render_to_response('author.html',{'Name':post["Author"]})
        return render_to_response('detail.html',{'book':newbook})
    return render_to_response('create.html')
@csrf_exempt
def author(request):
    #创建作者
    if request.POST:
        post = request.POST
        error = []
        if Author.objects.filter(Name = post["Name"]):
            return render_to_response('author.html', {'Error': True})
        AuthorID = post["AuthorID"]
        Name = post["Name"]
        Age = post["Age"]
        Country = post["Country"]
        if not AuthorID or not Name or not Age or not Country:
            if not AuthorID:
                error.append('作者ID没有填写')
            if not Name:
                error.append('作者姓名没有填写')
            if not Age:
                error.append('作者年龄没有填写')
            if not Country:
                error.append('作者国家没有填写')
            return render_to_response('author.html', {'error': error})
        else:
            newauthor = Author(AuthorID = AuthorID,Name = Name,Age = Age, Country = Country)
            newauthor.save()
    else:
        return render_to_response('author.html')
    return render_to_response('start.html')
@csrf_exempt
def update(request):
    #更新书籍功能
    q = request.GET['ISBN']
    if request.method == 'POST':
        error = []
        post = request.POST
        if Author.objects.filter(Name = post["Author"]):
                author = Author.objects.get(Name = post["Author"])
                ISBN = q
                AuthorID = author
                Title = post["Title"]
                Publisher = post["Publisher"]
                PublishDate= post["PublishDate"]
                Price= post["Price"]
                if not ISBN or not author or not Title or not Publisher or not PublishDate or not Price:
                    if not ISBN:
                        error.append('ISBN没有填写')
                    if not author:
                        error.append('作者没有填写')
                    if not Title:
                        error.append('书名没有填写')
                    if not Publisher:
                        error.append('出版商没有填写')
                    if not PublishDate:
                        error.append('出版日期没有填写')
                    if not Price:
                        error.append('价格没有填写')
                    return render_to_response('create.html', {'Error': error})
                else:
                    newbook = Book(ISBN=ISBN, AuthorID=AuthorID, Title=Title, Publisher=Publisher, PublishDate=PublishDate, Price=Price)
                    newbook.save()
        else:
            return render_to_response('author.html',{'Name':post["Author"]})
        return render_to_response('detail.html',{'book':newbook,'q':0})
    q = request.GET['ISBN']
    book = Book.objects.get(ISBN=q)
    return render_to_response('update.html',{'book':book})
