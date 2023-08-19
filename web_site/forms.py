from django import forms


# choice = (
#         ('py', 'Python'),
#         ('js', 'JavaScript'),
#     )
from web_site.models import UserProfileModel, KeywordsIgnoreModel, WordIgnoreModel


class UserKeywordForm(forms.Form):
    keyword = forms.CharField(max_length=100)
    #keyword_choise = forms.ChoiceField(choice=choice)

class KeywordForm(forms.ModelForm):
    class Meta:
        model = KeywordsIgnoreModel
        fields = ['keyword']


class WordIgnoreForm(forms.ModelForm):
    class Meta:
        model = WordIgnoreModel
        fields = ['word_ignore']