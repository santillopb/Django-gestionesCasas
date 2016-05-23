from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.utils import timezone
from .forms import LoginForm, ChatForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


from polls.models import Cases, Xat

def save_chat(request):
	#Xat.objects.create()
	# usuario: request.user
	# texto
	# - fecha
	if request.method == 'POST':
		form = ChatForm(request.POST)
		if form.is_valid():
			escriu = request.POST['escriu']
			xat = Xat.objects.create(text=escriu, user=request.user)
			xat.save()
			
	return redirect('polls:xat')

		
def login_page(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Te has identificado de modo correcto"
				else:
					message = "Tu usuario esta inactivo"

			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = LoginForm()

	form_chat = ChatForm()
	latest_cases_list = Cases.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	return render_to_response('polls/login.html', 
		{'message':message, 'formLogin':form, 'formChat': form_chat, 'latest_cases_list': latest_cases_list},
		 context_instance=RequestContext(request))	



def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(dateField__year__icontains=query) |
            Q(dateField__month__icontains=query) 
        )
        results = NotaCalendario.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("polls/search.html", {
        "results": results,
        "query": query
    })