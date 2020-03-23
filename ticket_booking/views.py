

# Create your views here.
from django.shortcuts import render,get_object_or_404
from .forms import MovieDetailForm
from .models import MovieDetails 



# Create your views here.

def create_view(request):
    form = MovieDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MovieDetailForm()
    context = {"form":form}
    template_name = 'ticket_booking/create.html'
    return render(request,template_name,context)

def list_view(request):
    obj = MovieDetails.objects.all #Fetches every detail from the moviedetails database
    template_name = 'ticket_booking/list.html'
    context = {"obj":obj}
    return render(request,template_name,context) 

def detail_view(request,slug):
	obj = get_object_or_404(MovieDetails,slug=slug)
	template_name = "ticket_booking/detail.html"
	context = {"obj":obj}
	return render(request,template_name,context) 



def detail_book_view(request,slug):
	obj = get_object_or_404(MovieDetails,slug=slug)
	template_name = "ticket_booking/detailbook.html"
	if(request.method == "POST"): 
		tickets = request.POST['tickets']  
		obj.Tickets_booked += int(tickets)
		obj.Tickets_available = obj.Tickets_available - int(tickets)
		obj.save() 

	'''if request.GET.get("mybtn"):
		obj = get_object_or_404(MovieDetails,slug=slug)
		obj.state = True 
		obj.save()'''

		 
		#obj.save() 

	context = {"obj":obj}
	return render(request,template_name,context)  

	