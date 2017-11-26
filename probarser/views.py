import inspect
import os

from django.shortcuts import render
from django.views.generic import TemplateView
from nltk.draw.tree import TreeView

from probarser.analysis import Analysis
from probarser.forms import InputForm
from probarser.processing import Processing


# Create your views here.
class HomeView(TemplateView):
    template_name = 'probarser/home.html'
    analyzer = Analysis()

    def get(self, request):
        form = InputForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InputForm(request.POST)
        if form.is_valid():
            query = Processing(form.cleaned_data["text"], self.analyzer)
            trees = query.process(form.cleaned_data["text"])
            args = {'form': form,
                    'stanford': 'Stanford Parser', 'bikel': 'Bikel Parser',
                    'stanford_draws': draw_stanford(trees), 'bikel_trees': trees[1],
                    'stanford_trees': trees[0]}
            return render(request, self.template_name, args)


def draw_stanford(tree):
    dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    filename = dirname + '/static/probarser/img/output_img'
    trees = []
    cont = 1
    for t in tree[0]:
        TreeView(t)._cframe.print_to_file(filename + '%s.ps' % cont)
        os.system('convert -density 150 ' + filename + '%s.ps ' % cont + filename + '%s.png' % cont)
        cont += 1
    for i in range(cont-1):
        trees.append('probarser/img/output_img' + '%s' % (i+1) + '.png')
    return trees
