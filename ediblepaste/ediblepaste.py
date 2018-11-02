import requests
import json
from . import config
from .exception import APIError

class EdiblePaste():
    def __init__(self):
        """Initializes the class"""
        self.pastebin_url = config.PASTEBIN_URL
        self.gist_url = config.GIST_URL
        self._session = requests.Session()


    def _request(self, function, params, service):
        # Determine the base_url based on the service that is being requested
        base_url = {
            'pastebin': self.pastebin_url
            'gist': self.gist_url
        }.get(service)

        # Send the request
        try:
            data = self._session.get(base_url + function)
        except Exception:
            raise APIError('Unable to connect to service')

        # Parse the text into JSON
        try:
            data = data.json()
        except ValueError:
            raise APIError('Unable to parse JSON response')

        return data


    def pastes(self, limit=250):
        """Scrape pastes from pastebin.com"""
        params = {
            'limit': limit,
        }
        return self._request('/api_scraping.php', params, service='pastebin')


    def gists(self, per_page=100):
        """Scrape gists from github.com"""
        params = {
            'per_page': per_page,
        }
        r = self._request('/gists', params, service='gist')

        for gist_meta in r:
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


    def raw(self, scrape_url):
        """Get raw data from scrape url"""
        return requests.get(scrape_url).text
