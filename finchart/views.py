from django.views.generic.list import MultipleObjectMixin # この行を追加
from .models import Company, Fstatement
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, DetailView
from .models import Company, Fstatement  # この行を追加


class IndexView(TemplateView):  # クラス名を変更
    template_name = 'finchart/index.html'

    #========以下すべて追加========
    def get_context_data(self, **kwargs):
        fstatement_list = Fstatement.objects.all().order_by('company')
        params = {
            'fstatement_list': fstatement_list,
        }
        return params

class CompanyView(DetailView):
    model = Company
    template_name = 'finchart/company_detail.html'

    def get_context_data(self, **kwargs):
        company_name = kwargs['object'].name
        fstatement_list = Fstatement.objects.filter(
            company=kwargs['object']).order_by('-fiscal_year')[:4]
        params = {
            'company_name': company_name,
            'fstatement_list': fstatement_list,
        }
        return params

# CompanyViewを変更
# class CompanyView(DetailView, MultipleObjectMixin):
#     model = Company
#     paginate_by = 4

#     def get_context_data(self, **kwargs):
#         # kwargs['object']は、今選択されているデータです。
#         # このCompanyViewが呼び出される時点ですでに1つのcompanyが選択されていますから、
#         # そのcompanyのデータを抽出することになります。
#         object_list = Fstatement.objects.filter(
#             company=kwargs['object']).order_by('-fiscal_year')
#         context = super(CompanyView, self).get_context_data(
#             object_list=object_list, **kwargs)

#         return context


class FstatementView(DetailView):
    model = Fstatement
