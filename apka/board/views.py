from django.views import generic
from .forms import ItemForm
from .models import Announcement, Item

class IndexView(generic.ListView):
    queryset = Announcement.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetailView(generic.DetailView):
    model = Announcement
    template_name = 'post_detail.html'

class ItemListView(generic.ListView):
    queryset = Item.objects.all().order_by('-created_on')
    template_name = 'item_list.html'

    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        context['form'] = ItemForm()
        return context