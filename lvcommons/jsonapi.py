import urllib3, certifi, json
from urllib3.util.timeout import Timeout

_pool_manager = None


def setup_pool_manager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(), timeout=Timeout(connect=6), retries=10,
                       **kwargs):
    global _pool_manager
    _pool_manager = urllib3.PoolManager(cert_reqs=cert_reqs, ca_certs=ca_certs, timeout=timeout, retries=retries,
                                        **kwargs)


def raw_request(url, method, data=None, authorization=None, extra_headers=None):
    h = {}
    if authorization:
        h['Authorization'] = authorization
    if extra_headers and isinstance(extra_headers, dict):
        h = dict(h, **extra_headers)
    res = _pool_manager.request(method=method, url=url, fields=data, headers=h, encode_multipart=False)
    return res


def request(url, method, data=None, authorization=None, extra_headers={}):
    new_headers = dict(extra_headers, Accept='application/json')
    res = raw_request(url, method, data, authorization, new_headers)
    str_res = res.data
    if str_res:
        if hasattr(str_res, 'decode'):
            str_res = str_res.decode()
        json_res = json.loads(str_res)
        res.json_data = json_res
    else:
        res.json_data = None
    return res


def get(url, data=None, authorization=None, extra_headers={}):
    return request(url, 'GET', data, authorization, extra_headers)


def post(url, data=None, authorization=None, extra_headers={}):
    return request(url, 'POST', data, authorization, extra_headers)


def post_form(url, data=None, authorization=None, extra_headers={}):
    new_headers = dict(extra_headers, **{'Content-Type': 'application/x-www-form-urlencoded'})
    return request(url, 'POST', data, authorization, new_headers)


def post_json(url, data=None, authorization=None, extra_headers={}):
    new_headers = dict(extra_headers, **{'Content-Type': 'application/json'})
    return request(url, 'POST', data, authorization, new_headers)


setup_pool_manager()