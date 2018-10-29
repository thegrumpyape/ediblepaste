import requests
import json
from . import config

class EdiblePaste():
    def __init__(self):
        self.pastebin_url = config.PASTEBIN_URL
        self.gist_url = config.GIST_URL
        self.limit = config.LIMIT

    def get_pastes(self):
        r = requests.get('{0}?limit={1}'.format(self.pastebin_url, self.limit))
        return r.json()

    def get_paste_raw(self, scrape_url):
        return requests.get(scrape_url).text

    def get_gists(self):
        gists = []
        r = requests.get('{}/gists?per_page={}'.format(self.gist_url, self.limit))

        for gist_meta in r.json():
            for file_name, file_meta in gist_meta["files"].items():
                gist_data = {}
                gist_data['scrape_url'] = file_meta['raw_url']
                gist_data['full_url'] = gist_meta['html_url']
                gist_data['date'] = gist_meta['created_at']
                gist_data['key'] = gist_meta['id']
                gist_data['size'] = file_meta['size']
                gist_data['expire'] = 0
                gist_data['title'] = file_name
                gist_data['syntax'] = file_meta['type']
                gist_data['user'] = gist_meta['user']
                gists.append(gist_data)

        return gists

    def get_gist_raw(self,scrape_url):
        return requests.get(scrape_url).text
