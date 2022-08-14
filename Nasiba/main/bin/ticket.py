import django
import os
import sys
import requests

directory = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(1, directory)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nasiba.settings")

django.setup()

from main.models import Trakoneshs

under_test = requests.get(
    "https://newsepasa.na30ba.ir/v1/credit/merchant/transaction-list/",
    params={'filter_id__gt': "3111", "filter_terminal__merchant__merchant_id": 1111188822,
            "page_size": 10, "order_by": "id"},
    headers={
        "Authorization": "Token client:xkMWWuLlnXdwusEJbjSk06kWSmHZ6fawp8nT7lmDSbsvs/07W8VuW9EToZtx1YxaSw1Ko2jttyTI5cVD"},
)

under_json = under_test.json()
under = under_json["results"]

if under:
    for i in under:
        start = 3111
        response = requests.get(
            "https://newsepasa.na30ba.ir/v1/credit/merchant/transaction-list/",
            params={'filter_id__gt': start, "filter_terminal__merchant__merchant_id": 1111188822,
                    "page_size": 10, "order_by": "-id"},
            headers={
                "Authorization": "Token client:xkMWWuLlnXdwusEJbjSk06kWSmHZ6fawp8nT7lmDSbsvs/07W8VuW9EToZtx1YxaSw1Ko2jttyTI5cVD"},
        )

        responsejson = response.json()
        trx_id1 = responsejson["results"][0]["contract"]

        response2 = requests.get(
            "https://newsepasa.na30ba.ir/v1/wallet/user/",
            params={"filter_contract__id": 1891},
            headers={
                "Authorization": "Token client:xkMWWuLlnXdwusEJbjSk06kWSmHZ6fawp8nT7lmDSbsvs/07W8VuW9EToZtx1YxaSw1Ko2jttyTI5cVD"},
        )

        response2json = response2.json()
        cellphone1 = response2json["results"][0]["cellphone"]

        response3 = requests.post(
            "https://newsepasa.na30ba.ir/v1/campaign/send-sms/",
            headers={
                "Authorization": "Token client:xkMWWuLlnXdwusEJbjSk06kWSmHZ6fawp8nT7lmDSbsvs/07W8VuW9EToZtx1YxaSw1Ko2jttyTI5cVD"},
            json={
                "mobile": "09022562088",
                "template": "cinemaTest",
                "params": {"param1": "code1"},
            },
        )

        code1 = "code"

        response3json = response3.json()
        campaign_id = response3json["campaign_id"]
        start = start + 1
        Trakoneshs.objects.create(
            id1=start, code=code1, trx_id=trx_id1, cellphone=cellphone1)
        print("ok!")
