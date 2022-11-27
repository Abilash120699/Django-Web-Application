from django.shortcuts import render

# Create your views here.

def example(request):
    return render(request, 'expense/index.html')

def example_2(request):
    return render(request, 'expense/expense.html')