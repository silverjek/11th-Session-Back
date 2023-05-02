from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from community.models import Posting
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def List(request):
    posts = Posting.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    return render(request, 'detail.html', {'post':post})

def search(request):
  content_list = Posting.objects.all()
  search_list = content_list
  search = request.GET.get('search','')
  if search:
    search_list = content_list.filter(
      Q(title__icontains = search) |
      Q(upload_time__icontains = search) |
      Q(content__icontains = search)
    )
  paginator = Paginator(search_list,5)
  page = request.GET.get('page','')
  posts = paginator.get_page(page)
  board = Posting.objects.all()

  return render(request, 'search.html',{'posts':posts, 'Board':board, 'search':search})