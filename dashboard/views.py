from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import GalleryImage

def home(request): 
        return render(request, "home.html")
def about(request): 
        return render(request, "about.html")
def services(request):
       return render(request, "services.html")
def gallery(request):
    category = request.GET.get("category", "")
    images = GalleryImage.objects.filter(is_visible=True)
    if category:
        images = images.filter(category=category)
    return render(request, "gallery.html", {
        "images": images,
        "categories": GalleryImage.CATEGORIES,
        "active": category,
    })
def contact(request):
    if request.method == "POST":
        print(">>> POST received")
        form = ContactForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            if d["website"]:
                print(">>> BLOCKED: hidden field was filled:", d["website"])
                messages.error(request, "Message blocked as spam. Please try again.")
                return redirect("contact")
            body = (
                f"Name: {d['name']}\n"
                f"Phone: {d['phone']}\n"
                f"Email: {d['email'] or 'not given'}\n"
                f"Subject: {d['subject']}\n\n"
                f"{d['message']}"
            )
            try:
                EmailMessage(
                    subject=f"Website message: {d['subject']} - {d['name']}",
                    body=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.SHOP_EMAIL],
                    reply_to=[d["email"]] if d["email"] else None,
                ).send()
                print(">>> EMAIL SENT")
                messages.success(request, "Thank you! Your message has been sent. We will get back to you soon.")
                return redirect("contact")
            except Exception as e:
                print(">>> EMAIL ERROR:", repr(e))
                messages.error(request, "Sorry, the message could not be sent. Please call or WhatsApp us instead.")
        else:
            print(">>> FORM INVALID:", form.errors.as_json())
            messages.error(request, "Please check the form: " + "; ".join(
                f"{f}: {', '.join(e)}" for f, e in form.errors.items()))
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})