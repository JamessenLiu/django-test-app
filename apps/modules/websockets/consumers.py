from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class DeployResult(AsyncWebsocketConsumer):

    async def connect(self):
        socket_id = self.scope['url_route']['kwargs']['socket_id']
        socket_group = 'chat_%s' % socket_id
        await self.channel_layer.group_add(
            socket_group,
            self.channel_name
        )

        await self.accept()

        await self.send(text_data=json.dumps({
            'code': 200,
            'message': "success",
            'data': {}
        }))

    async def system_message(self, event):
        """
        Receive message from socket group
        """
        message = event['message']
        await self.send(text_data=json.dumps({
            'code': message.get('code'),
            'message': message.get('message'),
            'data': message.get('data')
        }))

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        await self.send(text_data="收到信息")


def send_group_msg(socket_id, message):
    """
    send message out of channels
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'chat_{socket_id}',
        {
            "type": "system_message",
            "message": message,
        }
    )