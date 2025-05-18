from django.shortcuts import render


def home(reqiest):
    return render(reqiest, 'home.html')


def contacts(reqiest):
    return render(reqiest, 'contacts.html')
