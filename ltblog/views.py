# Create your views here.
from ltblog.models import Entry, Category
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from ltblog.models import Document
from ltblog.forms import DocumentForm

import datetime



def index(request):
    entry_list = Entry.objects.all().order_by('-pub_date')
    paginator = Paginator(entry_list,5)

    page = request.GET.get('page')

    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    return render_to_response('pages/index.html',{"entry_list" : entries},context_instance=RequestContext(request))

def entry(request, entry_id):
    blog = get_object_or_404(Entry, pk=entry_id)

    blog.num_views += 1
    blog.save()

    return render_to_response('pages/entry.html', {"entry":blog},context_instance=RequestContext(request))

def category_entry_list(request, category_id):
    #category = get_object_or_404(Category, id=category_id)
    entry_list = Entry.objects.filter(category__id=category_id)
    entry_list = entry_list.order_by('-pub_date')

    paginator = Paginator(entry_list,20)

    page = request.GET.get('page')

    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    return render_to_response('pages/entry_list.html', {"entry_list":entries},context_instance=RequestContext(request))

def archives_list(request, year, month):

    entry_list = Entry.objects.all()
    entry_list = entry_list.filter(pub_date__year=year, pub_date__month=month)

    paginator = Paginator(entry_list,20)

    page = request.GET.get('page')

    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    return render_to_response(('pages/entry_list.html'), {"entry_list": entries},context_instance=RequestContext(request))

def about(request):
    blog = get_object_or_404(Entry, pk=1)

    blog.num_views += 1
    blog.save()

    return render_to_response('pages/entry.html', {"entry":blog},context_instance=RequestContext(request))

def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('pages/login.html', c)

def auth_and_login(request, onsuccess='/fileupload/', onfail='/login/'):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)

def search(request):
    return render_to_response('pages/search.html', context_instance=RequestContext(request))

#def secured(request):
#    return render_to_response("pages/fileupload.html")

@login_required(login_url='/login/')
def uploadfile(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.upload_date = datetime.datetime.today()
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('ltblog.views.uploadfile'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    #end_date = datetime.timedelta(hours=1)
    date = datetime.datetime.today()
    documents = Document.objects.all().filter(upload_date__month=date.month, upload_date__year=date.year).order_by('-upload_date')

    # Render list page with the documents and the form
    return render_to_response(
        'pages/fileupload.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )