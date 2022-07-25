import requests
from tenacity import retry, wait_exponential, stop_after_attempt

store_hash = "rtmh8fqr05"
access_token = 'hzu9e8qa8zhz7hojmzx5pzcwxncktf8'
base_url = "https://api.bigcommerce.com/stores"


class BCCustomer:

    def __init__(self):
        self.session = requests.session()
        self.headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
            "X-Auth-Token": access_token
        }

    @retry(reraise=True, wait=wait_exponential(multiplier=1, max=60), stop=stop_after_attempt(5))
    def get_a_customer(self, customer_id):
        url = f"{base_url}/{store_hash}/v2/customers/{customer_id}"
        resp = self.session.get(url, headers=self.headers)
        if resp.status_code != 200:
            return False
        return resp.json()


# class AsyncBCCustomer:
#
#     def __init__(self):
#         self.headers = {
#             "Content-Type": "application/json",
#             "accept": "application/json",
#             "X-Auth-Token": access_token
#         }
#
#     @retry(reraise=True, wait=wait_exponential(multiplier=1, max=60), stop=stop_after_attempt(5))
#     async def get_a_customer(self, customer_id):
#         url = f"{base_url}/{store_hash}/v2/customers/{customer_id}"
#         async with httpx.AsyncClient() as client:
#             resp = await client.get(url, headers=self.headers)
#             if resp.status_code != 200:
#                 return False
#             return resp.json()
