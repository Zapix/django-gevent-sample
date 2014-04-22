# -*- coding: utf-8 -*-
import json

from django import http
from django.conf import settings

import gevent
import zmq.green as zmq

from socketio import socketio_manage
from socketio.namespace import BaseNamespace

context = zmq.Context()


def listener(socketio):
    """
    Connects to zmq.PUB as subscriber and listening for
    messages with id.
    :param socketio: socketio for sending message
    """
    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://127.0.0.1:%d' % settings.AGENT_TO_DJANGO_PORT)
    subscriber.setsockopt(zmq.SUBSCRIBE, "django")
    socketio.send(json.dumps({'status': 'connected'}))
    while True:
        message = subscriber.recv()
        if message:
            socketio.send(json.dumps({"message":message.split(":")[1]}), json=True)


class RandomNamespace(BaseNamespace):
    """
    Namespace for working client with devices backend
    """
    def recv_message(self, msg):
        self.handle_received_json(json.loads(msg))

    def handle_received_json(self, data):
        action = data.get('action')
        method = getattr(self, action)
        method(data)

    def subscribe(self, data):
        gevent.spawn(listener, self)


def socketio(request):
    socketio_manage(
        request.environ,
        {'': RandomNamespace},
        request=request
    )
    return http.HttpResponse()
