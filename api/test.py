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

        # if "country" in dic:
        #     url = f"https://restcountries.com/v3.1/name/{dic["country"]}?fullText=true"
        #     r = requests.get(url)
        #     data = r.json()
        #     capitals = []
        #     for country_data in data:
        #       capital = country_data["countries"][0]["capitals"][0]["capital"]
        #       capitals.append(capital)
        #     message = str(data)

        # else:
        message = "search a country"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return