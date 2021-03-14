from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Companies


def blackbox(request):
    if request.method == 'POST':
        button1 = ""
        button2 = ""
        button3 = ""
        button4 = ""
        button5 = ""
        button6 = ""
        if request.POST.get('Submit') == 'button-1':
            user_variable = request.POST.get('button1')
            try:
                user_int = int(user_variable)
                if user_int >= 100 and user_int <= 1000:
                    result = user_int
                else:
                    result = "Wartosc niepoprawna"
            except ValueError:
                result = "Wartosc nie jest liczbą"
            button1 = result
        elif request.POST.get('Submit') == 'button-2':
            user_variable = request.POST.get('button2')
            try:
                user_int = int(user_variable)
                if user_int >= 100:
                    result = user_int
                else:
                    result = "Wartosc niepoprawna"
            except ValueError:
                result = "Wartosc nie jest liczbą"
            button2 = result
        elif request.POST.get('Submit') == 'button-3':
            base_price = 10
            user_variable = request.POST.get('button3')
            try:
                user_int = int(user_variable)
                if user_int <= 0:
                    result = "Musisz zamówić no najmniej 1 sztukę"
                elif user_int > 0 and user_int <= 5:
                    result = user_int * base_price
                elif user_int > 5 and user_int and user_int < 50:
                    result = "{0} + darmowa dostawa".format(user_int * base_price)
                elif user_int >= 50 and user_int <= 99:
                    result = "{0} + darmowa dostawa".format(user_int * base_price * 0.9)
                elif user_int > 99:
                    result = "Nie można zmówić więcej niż 99 sztuk"
                else:
                    result = "Liczba sztuk jest niepoprawna."
            except ValueError:
                result = "Wartosc nie jest liczbą"
            button3 = result
        elif request.POST.get('Submit') == 'button-4':
            base_price = 10
            user_variable = request.POST.get('button4')
            user_int = int(user_variable)
            if user_int <= 0:
                result = "Musisz zamówić no najmniej 1 sztukę"
            elif user_int > 0 and user_int <= 5:
                result = user_int * base_price
            elif user_int > 5 and user_int and user_int < 50:
                result = "{0} + darmowa dostawa".format(user_int * base_price)
            elif user_int > 50 and user_int <= 99:
                result = "{0} + darmowa dostawa".format(user_int * base_price * 0.9)
            elif user_int > 99:
                result = "Nie można zmówić więcej niż 99 sztuk"
            else:
                result = "Liczba sztuk jest niepoprawna."
            button4 = result
        elif request.POST.get('Submit') == 'button-5':
            param1 = request.POST['param1']
            param2 = request.POST['param2']
            param3 = request.POST['param3']
            param4 = request.POST['param4']
            if param1 =='YES' and param2 == 'YES' and param3 == 'YES' and param4 == 'YES':
                result = "TAK"
            else:
                result = "NIE"
            button5 = result
        elif request.POST.get('Submit') == 'button-6':
            param1 = request.POST['param1']
            param2 = request.POST['param2']
            param3 = request.POST['param3']
            param4 = request.POST['param4']
            if param1 =='YES' and param2 == 'YES' and param3 == 'YES':
                result = "TAK"
            else:
                result = "NIE"
            button6 = result
        else:
            pass
        context = {
            'button1': button1,
            'button2': button2,
            'button3': button3,
            'button4': button4,
            'button5': button5,
            'button6': button6
            }
        return render(request, 'tutorial/blackbox.html', context)
    else:
        context = {'button1': ''}
        return render(request, 'tutorial/blackbox.html', context)


def blackbox_results(request):
    context = {'button1': ''}
    return render(request, 'tutorial/blackbox_results.html', context)


def stan1(request):
    var1 = request.GET.get('var1', 'a')
    context = {
        "var1": var1
    }
    return render(request, 'tutorial/stan1.html', context)


def stan2(request):
    var1 = request.GET.get('var1', 'a')
    context = {
        "var1": var1
    }
    return render(request, 'tutorial/stan2.html', context)


def stan3(request):
    var1 = request.GET.get('var1', 'a')
    context = {
        "var1": var1
    }
    return render(request, 'tutorial/stan3.html', context)


def stan4(request):
    var1 = request.GET.get('var1', 'a')
    context = {
        "var1": var1
    }
    return render(request, 'tutorial/stan4.html', context)


def stan5(request):
    var1 = request.GET.get('var1', 'a')
    context = {
        "var1": var1
    }
    return render(request, 'tutorial/stan5.html', context)


def use_case_login(request):
    if request.method == 'POST':
        user_login = request.POST.get('email', '')
        user_pass = request.POST.get('pass', '')
        if user_login == 'admin@admin' and user_pass == "admin":
            return HttpResponseRedirect('use_case_home')
        else:
            var1 = request.GET.get('var1', 'a')
            error = "bad credentials"
            context = {
                "var1": var1,
                "error": error
            }
            return render(request, 'tutorial/use_case_login.html', context)
    else:
        var1 = request.GET.get('var1', 'a')
        error = ""
        context = {
            "var1": var1,
            "error": error
        }
        return render(request, 'tutorial/use_case_login.html', context)


def use_case_home(request):
    if request.method == 'POST':
        pass
    else:
        var1 = request.GET.get('var1', 'a')
        error = ""
        companies_list = Companies.objects.all()
        context = {
            "var1": var1,
            "error": error,
            "companies_list": companies_list
        }
        return render(request, 'tutorial/use_case_home.html', context)


def use_case_add_invoice(request):
    if request.method == 'POST':
        error = "Faktura dodana poprawnie"
        var1 = request.POST.get("company_id")
        company_info = Companies.objects.get(pk=var1)
        context = {
            "error": error,
            "company_info": company_info
        }
        return render(request, 'tutorial/use_case_add_invoice.html', context)
    else:
        error = ""
        company_info = ""
        var1 = request.GET.get('pk', '')
        if var1 != '':
            company_info = Companies.objects.get(pk=var1)
        context = {
            "var1": var1,
            "company_info": company_info
        }
        return render(request, 'tutorial/use_case_add_invoice.html', context)


def use_case_add_company(request):
    if request.method == 'POST':
        company_name = request.POST.get('text1', '')
        company_nip = request.POST.get('text2', '')
        var1 = 'a'
        if company_name != '' and company_nip != '':
            try:
                int(company_nip)
                if len(company_nip) > 10:
                    error = "NIP jest za długi"
                elif len(company_nip) < 10:
                    error = "NIP jest za krótki"
                else:
                    Companies.objects.create(company_name=company_name, company_nip=company_nip)
                    error = "Firma poprawnie dodana do bazy"
            except ValueError:
                error = "Nip musi być liczbą"
        else:
            error = "Nazwa firmy i NIP nie mogą być puste"
        context = {
            "var1": var1,
            "error": error
        }
        return render(request, 'tutorial/use_case_add_company.html', context)
    else:
        var1 = request.GET.get('var1', 'a')
        error = ""
        context = {
            "var1": var1,
            "error": error
        }
        return render(request, 'tutorial/use_case_add_company.html', context)


def web_apps(request):
    if request.method == 'POST':
        context = {'data': ''}
        if request.POST.get('Submit') == 'admin':
            print(request)
            context['data'] = 'Admin credentials: Admin/admin'
            print(context)
        return render(request, 'tutorial/web_apps.html', context)
    else:
        context = {'data': ''}
        return render(request, 'tutorial/web_apps.html', context)
