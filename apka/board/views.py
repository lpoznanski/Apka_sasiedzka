from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ItemForm, UserDetailForm
from .models import Announcement, Item, Image, UserDetail

class IndexView(generic.ListView):
    queryset = Announcement.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetailView(generic.DetailView):
    model = Announcement
    template_name = 'post_detail.html'

class ItemListView(FormMixin, LoginRequiredMixin, generic.ListView):
    queryset = Item.objects.all().order_by('-created_on')
    template_name = 'item_list.html'
    form_class = ItemForm

    # def get_context_data(self, **kwargs):
    #     context = super(ItemListView, self).get_context_data(**kwargs)
    #     context['form'] = ItemForm()
    #     return context

    def post(self, request):
        form = ItemForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')
        if form.is_valid():
            author = request.user
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            new_item = Item.objects.create(author=author, name=name, description=description, status=status)
            for file in images:
                new_image = Image.objects.create(item=new_item, photo=file)
            return redirect('/items')
        else:
            return HttpResponse(form.errors)

class UserDetailCreateView(generic.CreateView):
    model = UserDetail
    fields = '__all__'