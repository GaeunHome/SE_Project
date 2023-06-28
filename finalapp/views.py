from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MassageChair, Salesperson, Branch, profit, customer, SalesDetail, purchase, Coupon, Satisfaction
from django.template.defaultfilters import floatformat
from django.db.models import Sum, Count
from django.http import JsonResponse
from .forms import SatisfactionForm, PurchaseForm

# Create your views here.
def company(request):
    # 同期相比
    totalthisJuly = Branch.objects.filter(SMON=6).aggregate(totalthisJuly=Sum('SNSALE'))['totalthisJuly']
    totalpastJuly = Branch.objects.filter(SMON=6).aggregate(totalpastJuly=Sum('SOSALE'))['totalpastJuly']
    totalthisMay = Branch.objects.filter(SMON=5).aggregate(totalthisMay=Sum('SNSALE'))['totalthisMay']
    totalpastMay = Branch.objects.filter(SMON=5).aggregate(totalpastMay=Sum('SOSALE'))['totalpastMay']
    totalthisApril = Branch.objects.filter(SMON=4).aggregate(totalthisApril=Sum('SNSALE'))['totalthisApril']
    totalpastApril = Branch.objects.filter(SMON=4).aggregate(totalpastApril=Sum('SOSALE'))['totalpastApril']
    totalthisMarch = Branch.objects.filter(SMON=3).aggregate(totalthisMarch=Sum('SNSALE'))['totalthisMarch']
    totalpastMarch = Branch.objects.filter(SMON=3).aggregate(totalpastMarch=Sum('SOSALE'))['totalpastMarch']
    # 目標銷售
    goal = Branch.objects.aggregate(goal=Sum('STc'))['goal']
    score = Branch.objects.aggregate(score=Sum('SAc'))['score']
    return render(request, 'companyindex.html', {
            'totalthisJuly': totalthisJuly,
            'totalpastJuly': totalpastJuly,
            'totalthisMay': totalthisMay,
            'totalpastMay': totalpastMay,
            'totalthisApril': totalthisApril,
            'totalpastApril': totalpastApril,
            'totalthisMarch': totalthisMarch,
            'totalpastMarch': totalpastMarch,
            'goal': goal,
            'score': score
        }
    )

def sales(request):
    salesperson = request.GET.get('salesperson')
    # 根據銷售人員參數從數據庫中獲取相應的數據
    salesperson_data = Salesperson.objects.get(SName=salesperson)
    return render(request, 'sales.html', {'salesperson': salesperson_data})

# def sales_view(request):
#     salespersons = Salesperson.objects.all().order_by('SID')  
#     context = {'salespersons': salespersons}
#     return render(request, 'sales.html', context)

def salesindex_view(request):
    salespersons = Salesperson.objects.all().order_by('SID')  
    context = {'salespersons': salespersons}
    return render(request, 'salesindex.html', context)

def salesindex(request):
    return render(request, 'salesindex.html')

def customer_view(request, customers):
    # 店名
    if customers=="B001":
        name = "中壢中原店"
    elif customers=="B002":
        name = "中壢中大店"
    elif customers=="B003":
        name = "中壢中北店"
    else:
        name = "中壢原大店"
    # 上排儀表板分析
    Newcustomer = customer.objects.filter(CMON="6", BID=customers).count()
    Perfer = customer.objects.filter(BID=customers).values('CDemand_description').annotate(count=Count('CDemand_description')).order_by('-count')[0]['CDemand_description']
    Recommend = customer.objects.filter(BID=customers).values('CHow').annotate(count=Count('CHow')).order_by('-count')[0]['CHow']
    # 客戶年齡分析
    age1 = customer.objects.filter(CAge_range="20-29", BID=customers).count()
    age2 = customer.objects.filter(CAge_range="30-39", BID=customers).count()
    age3 = customer.objects.filter(CAge_range="40-49", BID=customers).count()
    age4 = customer.objects.filter(CAge_range="50-59", BID=customers).count()
    age5 = customer.objects.filter(CAge_range="60以上", BID=customers).count()
    sum = age1 + age2 + age3 + age4 + age5
    # 當月客戶各產品銷售數量
    sale1 = sale2 = sale3 = sale4 = sale5 = sale6 = 0
    sale7 = sale8 = sale9 = sale10 = sale11 = sale12 = 0
    result1 = SalesDetail.objects.filter(MNAME="OSIM", MClass="高級豪華型")
    for sales_detail in result1:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale1 = sale1 + 1
    result2 = SalesDetail.objects.filter(MNAME="OSIM", MClass="實用按摩型")
    for sales_detail in result2:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale2 = sale2 + 1
    result3 = SalesDetail.objects.filter(MNAME="OSIM", MClass="經濟實惠型")
    for sales_detail in result3:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale3 = sale3 + 1
    result4 = SalesDetail.objects.filter(MNAME="Tokuyo", MClass="高級豪華型")
    for sales_detail in result4:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale4 = sale4 + 1
    result5 = SalesDetail.objects.filter(MNAME="Tokuyo", MClass="實用按摩型")
    for sales_detail in result5:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale5 = sale5 + 1
    result6 = SalesDetail.objects.filter(MNAME="Tokuyo", MClass="經濟實惠型")
    for sales_detail in result6:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale6 = sale6 + 1
    result7 = SalesDetail.objects.filter(MNAME="HY", MClass="高級豪華型")
    for sales_detail in result7:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale7 = sale7 + 1
    result8 = SalesDetail.objects.filter(MNAME="HY", MClass="實用按摩型")
    for sales_detail in result8:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale8 = sale8 + 1
    result9 = SalesDetail.objects.filter(MNAME="HY", MClass="經濟實惠型")
    for sales_detail in result9:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale9 = sale9 + 1
    result10 = SalesDetail.objects.filter(MNAME="FUJI", MClass="高級豪華型")
    for sales_detail in result10:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale10 = sale10 + 1
    result11 = SalesDetail.objects.filter(MNAME="FUJI", MClass="實用按摩型")
    for sales_detail in result11:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale11 = sale11 + 1
    result12 = SalesDetail.objects.filter(MNAME="FUJI", MClass="經濟實惠型")
    for sales_detail in result12:
        cid = sales_detail.CID
        customer_obj = customer.objects.get(CID=cid)
        if customer_obj.BID == customers:
            sale12 = sale12 + 1
    # 各分店銷售最高型號
    max_sale = max(sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10, sale11, sale12)
    if max_sale == sale1:
        max_sale_name = "OSIM 高級豪華型"
    elif max_sale == sale2:
        max_sale_name = "OSIM 實用按摩型"
    elif max_sale == sale3:
        max_sale_name = "OSIM 經濟實惠型"
    elif max_sale == sale4:
        max_sale_name = "Tokuyo 高級豪華型"
    elif max_sale == sale5:
        max_sale_name = "Tokuyo 實用按摩型"
    elif max_sale == sale6:
        max_sale_name = "Tokuyo 經濟實惠型"
    elif max_sale == sale7:
        max_sale_name = "HY 高級豪華型"
    elif max_sale == sale8:
        max_sale_name = "HY 實用按摩型"
    elif max_sale == sale9:
        max_sale_name = "HY 經濟實惠型"
    elif max_sale == sale10:
        max_sale_name = "FUJI 高級豪華型"
    elif max_sale == sale11:
        max_sale_name = "FUJI 實用按摩型"
    else:
        max_sale_name = "FUJI 經濟實惠型"
    # 當月消費客戶職業分析
    job1 = job2 = job3 = job4 = job5 = job6 = 0
    # 有消費的用戶才列進來 所以使用SalesDetail資料表
    job = SalesDetail.objects.all()
    for job_detail in job:
        cid = job_detail.CID
        customer_obj2 = customer.objects.get(CID=cid)
        if customer_obj2.BID == customers:
            if customer_obj2.COccupation_category == "農林牧業":
                job1 = job1 + 1
            elif customer_obj2.COccupation_category == "金融業":
                job2 = job2 + 1
            elif customer_obj2.COccupation_category == "軍公教":
                job3 = job3 + 1
            elif customer_obj2.COccupation_category == "服務業":
                job4 = job4 + 1
            elif customer_obj2.COccupation_category == "運動員":
                job5 = job5 + 1
            else:
                job6 = job6 + 1
    # 客戶透過何種管道得知本公司
    funct1 = customer.objects.filter(BID=customers, CHow="官方網站").count()
    funct2 = customer.objects.filter(BID=customers, CHow="親友推薦").count()
    funct3 = customer.objects.filter(BID=customers, CHow="廣告").count()
    funct4 = customer.objects.filter(BID=customers, CHow="社群媒體").count()
    funct5 = customer.objects.filter(BID=customers, CHow="搜尋引擎").count()
    funct6 = customer.objects.filter(BID=customers, CHow="其他").count()
    # 優惠卷
    discountnotuse = Coupon.objects.filter(BID=customers, CMON="6", AUse=False).count()
    discountuse = Coupon.objects.filter(BID=customers, CMON="6", AUse=True).count()
    total = discountnotuse + discountuse
    # 客戶偏好產品特色分析
    body = customer.objects.filter(BID=customers, CDemand_description="全身").count()
    leg = customer.objects.filter(BID=customers, CDemand_description="腿部").count()
    shoulder = customer.objects.filter(BID=customers, CDemand_description="肩頸").count()
    waist = customer.objects.filter(BID=customers, CDemand_description="腰部").count()
    perfer = body + leg + shoulder + waist
    # 客戶資料表
    datas = SalesDetail.objects.all()
    data2 = customer.objects.filter(BID=customers)
    # for data in datas:
    #     cid = data.CID
    #     customer_obj3 = customer.objects.get(CID=cid)
    #     if customer_obj3.BID == customers:
    #         person =  customer_obj3.CName
    #         stage = customer_obj3.CStage
    #         product = data.MNAME+"-"+data.MClass
    #         price = data.SPrice
    return render(
        request, 
        'customer.html', {
            'name': name,
            'Newcustomer': Newcustomer, 'Perfer': Perfer, 'Recommend': Recommend,
            'age1': age1, 'age2': age2, 'age3': age3, 'age4': age4, 'age5': age5, 'sum': sum,
            'sale1': sale1, 'sale2': sale2, 'sale3': sale3, 'sale4': sale4, 'sale5': sale5, 'sale6': sale6,
            'sale7': sale7, 'sale8': sale8, 'sale9': sale9, 'sale10': sale10, 'sale11': sale11, 'sale12': sale12,
            'job1': job1, 'job2': job2, 'job3': job3, 'job4': job4, 'job5': job5, 'job6': job6,
            'funct1': funct1, 'funct2': funct2, 'funct3': funct3, 'funct4': funct4, 'funct5': funct5, 'funct6': funct6,
            'discountuse': discountuse, 'discountnotuse': discountnotuse, 'total': total,
            'body': body, 'leg': leg, 'shoulder': shoulder, 'waist': waist, 'perfer': perfer,
            'datas': datas, 'data2': data2, 'max_sale_name': max_sale_name,
            'customers': customers,
            # 'person': person, 'satge': stage, 'product': product, 'price': price
        }
    )

def c2stage(request, customers, Perfer):
    man = customer.objects.filter(BID=customers, CDemand_description=Perfer, CGender="男性").count()
    woman = customer.objects.filter(BID=customers, CDemand_description=Perfer, CGender="女性").count()
    fin = customer.objects.filter(BID=customers, CDemand_description=Perfer, COccupation_category="金融業").count()
    farm = customer.objects.filter(BID=customers, CDemand_description=Perfer, COccupation_category="農林漁業").count()
    sport = customer.objects.filter(BID=customers, CDemand_description=Perfer, COccupation_category="運動員").count()
    other = customer.objects.filter(BID=customers, CDemand_description=Perfer, COccupation_category="其他").count()
    server = customer.objects.filter(BID=customers, CDemand_description=Perfer, COccupation_category="服務業").count()
    unknown = customer.objects.filter(BID=customers, CDemand_description=Perfer, COccupation_category="軍公教").count()
    return render(
        request,
        'c2stage.html', {
            'man': man, 'woman': woman,
            'fin': fin, 'farm': farm, 'sport': sport, 'other': other, 'server': server, 'unknown': unknown
        }
    )

def get_salesperson_data(request):
    salesperson_name = request.GET.get('salesperson')
    salesperson = Salesperson.objects.get(SName=salesperson_name)

    max_value = max(salesperson.SM1, salesperson.SM2, salesperson.SM3)

    if max_value == salesperson.SM1:
        max_name = "經濟實惠型"
    elif max_value == salesperson.SM2:
        max_name = "實用按摩型"
    elif max_value == salesperson.SM3:
        max_name = "高級豪華型"
    else:
        max_name = ""

    achievement_rate = (salesperson.SQ / salesperson.STQ) * 100

    data = {
        'SR': str(salesperson.SR),
        'SQ': str(salesperson.SQ),
        'achievement_rate': format(achievement_rate, '.2f'),
        'max_name': max_name,
        'SARR': str(salesperson.SARR),
        'SLE': str(salesperson.SLE),
        'SM1': str(salesperson.SM1),
        'SM2': str(salesperson.SM2),
        'SM3': str(salesperson.SM3)
    }
    return JsonResponse(data)

def branch(request):
    return render(request, 'branch.html')


def branch_view(request, branch):
    name_mapping = {
        'S001': '潘於新',
        'S002': '江姜好',
        'S003': '邱汪明',
        'S004': '邱曉愈',
        'S005': '劉心瑀',
        'S006': '劉心成',
        'S007': '李冠郁',
        'S008': '黃盛餘',
        'S009': '黃新衣',
        'S010': '陳大賀',
        'S011': '汪曉明',
        'S012': '陳一新',
    }

    branches = list(Branch.objects.filter(BID=branch, SMON='5').order_by('SID'))
    chairs = MassageChair.objects.filter(BID=branch)
    
    sids = []
    sacs = []
    snsales = []
    for branch_obj in branches:
        sid = branch_obj.SID
        sids.append(sid)
        sacs.append(branch_obj.SAc)
        snsales.append(branch_obj.SNSALE)
    
    names = [name_mapping.get(sid, '') for sid in sids]
    
    if branch_obj:
        branch_name = branch_obj.BName
    else:
        branch_name = ""
        
    sac_sum = sum(sacs)
    stc_sum = Branch.objects.filter(BID=branch, SMON='5').aggregate(stc_sum=Sum('STc'))['stc_sum']

    if stc_sum is None:
        return render(request, 'branch.html', {'branch_code': branch})

    achieved_percent = int((sac_sum / stc_sum) * 100)
    not_achieved_percent = 100 - achieved_percent

    new_sum = 0
    old_sum = 0
    branch_obj = Branch.objects.filter(BID=branch).first()
    if branch_obj:
        new_sum = branch_obj.SNew
        old_sum = branch_obj.SOld
    data3 = list(profit.objects.filter(BID=branch, year=2022).values_list('one', 'two', 'three', 'four', 'five', 'six').first())
    data4 = list(profit.objects.filter(BID=branch, year=2023).values_list('one', 'two', 'three', 'four', 'five', 'six').first())

    diff_6 = data4[5] - data3[5] + 12
    diff_5 = data4[4] - data3[4]
    diff_4 = data4[3] - data3[3]
    diff_3 = data4[2] - data3[2]
    diff_2 = data4[1] - data3[1]

    context = {
        'branch_code': branch,
        'names': names,
        'branch_name': branch_name,
        'sacs': sacs,
        'achieved_percent': achieved_percent,
        'not_achieved_percent': not_achieved_percent,
        'new_percent': new_sum / (new_sum + old_sum),
        'old_percent': old_sum / (new_sum + old_sum),
        'data3': data3,
        'data4': data4,
        'diff_6': diff_6,
        'diff_5': diff_5,
        'diff_4': diff_4,
        'diff_3': diff_3,
        'diff_2': diff_2,
        'sids_array': sids,
        'snsales_array': snsales,
        'chairs': chairs,
    }

    return render(request, 'branch.html', context)
# 按摩椅儀表板
def chair(request):
    purch = purchase.objects.all()
    # 品牌銷售
    FUJI = SalesDetail.objects.filter(MNAME="FUJI").count()
    HY = SalesDetail.objects.filter(MNAME="HY").count()
    Tokuyo = SalesDetail.objects.filter(MNAME="Tokuyo").count()
    OSIM = SalesDetail.objects.filter(MNAME="OSIM").count()
    brand = FUJI + HY + Tokuyo + OSIM
    # 型號銷售
    # 獲取所有資料
    all_data = SalesDetail.objects.all()
    # 計算同名稱資料的筆數並按照筆數排序
    data_counts = {}
    for data in all_data:
        if data.MClass in data_counts:
            data_counts[data.MClass] += 1
        else:
            data_counts[data.MClass] = 1
    sorted_data_counts = sorted(data_counts.items(), key=lambda x: x[1], reverse=True)
    # data_counts = SalesDetail.objects.values('MClass').annotate(count=Count('MClass')).order_by('-count')
    # 滿意度調查
    satisfaction1 = Satisfaction.objects.filter(Brand="HY", Feedback="滿意").count()
    satisfaction2 = Satisfaction.objects.filter(Brand="HY", Feedback="不滿意").count()
    satisfaction3 = Satisfaction.objects.filter(Brand="FUJI", Feedback="滿意").count()
    satisfaction4 = Satisfaction.objects.filter(Brand="FUJI", Feedback="不滿意").count()
    satisfaction5 = Satisfaction.objects.filter(Brand="Tokuyo", Feedback="滿意").count()
    satisfaction6 = Satisfaction.objects.filter(Brand="Tokuyo", Feedback="不滿意").count()
    satisfaction7 = Satisfaction.objects.filter(Brand="OSIM", Feedback="滿意").count()
    satisfaction8 = Satisfaction.objects.filter(Brand="OSIM", Feedback="不滿意").count()
    if request.method == 'POST':
        purchaseform = PurchaseForm(request.POST)
        if purchaseform.is_valid():
            purchaseform.save()
            return redirect('chair')
    else:
        purchaseform = PurchaseForm()
    return render(request, 'chair.html', {
        'purch': purch, 'data_counts': sorted_data_counts,
        'FUJI': FUJI, 'HY': HY, 'Tokuyo': Tokuyo, 'OSIM': OSIM, 'brand': brand,
        'satisfaction1': satisfaction1, 'satisfaction2': satisfaction2, 'satisfaction3': satisfaction3,
        'satisfaction4': satisfaction4, 'satisfaction5': satisfaction5, 'satisfaction6': satisfaction6,
        'satisfaction7': satisfaction7, 'satisfaction8': satisfaction8,
        'purchaseform': purchaseform
        }
    )

def satisfaction_form(request):
    if request.method == 'POST':
        satform = SatisfactionForm(request.POST)
        if satform.is_valid():
            satform.save()
            return redirect('chair')
    else:
        satform = SatisfactionForm()
    return render(request, 'test2.html', {
        'satform': satform,
        }
    )