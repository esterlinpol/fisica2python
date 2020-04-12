from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

valor = "hola"
valor2 = "40"
valor3 = "50"
valor4 = "20"
valor5 = "not found"
class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            process = open(self.path[1:]).read()
            
        if self.path == '/flow':
            process = valor2
        if self.path == '/sonar1':
            process = valor3
        if self.path == '/sonar2':
            process = valor4                         
        try:
            response = process
            self.send_response(200)
        except:
            response = "not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(response))


httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
