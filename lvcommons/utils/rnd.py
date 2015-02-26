import string
import random


SPECIAL_CHARS = ',;.:-_!@#$%&/=?'


def _get_src_str_for_rnd(digits=True, upper_case=True, lower_case=True, specials=False, extra=None):
    src = []
    if digits:
        src += string.digits
    if upper_case:
        src += string.ascii_uppercase
    if lower_case:
        src += string.ascii_lowercase
    if specials:
        src += SPECIAL_CHARS
    if extra:
        src += extra
    return src


def generate_random_string(length, digits=True, upper_case=True, lower_case=True, specials=False, extra=None):
    """
    Genera una cadena de texto aleatoria, útil para códigos de confirmación
    :param length: Longitud que la cadena debe tener
    :return:
    """
    src = _get_src_str_for_rnd(digits, upper_case, lower_case, specials, extra)
    sr = random.SystemRandom()
    return ''.join(sr.choice(src) for x in range(length))


def get_random_string_generator(length, digits=True, upper_case=True, lower_case=True, specials=False, extra=None):
    """
    Crea un generador de cadenas aleatorias en base a los parámetros dados
    :param length:
    :param digits:
    :param upper_case:
    :param lower_case:
    :param specials:
    :param extra:
    :return:
    """
    src = _get_src_str_for_rnd(digits, upper_case, lower_case, specials, extra)
    sr = random.SystemRandom()
    while True:
        yield ''.join(sr.choice(src) for x in range(length))