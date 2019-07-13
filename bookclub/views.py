from django.shortcuts import render

# Create your views here.
def index(request):
	all_books = books.objects[:-1]
	context = {'all_books':all_books}
	return render(request,'/index.html',context)
def detail(request, book_name):
	try:
		book = books.objects.get(pk = book_name)
	except books.DoesNotExist:
		raise Http404("Book not available")
	return render(request,'/details.html',{'book':book})


