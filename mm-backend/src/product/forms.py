from django import forms


class SecondCategoryForm(forms.ModelForm):

    def clean_title(self):
        # do something that validates your data
        title = self.cleaned_data["title"]
        if len(title) > 10:
            raise forms.ValidationError("标题不要超过10个字符!")
        return title
