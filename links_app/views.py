from django.shortcuts import render
from .models import Link
from .forms import AddLinkForm

def home_view(request):
    no_discounted = 0
    error = None
    
    form = AddLinkForm(request.POST or None)

    if request.method == "POST":
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Opps !!.. Name of price not found !!"
        except:
            error = "Opps !! something went wrong !!"

    form = AddLinkForm()
    query_set = Link.objects.all()
    items_no = query_set.count()

    if items_no > 0:
        discount_list = []
        for item in query_set:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)

    context = {
        'query_set':query_set,
        'items_no':items_no,
        'form':form,
        'error':error,
        'no_discounted':no_discounted,

    }    

    template_name = 'links/main.html'

    return render(request,template_name,context)

