import csv
from .models import Companies
from apps.modules.websockets.consumers import send_group_msg


def export_all_companies():
    companies = Companies.objects.all().values()
    with open('company.csv', 'w', encoding='utf-8') as fp:
        company_file = csv.DictWriter(fp, fieldnames=['name', 'email'])
        company_file.writeheader()
        for company in companies:
            company_file.writerow({
                "name": company['name'],
                "email": company['email']
            })
    send_group_msg("9527", {
        "code": 200,
        "message": "success",
        "data": {
            "company_csv_path": "/api/companies/export"
        }
    })
    return
