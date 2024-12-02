from django import forms
from matches.models import Match, Zawodnik, Events

class DodajMeczForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['Gosp', 'Gosc', 'SedziaG','SedziaA1', 'SedziaA2','data', 'godzina', 'ulica', 'miejscowosc','rozgrywki','runda','kolejka']

class EdytujMeczForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['wynik']

class DodajZawodnikaForm(forms.ModelForm):
    class Meta:
        model = Zawodnik
        fields = ['imie', 'nazwisko','nr']

class DodajEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['typ','minuta','kto','nr_zawodnika']