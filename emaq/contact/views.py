from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def contact(request):
  contact_form = ContactForm()

  if request.method == "POST":
    contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
      name = request.POST.get('name','')
      email = request.POST.get('email','')
      content = request.POST.get('content','')
      #Enviar correo y redireccion
      email = EmailMessage(
        'Emaq S.A: Nuevo mensaje de contacto',
        'De {} <{}>\n\nEscribio:\n\n{}'.format(name,email,content),
        'no-contestar@inbox.mailtrap.io', #Emaqil de la empresa. 
        [''],
        reply_to=['email'],
      )

      try:
        email.send()
        #Si funciona
        return redirect(reverse('contact')+"?ok")
      except:
        #Algo no funciona
        return redirect(reverse('contact')+"?fail")

  return render(request,"contact/contact.html",{'form':contact_form})