from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from . import forms
from .models import Income, Expense

def home(request):
    income_list = Income.objects.all()
    expense_list = Expense.objects.all()

    def income_amount_sum():
        transaction_total = 0
        for amount in income_list:
            transaction_total += amount.income_amount

        return transaction_total

    def expenses_amount_sum():
        transaction_total = 0
        for amount in expense_list:
            transaction_total += amount.expense_amount

        return transaction_total

    income_total = income_amount_sum()
    expense_total = expenses_amount_sum()
    savings = income_total-expense_total

    if(request.method == 'POST'):
        form1 = forms.RecordIncome(request.POST)
        form2 = forms.RecordExpense(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')
        if form2.is_valid():
            form2.save()
            return redirect('home')
    else:
        form1 = forms.RecordIncome()
        form2 = forms.RecordExpense()

    context = {'income_list': income_list, 'expense_list': expense_list, 'form1': form1, 'form2': form2, 
                'income_total': income_total, 'expense_total': expense_total, 'savings': savings}
    
    return render(request, 'transactions/home.html', context)


def delete_income_item(request, id):
    id = int(id)
    
    obj = Income.objects.get(id = id)

    obj.delete()
    return redirect('home')


def delete_expense_item(request, id):
    id = int(id)

    obj = Expense.objects.get(id = id)
    obj.delete()

    return redirect('home')

    

def update_income_item(request, id):
    id = int(id)

    obj = Income.objects.get(id = id)

    form = forms.RecordIncome(instance=obj)

    if request.method == 'POST':
        form = forms.RecordIncome(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'transactions/update_income.html', context)

def update_expense_item(request, id):
    id = int(id)

    obj = Expense.objects.get(id = id)

    form = forms.RecordExpense(instance=obj)

    if request.method == 'POST':
        form = forms.RecordExpense(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'transactions/update_expense.html', context)


