from django.urls import path
from apps.modules.companies.views import CompaniesView, CompaniesExportView
from apps.modules.users.views import CustomersView

urlpatterns = [
    path('companies', CompaniesView.as_view()),
    path('customers', CustomersView.as_view()),
    path('companies/export', CompaniesExportView.as_view())
]
