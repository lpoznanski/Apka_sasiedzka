from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import FormMixin

from .forms import ItemForm
from .models import Announcement, Item

class IndexView(generic.ListView):
    queryset = Announcement.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetailView(generic.DetailView):
    model = Announcement
    template_name = 'post_detail.html'

class ItemListView(FormMixin, generic.ListView):
    queryset = Item.objects.all().order_by('-created_on')
    template_name = 'item_list.html'
    form_class = ItemForm

    # def get_context_data(self, **kwargs):
    #     context = super(ItemListView, self).get_context_data(**kwargs)
    #     context['form'] = ItemForm()
    #     return context

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            Item.objects.create(author=author, name=name, description=description, status=status)
            return redirect('/items')
        else:
            return HttpResponse(form.errors)
