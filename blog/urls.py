from django.urls import path
from blog.apps import BlogConfig
from blog.views import PaperListView, PaperDetailView, PaperCreateView, PaperUpdateView, PaperDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('paper_list', PaperListView.as_view(), name='paper_list'),
    path('paper_detail/<int:pk>', PaperDetailView.as_view(), name='paper_detail'),
    path('paper_form', PaperCreateView.as_view(), name='paper_create'),
    path('paper_list/<int:pk>/update', PaperUpdateView.as_view(), name='paper_update'),
    path('paper_list/<int:pk>/delete', PaperDeleteView.as_view(), name='paper_delete'),
]