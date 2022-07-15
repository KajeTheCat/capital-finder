from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

  # http://localhost:3000/api/define?word=python

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "state" in dic:
            url = "https://restcountries.com/#rest-countries"
            r = requests.get(url + dic["state"])
            data = r.json()
            capitals = []
            for state_data in data:
                capital = state_data["states"][0]["capitals"][0]["capital"]
                capitals.append(capital)
            message = str("the capital of "state " is " capital)

        else:
            message = "Give me a state or capital"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return