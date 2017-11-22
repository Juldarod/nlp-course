from django.views.generic import TemplateView
from django.shortcuts import render
from morphan.forms import InputForm
from morphan.processing import Processing


# Create your views here.
class HomeView(TemplateView):
    template_name = 'morphan/home.html'
    processing = Processing()
    corpus = processing.get_dictionary()

    def get(self, request):
        form = InputForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InputForm(request.POST)
        processing = self.processing
        if form.is_valid():
            tokenized_text = processing.nltk_tweet_tokenizer(form.cleaned_data['tweet'])
            new_tokenized_text = processing.my_tokenizer(tokenized_text, self.corpus)
            raw_text = processing.get_raw_text(new_tokenized_text)
            analyzed_words = processing.analyze_raw_text(raw_text + '.')
            text = processing.make_text(analyzed_words, new_tokenized_text)
            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)
