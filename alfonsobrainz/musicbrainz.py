import requests

try:
    import requests_cache

    requests_cache_available = True
except ImportError:
    requests_cache_available = False

from alfonsobrainz.rate_limit import rate_limited


class Alfonsobrainz(object):
    def __init__(self):
        self.user_agent = 'alfonsobrainz'
        self.hostname = 'https://musicbrainz.org'
        self.requests_per_second = 2

    # TODO: Perfect this method - it doesn't give any completion hints...
    def enable_caching(self, args, **kwargs):
        if requests_cache_available:
            requests_cache.install_cache(args, **kwargs)

    def get_area_by_id(self, mbid, includes=[]):
        return self._send_query('area', mbid, includes)

    def get_artist_by_id(self, mbid, includes=[]):
        return self._send_query('artist', mbid, includes)

    def get_label_by_id(self, mbid, includes=[]):
        return self._send_query('label', mbid, includes)

    def get_place_by_id(self, mbid, includes=[]):
        return self._send_query('place', mbid, includes)

    def get_recording_by_id(self, mbid, includes=[]):
        return self._send_query('recording', mbid, includes)

    def get_release_by_id(self, mbid, includes=[]):
        return self._send_query('release', mbid, includes)

    def get_release_group_by_id(self, mbid, includes=[]):
        return self._send_query('release-group', mbid, includes)

    def get_work_by_id(self, mbid, includes=[]):
        return self._send_query('work', mbid, includes)

    def _send_query(self, entity, mbid, includes=[]):
        if not isinstance(includes, list):
            includes = [includes]

        # TODO: Check to see if includes are valid

        args = {}

        if includes.__len__() > 0:
            args['inc'] = ' '.join(includes)

        path = '%s/%s' % (entity, mbid)

        return self._send_get_request(path, args)

    def _generate_url(self, path):
        return '%s/ws/2/%s' % (self.hostname, path)

    @rate_limited(2)
    def _send_get_request(self, path, params):
        headers = {'User-Agent': self.user_agent}

        params['fmt'] = 'json'

        return requests.get(self._generate_url(path), params=params, headers=headers).json()