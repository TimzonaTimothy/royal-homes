from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from .choices import property_choices


# home-variation2.html
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    return render(request, 'home-variation2.html', {'listings':listings,'property_choices':property_choices,})


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'listings':paged_listings
    }
    return render(request, 'listings.html', context)


def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing':listing
    }

    return render(request, 'listing.html', context)


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact = Inquiry(listing=listing, listing_id=listing_id, name=name, email=email, 
        phone=phone, message=message, )
        contact.save()

        #sending mail
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for '+ listing + '. Sign in to admin panel for more information',
        #     'arizonatymothy@gmail.com',
        #     ['arizonatymothy@gmail.com','timzonatimothy@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted.')

        return redirect('/listings/'+listing_id)
    

def agent(request):
    return render(request, "agent.html", {})
    

def about(request):
    return render(request, "about.html", {})

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)


    if 'property' in request.GET:
        property_ = request.GET['property']
        if property_:
            queryset_list = queryset_list.filter(property_type__iexact=property_)

    

    context = {
        'listings':queryset_list,
        'property_choices':property_choices,
        'values':request.GET,
    }
    return render(request, 'search.html', context)



def main_contact(request):
     if request.method == "POST":
          name = request.POST['name'] 
          email = request.POST['email']
          phone = request.POST['phone']
          subject = request.POST['subject']
          message = request.POST['message']

          contact = Contacts.objects.create(name=name,phone=phone,email=email,subject=subject,message=message)
          contact.save();
          messages.success(request, 'Your massage has been submitted ','')
          return render(request, 'contact.html', {})
     else:
          return render(request, 'contact.html', {})

		  
           
# def main_contact(request):
#     if request.method == "POST":
# 		name = request.POST['name'] 
# 		email = request.POST['email']
#         phone = request.POST['phone']
#         subject = request.POST['subject']
#         message = request.POST['message']
            
# 		contact = Contact.objects.create(name=name,phone=phone,email=email,message_subject=subject,message=message)
# 		contact.save();
# 		messages.success(request, 'Your massage has been submitted ','')
# 		# send_mail(
# 		# 	massage_firstname + ''+ massage_lastname +' sent you an enquiry '+ massage_email + ' '+ massage_subject,
# 		# 	massage,
# 		# 	'arizonatymothy@gmail.com',
# 		# 	['arizonatymothy@gmail.com',],
# 		# 	fail_silently=False
# 		# 	)
# 		# messages.success(request, 'Your email has been sent ','alert alert-success alert-dismissible')
# 		return render(request, 'contact.html', {})
# 	else:
# 		return render(request, 'contact.html', {})
    