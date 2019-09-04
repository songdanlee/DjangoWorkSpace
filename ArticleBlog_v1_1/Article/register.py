from django import forms


class Register(forms.Form):

    username = forms.CharField(max_length=32,label='用户名')
    password = forms.CharField(max_length=32,required=True,label='密码')
    email = forms.EmailField(label='邮箱')
    d_password = forms.CharField(max_length=32,required=True,label='重新输入密码')


    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username == "admin":
            self.add_error("username","用户名%s为非法字符"%username)
            print(self.errors)
        else:
            return username