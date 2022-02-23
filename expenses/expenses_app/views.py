from django.shortcuts import render, redirect

from expenses.expenses_app.forms import CreateExpenseForm, CreateProfileForm, EditProfileForm, EditExpenseForm, \
    DeleteExpenseForm, DeleteProfileForm
from expenses.expenses_app.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    else:
        expenses = Expense.objects.all()
        total_expenses = sum(e.price for e in expenses)
        money_left = profile.budget - total_expenses

    context = {
        'profile': profile,
        'expenses': expenses,
        'money_left': money_left,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == "POST":
        expense_form = CreateExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('home')
    else:
        expense_form = CreateExpenseForm()

    expense = Expense.objects.count()

    context = {
        'expense': expense,
        'expense_form': expense_form,

    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        expense_form = EditExpenseForm(request.POST, instance=expense)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('home')
    else:
        expense_form = EditExpenseForm(instance=expense)
    context = {
        'expense': expense,
        'expense_form': expense_form,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        expense_form = DeleteExpenseForm(request.POST, instance=expense)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('home')
    else:
        expense_form = DeleteExpenseForm(instance=expense)
    context = {
        'expense': expense,
        'expense_form': expense_form,
    }
    return render(request, 'expense-delete.html', context)


def create_profile(request):
    if request.method == "POST":
        profile_form = CreateProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = CreateProfileForm()

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = get_profile()

    expenses = Expense.objects.all()
    expenses_count = Expense.objects.count()

    total_expenses = sum(e.price for e in expenses)
    money_left = profile.budget - total_expenses

    context = {
        'profile': profile,
        'expenses': expenses,
        'expenses_count': expenses_count,
        'money_left': money_left,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    if request.method == "POST":
        profile_form = EditProfileForm(request.POST, request.FILES, instance=get_profile())
        if profile_form.is_valid():
            profile_form.save()
            return redirect('show profile')
    else:
        profile_form = EditProfileForm(instance=get_profile())
    context = {
        'profile_form': profile_form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    if request.method == "POST":
        profile_form = DeleteProfileForm(request.POST, instance=get_profile())
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = DeleteProfileForm(instance=get_profile())

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'profile-delete.html', context)
