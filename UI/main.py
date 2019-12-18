import tornado.ioloop
import tornado.web
import logging
import Settings
import pathlib
import json
import urllib
from PIL import Image
import io
from  tornado.escape import json_decode
from predict import get_celebrity_matches

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ImageHandler(tornado.web.RequestHandler):
    def post(self):
        print(type(self.request.files))
        image_body = self.request.files['image'][0]['body']

        #img = Image.open(io.BytesIO(image_body))
        celeb_images = get_celebrity_matches(image_body)
        # celeb_images = ['celeb/train/Abdullah_Gul/Abdullah_Gul_0005.jpg', 'celeb/train/Jack_Straw/Jack_Straw_0024.jpg', 'celeb/train/Mahmoud_Abbas/Mahmoud_Abbas_0008.jpg', 'celeb/train/Jack_Straw/Jack_Straw_0026.jpg', 'celeb/train/Wen_Jiabao/Wen_Jiabao_0002.jpg']
        data = {}
        for path in celeb_images:
            data[path] = str(pathlib.Path(path).parent.name)

        res = json.dumps(data)
        self.write(res)

class Application(tornado.web.Application):
    def __init__(self):
        app_settings = {
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
            'default_handler_args': dict(status_code=404),
        }

        app_handlers = [
            (r'^/', MainHandler),
            (r'^/processImage$', ImageHandler)
        ]

        super(Application, self).__init__(app_handlers, **app_settings)

if __name__ == "__main__":
    port = 8000
    address = '0.0.0.0'
    logging_level = logging.getLevelName('INFO')
    logging.getLogger().setLevel(logging_level)
    logging.info('starting event logger on %s:%d', address, port)

    http_server = tornado.httpserver.HTTPServer(
        request_callback=Application(), xheaders=True)
    http_server.listen(port, address=address)

    tornado.ioloop.IOLoop.instance().start()
