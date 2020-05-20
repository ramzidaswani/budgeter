import json
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from .models import Customer, Budgeter, Type, Transaction
from .forms import  USerForm, UserInfo,transactionForm,

def budget_list(request):

    budget_list = Budgeter.objects.all()

    return render(request, 'budget/budgetlist.html', {'budget_list': budget_list})


def budget_info(request, budget_slug):

    budget = get_object_or_404(budget, slug=budget_slug)

    if request.method == 'GET':

        type_list = type.objects.filter(budget=budget)
        
        transaction_list = budget.transactions.all()

        return render(request, 'budget/budget-detail.html', {'budget': budget,
                                                              'transaction_list': transaction_list,
                                                              'type_list': type_list})

    elif request.method == 'POST':

        form = transactionForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            type_name = form.cleaned_data['type']

            type = get_object_or_404(type,
                                        budget = budget,
                                        name = type_name)

            transaction.objects.create(budget = budget,
                                  title = title,
                                  amount = amount,
                                  type = type
            ).save()

    elif request.method == 'DELETE':

        id = json.loads(request.body)['id']
        transaction = get_object_or_404(transaction, id=id)
        transaction.delete()

        return HttpResponse('')

    return HttpResponseRedirect(budget_slug)


class BudgetCreateView(CreateView):

    model = budget
    template_name = 'budget/add-budget.html'
    fields = ('name', 'budget')

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')

        for type in categories:

            type.objects.create(
                budget = budget.objects.get(id=self.object.id),
                name = type
            ).save

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])