from django.db import models

class Income(models.Model):
    income_source = models.CharField(max_length=100)
    income_amount = models.FloatField()
    income_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.income_source


class Expense(models.Model):
    expense_source = models.CharField(max_length=100)
    expense_amount = models.FloatField()
    expense_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.expense_source