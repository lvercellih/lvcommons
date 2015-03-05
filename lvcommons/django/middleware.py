
class RealIpMiddleware(object):

    def process_request(self, request):
        if hasattr(request, 'real_ip'):
            return
        meta = request.META
        if 'HTTP_X_FORWARDED_FOR' in meta:
            request.real_ip = meta.get('HTTP_X_FORWARDED_FOR').split(",")[0]
        elif 'HTTP_X_REAL_IP' in meta:
            request.real_ip = meta.get('HTTP_X_REAL_IP').split(",")[0]
        else:
            request.real_ip = meta.get('REMOTE_ADDR', "")