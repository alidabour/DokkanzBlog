from channels.routing import route
from blogapp.consumers import ws_post_list_update, ws_connect, ws_disconnect,ws_post_connect,ws_post_disconnect,ws_post_update


channel_routing = [
    route('websocket.connect', ws_connect,path=r"/blog_list/"),
    route('websocket.connect',ws_post_connect,path=r"/blog_detail/(?P<post_id>[0-9]+)/$"),
    route('websocket.receive',ws_post_list_update,path=r"/blog_list/"), 
    route('websocket.disconnect',ws_post_disconnect,path=r"/blog_detail/(?P<post_id>[0-9]+)/$"),
    route('websocket.receive',ws_post_update,path=r"/blog_detail/(?P<post_id>[0-9]+)/$"), 
    route('websocket.disconnect', ws_disconnect),
]
