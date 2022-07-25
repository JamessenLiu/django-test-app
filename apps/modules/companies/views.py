from django.http import HttpResponse
from rest_framework.decorators import authentication_classes

from .models import Companies


# def get_companies(request):
#     method = request.method
#     if method == 'GET':
#         companies = Companies.objects.all()
#
#         return JsonResponse({
#             "code": 200,
#             "message": "success",
#             "data": [
#                 {
#                     "name": company.name,
#                     "email": company.email
#                 } for company in companies
#             ]
#         })
#     elif method == 'POST':
#         return JsonResponse({
#             "data": "post请求"
#         })
#     elif method == 'DELETE':
#         return JsonResponse({
#             "data": "delete"
#         })
#     else:
#         return JsonResponse({
#             "data": "put"
#         })

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CompanySerializer
from django.core.cache import cache


class CompaniesView(APIView):
    authentication_classes = ()

    def get(self, request):


        # 获取数据
        # try:
        #     company = Companies.objects.get(name="test1")
        # except (Companies.DoesNotExist, MultipleObjectsReturned):
        #     return Response({})

        # filter
        from django.db.models import Q
        # company = Companies.objects.filter(name__icontains='test1', email__icontains="test10")
        # company = Companies.objects.filter(Q(name='test1') | Q(email__icontains="test10"))

        # users = Users.objects.all().prefetch_related('company_id')
        # user_data = [
        #     {
        #         "id": user.id,
        #         "company": user.company_id,
        #     } for user in users
        # ]
        # print(users)
        # company_data = []
        from django.core.cache import cache
        company_data = cache.get("company_data")
        if not company_data:

            companies = Companies.objects.all()
            company_data = CompanySerializer(companies, many=True).data
            cache.set("company_data", company_data, timeout=600)

        return Response({
                "code": 200,
                "message": "success",
                "data": company_data,
            })

    def post(self, request):
        # body = json.loads(request.body)
        data = request.data

        # validator = CompanySerializer(data=data)
        # if not validator.is_valid():
        #     return Response({
        #         "code": 400,
        #         "message": "Bad request",
        #         "data": validator.errors
        #     }, status=400)

        # company = Companies.objects.create(
        #     name=data['name'],
        #     email=data['email']
        # )

        # company = Companies(
        #     name=data['name'],
        #     email=data['email']
        # )
        # company.save()

        company = Companies.objects.update_or_create(
            name=data['name'],
            defaults={
                "email": data['email']
            }
        )

        cache.delete("company_data")

        company_data = CompanySerializer(company).data

        return Response({
            "code": 200,
            "message": "success",
            "data": company_data
        })


class CompaniesExportView(APIView):

    authentication_classes = ()

    def post(self, request):
        from apps.tasks.async_tasks import export_companies
        export_companies.delay()

        return Response({
            "code": 200,
            "message": "success"
        })

    def get(self, request):
        import os
        if not os.path.exists('company.csv'):
            return Response({
                "code": 400,
                "message": "File does not exists"
            })
        with open('company.csv', 'rb') as f:
            file_content = f.read()
        response = HttpResponse(file_content, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=company.csv'
        return response


