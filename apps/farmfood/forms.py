from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class products(models.Form):
	product_name= models.CharField(max_length=30)
	quantity = models.IntegerField(max)
	quality= models.CharField(max_length=30)
	updatedqty= models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	