from django.views.generic import TemplateView
from django.shortcuts import render
from morphan.forms import InputForm
from morphan.processing import *


# Create your views here.
class HomeView(TemplateView):
    template_name = 'morphan/home.html'
    corpus = get_dictionary()

    def get(self, request):
        form = InputForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InputForm(request.POST)
        if form.is_valid():
            tokenized_text = nltk_tweet_tokenizer(form.cleaned_data['tweet'])
            new_tokenized_text = my_tokenizer(tokenized_text, self.corpus)
            raw_text = get_raw_text(new_tokenized_text)
            analyzed_words = analyze_raw_text(raw_text + '.')
            text = make_text(analyzed_words, new_tokenized_text)
            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)
