#
# from django import forms
# from orms.models import *
#
#
# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=20, label='name')
#     weight = forms.CharField(max_length=50, label='重量')
#     size = forms.CharField(max_length=50, label='尺寸')
#
#     choices_list = [(i+1, v['type_name']) for i,v in enumerate(type.objects.values('type_name'))]
#     type = forms.CharField(choice=choices_list, label='产品类型')
