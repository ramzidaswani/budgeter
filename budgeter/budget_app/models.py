from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    email = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    bank_name = models.CharField(max_length = 50, null=True, blank= False, unique=False, default = None)
    def __str__(self):
        return self.customer.username


class Budgeter(models.Model):
    budget_name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    budget_name = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(budget, self).save(*args, **kwargs)

    @property
    def budget(self):
        expenses = Expense.objects.filter(budget=self)
        total_amount = 0

        for every_expense in expenses:
            total_amount += expense.amount

        return self.budget - total_amount

    @property
    def transactions_total(self):

        expenses = Expense.objects.filter(budget=self)
        return len(expense_list)


class Type(models.Model):
    budget = models.ForeignKey(Budgeter, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class Transaction(models.Model):
    budget = models.ForeignKey(Budgeter, on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('amount',)
