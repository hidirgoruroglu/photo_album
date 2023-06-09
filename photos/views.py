from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Photo

# Create your views here.
def gallery_view(request):
    category = request.GET.get("category")

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()
    context = dict(categories = categories, photos = photos)
    return render(request,"photos/gallery.html",context)

def photo_view(request, id):
    photo = get_object_or_404(Photo, id = id)
    context = dict(photo = photo)
    return render(request,"photos/photo.html",context)

def addPhoto_view(request):

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get("image")
        

        if data["category"] != "none":
            category = Category.objects.get(id = data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(name = data["category_new"])
        else:
            category = None

        photo = Photo.objects.create(category = category, description = data["description"], image = image)
        photo.save()

        return redirect("gallery")

    categories = Category.objects.all()

    context = dict(categories = categories)
    return render(request,"photos/add.html",context)