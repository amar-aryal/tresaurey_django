from django import forms

from . import models

class RecordIncome(forms.ModelForm):
    class Meta:
        model = models.Income
        fields = ['income_source', 'income_amount']

class RecordExpense(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = ['expense_source', 'expense_amount']