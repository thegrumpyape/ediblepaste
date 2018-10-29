import requests
import json
from . import config

class EdiblePaste():
    def __init__(self):
        """Initializes the class"""
        self.pastebin_url = config.PASTEBIN_URL
        self.gist_url = config.GIST_URL
        self.limit = config.LIMIT

    def scrape(self):
        """Scrapes all sites for paste data"""
        pastes = self.get_pastes() + self.get_gists()
        for paste in pastes:
            paste['raw_paste'] = self.get_raw(paste['scrape_url'])
        return pastes

    def get_pastes(self):
        """Scrape pastes from pastebin.com"""
        r = requests.get('{0}?limit={1}'.format(self.pastebin_url, self.limit))
        return r.json()

    def get_gists(self):
        """Scrape gists from github.com"""
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

    def get_raw(self, scrape_url):
        """Get raw data from scrape url"""
        return requests.get(scrape_url).text
