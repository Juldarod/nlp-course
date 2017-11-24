from django.views.generic import TemplateView
from django.shortcuts import render
from probarser.forms import InputForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'probarser/home.html'

    def get(self, request):
        form = InputForm()
        return render(request, self.template_name, {'form': form})

    # def post(self, request):
    #     form = InputForm(request.POST)
    #     if form.is_valid():
    #         args = {'form': form, 'text': text}
    #         return render(request, self.template_name, args)
