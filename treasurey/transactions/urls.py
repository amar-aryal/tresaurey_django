from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete-income/<int:id>', views.delete_income_item, name="income-delete"),
    path('delete-expense/<int:id>', views.delete_expense_item, name="expense-delete"),
    path('update-income/<int:id>', views.update_income_item, name="income-update"),
    path('update-expense/<int:id>', views.update_expense_item, name="expense-update"),
]