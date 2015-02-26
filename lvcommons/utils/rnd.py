import string
import random


ESPECIAL_CHARS = ',;.:-_!@#$%&/=?'

def generate_random_string(length, digits=True, upper_case=True, lower_case=True, especials=False, extra=None):
    """
    Genera una cadena de texto aleatoria, útil para códigos de confirmación
    :param length: Longitud que la cadena debe tener
    :return:
    """
    src = []
    if digits:
        src += string.digits
    if upper_case:
        src += string.ascii_uppercase
    if lower_case:
        src += string.ascii_lowercase
    if especials:
        src += ESPECIAL_CHARS
    if extra:
        src += extra
    sr = random.SystemRandom()
    return ''.join(sr.choice(src) for x in range(length))
