import urllib3, certifi, json
from urllib3.util.request import make_headers
from urllib3.util.timeout import Timeout

_pool_manager = None


def setup_pool_manager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(),
                       timeout=Timeout(connect=6), retries=10,
                       **kwargs):
    global _pool_manager
    _pool_manager = urllib3.PoolManager(cert_reqs=cert_reqs, ca_certs=ca_certs,
                                        timeout=timeout, retries=retries,
                                        **kwargs)


def raw_request(url, method, data=None, authorization=None, extra_headers=None,
                basic_auth=False):
    h = {}
    if authorization:
        if basic_auth:
            h = make_headers(basic_auth=authorization)
        else:
            h['Authorization'] = authorization
    if extra_headers and isinstance(extra_headers, dict):
        h = dict(h, **extra_headers)
    res = _pool_manager.request(method=method, url=url, fields=data, headers=h,
                                encode_multipart=False)
    return res


def request(url, method, data=None, authorization=None, extra_headers={},
            basic_auth=False):
    new_headers = dict(extra_headers, Accept='application/json')
    res = raw_request(url, method, data, authorization, new_headers,
                      basic_auth=basic_auth)
    str_res = res.data
    if str_res:
        if hasattr(str_res, 'decode'):
            str_res = str_res.decode()
        res.str_data = str_res
        try:
            json_res = json.loads(str_res)
            res.parsed_data = json_res
        except ValueError:
            res.parsed_data = None
    else:
        res.parsed_data = None
        res.str_data = None
    return res


def get(url, data=None, authorization=None, extra_headers={}, basic_auth=False):
    return request(url, 'GET', data, authorization, extra_headers,
                   basic_auth=basic_auth)


def post(url, data=None, authorization=None, extra_headers={}, basic_auth=False):
    return request(url, 'POST', data, authorization, extra_headers,
                   basic_auth=basic_auth)


def post_form(url, data=None, authorization=None, extra_headers={},
              basic_auth=False):
    new_headers = dict(extra_headers,
                       **{'Content-Type': 'application/x-www-form-urlencoded'})
    return post(url, data, authorization, new_headers, basic_auth=basic_auth)


def post_json(url, data=None, authorization=None, extra_headers={},
              basic_auth=False):
    new_headers = dict(extra_headers, **{'Content-Type': 'application/json'})
    return post(url, data, authorization, new_headers, basic_auth=basic_auth)


def put(url, data=None, authorization=None, extra_headers={}, basic_auth=False):
    return request(url, 'PUT', data, authorization, extra_headers,
                   basic_auth=basic_auth)


def put_form(url, data=None, authorization=None, extra_headers={},
              basic_auth=False):
    new_headers = dict(extra_headers,
                       **{'Content-Type': 'application/x-www-form-urlencoded'})
    return put(url, data, authorization, new_headers, basic_auth=basic_auth)


setup_pool_manager()