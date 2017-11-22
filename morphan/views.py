import time
from django.views.generic import TemplateView
from django.shortcuts import render
from morphan.forms import InputForm
from morphan.processing import Processing, dictionary
from morphan.analysis import Analysis


# Create your views here.
class HomeView(TemplateView):
    template_name = 'morphan/home.html'
    analyzer = Analysis()
    start_time = time.clock()
    dictionary = dictionary()
    end_time = time.clock()
    print('Creating dictionary: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds\n')

    def get(self, request):
        form = InputForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InputForm(request.POST)
        if form.is_valid():
            query = Processing(emoticon=[], money=[], comma=[], mayor=[])
            text = query.process(self.dictionary, form.cleaned_data["tweet"], self.analyzer)
            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)
