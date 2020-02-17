# ナビゲーションでどの画面からでも呼び出せるようにする
from .models import Company

def company_list(request):
    company_list = Company.objects.all()

    params = {
        'company_list': company_list
    }
    return params