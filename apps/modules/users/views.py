from rest_framework.views import APIView
from rest_framework.response import Response
from apps.utils.bc_requests import BCCustomer


class CustomersView(APIView):

    authentication_classes = ()

    def get(self, request):
        bc_customer = BCCustomer()
        customer_ids = [6, 7, 9, 10, 12, 13]
        customers = []
        # for customer_id in customer_ids:
        #     customer = bc_customer.get_a_customer(customer_id)
        #     customers.append(customer)

        from concurrent.futures import ThreadPoolExecutor

        with ThreadPoolExecutor(max_workers=10) as exe:
            results = exe.map(bc_customer.get_a_customer, customer_ids)
            for result in results:
                if result:
                    customers.append(result)

        # customers = async_to_sync(self.get_bc_customer(customer_ids)).awaitable

        return Response({
            'code': 200,
            'data': customers
        })

    # @async_to_sync
    # async def get_bc_customer(self, customer_ids):
    #     from apps.utils.bc_requests import AsyncBCCustomer
    #     import asyncio
    #     bc_customer = AsyncBCCustomer()
    #     tasks = [bc_customer.get_a_customer(customer_id) for customer_id in customer_ids]
    #     result = await asyncio.gather(*tasks)
    #     return result
