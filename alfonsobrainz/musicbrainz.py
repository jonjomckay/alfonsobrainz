import requests

VERSION = '0.5'

def get_version():
    return VERSION

def get_recording_by_id(mbid, includes=[]):
    return _send_query('recording', mbid, includes)

def _generate_url(path):
    return 'https://musicbrainz.org/ws/2/%s' % path

def _send_query(entity, mbid, includes=[]):
    if not isinstance(includes, list):
        includes = [includes]

    # TODO: Check to see if includes are valid

    args = {}

    if includes.__len__() > 0:
        args['inc'] = ' '.join(includes)

    path = '%s/%s' % (entity, mbid)

    return _send_get_request(path, args)

def _send_get_request(path, params):
    params['fmt'] = 'json'

    return requests.get(_generate_url(path), params=params).json()