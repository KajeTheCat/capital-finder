from http.server import BaseHTTPRequestHandler
import requests


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    r = requests.get('https://restcountries.com/#rest-countries')

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "The capital of X is Y"
    self.wfile.write(message.encode())
    return