from django.shortcuts import redirect, render
from django.contrib import messages 
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        property = request.POST['property']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        landlord_email = request.POST['landlord_email']

        # Check to see user has already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            had_contacted = Contact.objects.all().filter(property_id=property_id, user_id=user_id)
            if had_contacted:
                messages.error(request, 'You have previously submitted an inquiry for '+property)
                return redirect('/properties/'+property_id)

        contact = Contact(property= property, property_id = property_id, name=name, email=email,phone=phone, message= message, user_id=user_id)        
            
        contact.save()

        #send email
        send_mail(
            'Property Listing Inquiry',
            'There has been an iquiry for ' + property +'. Sign into the Admin Panel for more details.',
            'tekeliap@gmail.com',
            [landlord_email,'theterrys2018@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Your request has been submitted. You will be contacted shortly. ')

        return redirect('/properties/'+property_id)