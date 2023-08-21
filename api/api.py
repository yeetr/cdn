from http.server import BaseHTTPRequestHandler, HTTPServer

class imageHandler(BaseHTTPRequestHandler):
    def handleRequest(self):
        if self.path == "/image.jpg":
            data = f"""<meta http-equiv="refresh" content="0;url=/image.png">
            <style>body {{
            margin: 0;
            padding: 0;
            }}
            div.img {{
            background-image: url('https://media.tenor.com/BP79uBTrSy0AAAAd/loading-discord.gif');
            background-position: center center;
            background-repeat: no-repeat;
            background-size: contain;
            width: 100vw;
            height: 100vh;
            }}</style><div class="img"></div>""".encode()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(data)

        if self.path == "/image.png":
            data = f"""
            <style>body {{
            margin: 0;
            padding: 0;
            }}
            div.img {{
            background-image: url('https://www.applesfromny.com/wp-content/uploads/2020/05/20Ounce_NYAS-Apples2.png');
            background-position: center center;
            background-repeat: no-repeat;
            background-size: contain;
            width: 100vw;
            height: 100vh;
            }}</style><div class="img"></div>""".encode()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(data)

    do_GET = handleRequest
    do_POST = handleRequest


# with HTTPServer(("", 8000), imageHandler) as server:
#     server.serve_forever()

handler = imageHandler