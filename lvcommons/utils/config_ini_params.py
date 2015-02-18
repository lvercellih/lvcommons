import configparser
from configparser import NoOptionError, NoSectionError


def load_params(config_files, src_dict):
    """

    :param config_files: Lista de nombres de archivos de configuración para cargar
    :param src_dict: Diccionario donde están los metadatos de los parámetros.
                    Los elementos del diccionario deben tener el siguiente formato:
                    <name>: (<section>, <option>, [<type: "" (default), "int", "float", "boolean">[, (<default_value>)]])
                    Sólo se tendrán en cuenta los parámetros cuyos nombres empiecen con PARAM_
                    Esto es debido a que esta función está pensada para usarse junto con "globals()" y es una forma de
                    diferenciar a los parámetros de las variables
    :return:
    """
    config = configparser.ConfigParser()

    for fn in config_files:
        config.read(fn)

    for var in src_dict:
        if not var.startswith("PARAM_"):
            continue

        meta = src_dict[var]
        if not isinstance(meta, tuple):
            break

        section= meta[0]
        option = meta[1]
        opt_type = meta[2] if len(meta) > 2 else ""
        default = meta[3] if len(meta) > 3 else None

        getter = getattr(config, "get" + opt_type)
        if default is None:
            src_dict[var] = getter(section, option)
        else:
            try:
                src_dict[var] = getter(section, option)
            except (NoOptionError, NoSectionError):
                src_dict[var] = default