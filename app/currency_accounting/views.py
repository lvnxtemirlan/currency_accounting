from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CurrencyInfo
from django.core import serializers



@csrf_exempt
def page(request, template="currency_accounting/main.html"):
    return render(request, template, {})


@csrf_exempt
def show_table(request):
    # print(request.POST)
    data = {
        "first": {"row1": "Перечислены денежные средства с валютного счета для продажи иностранной валюты (для конвертации долларов в тенге) по рыночному курсу",
                  "row2": "Зачислены денежные средства на тенговый счет по курсу обслуживающего банка",
                  "row3": "Признаны расходы по суммовой разнице",
                  "row4": "Признаны доходы по суммовой разнице"
                  }
    }
    if request.method == "POST":
        print(request.POST)
        create = request.POST.get("type")
        bank_currency = float(request.POST.get("bank_currency").replace(",", "."))
        market_currency = float(request.POST.get("market_currency").replace(",", "."))
        value = float(request.POST.get("value").replace(" ", ""))
        print(create, bank_currency, market_currency, value)
        try:
            info = CurrencyInfo(
                bank_currency=bank_currency,
                market_currency=market_currency,
                value=value
            )
            info.save()
            return JsonResponse({"success": 1})
        except Exception as e:
            print(e)
            return JsonResponse({"success": 0})

    currency_info = CurrencyInfo.objects.all() # noqa
    serialized_currency_info = json.loads(serializers.serialize("json", currency_info))
    for cur in serialized_currency_info:

        cur["fields"]["row1"] = data["first"]["row1"]
        cur["fields"]["row2"] = data["first"]["row2"]

        cur["fields"]["debit1"] = "1020"
        cur["fields"]["credit1"] = "1030/2"
        cur["fields"]["debit2"] = "1030/1"
        cur["fields"]["credit2"] = "1020"
        if cur["fields"]["bank_currency"] < cur["fields"]["market_currency"]:
            cur["fields"]["debit3"] = "7480"
            cur["fields"]["credit3"] = "1020"
            cur["fields"]["row3"] = data["first"]["row3"]
        else:
            cur["fields"]["debit3"] = "1020"
            cur["fields"]["credit3"] = "7480"
            cur["fields"]["row3"] = data["first"]["row4"]
        cur["fields"]["summ1"] = int(cur["fields"]["bank_currency"] * cur["fields"]["value"])
        cur["fields"]["summ2"] = int(cur["fields"]["market_currency"] * cur["fields"]["value"])
        cur["fields"]["summ3"] = int(abs((cur["fields"]["bank_currency"] - cur["fields"]["market_currency"]) * cur["fields"]["value"]))

    return render(request, "currency_accounting/main.html", {
        "currency_info": serialized_currency_info
    })


@csrf_exempt
def delete_table(request, pk):
    currency_info = CurrencyInfo.objects.get(id=pk) # noqa
    currency_info.delete()

    return redirect("/currency/table")