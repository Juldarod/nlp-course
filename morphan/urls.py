from django.conf.urls import url
from morphan.views import HomeView

urlpatterns = [
    url('morphan', HomeView.as_view())]
