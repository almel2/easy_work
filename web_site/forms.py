from django import forms


# choice = (
#         ('py', 'Python'),
#         ('js', 'JavaScript'),
#     )


class UserKeywordForm(forms.Form):
    keyword = forms.CharField(max_length=100)
    #keyword_choise = forms.ChoiceField(choice=choice)