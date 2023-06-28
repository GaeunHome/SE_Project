from django import forms
from .models import Satisfaction, purchase

class SatisfactionForm(forms.ModelForm):
    class Meta:
        model = Satisfaction
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = purchase
        fields = '__all__'
        labels = {
            'MID': '編號',
            'MNAME': '品牌',
            'PCost': '成本',
            'PDate': '日期',
            'MFuction': '功能',
            'PAmount': '數量',
            'MClass': '型號',
        }