from django.conf.urls import url
from probarser.views import HomeView

urlpatterns = [
    url('probarser', HomeView.as_view())]