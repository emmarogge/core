import logging
import pathlib
import urllib.request

from cellprofiler_core.utilities.image import is_file_url
from cellprofiler_core.constants.image import FILE_SCHEME, PASSTHROUGH_SCHEMES


def pathname2url(path):
    """Convert the unicode path to a file: url"""
    lower_path = path.lower()
    if any((lower_path.startswith(x) for x in PASSTHROUGH_SCHEMES)):
        return path
    path_object = pathlib.Path(path)
    if path_object.is_absolute():
        # Produces a valid URI regardless of platform.
        return path_object.as_uri()
    # Produces CellProfiler's interpretation of a relative path URI.
    return FILE_SCHEME + urllib.request.pathname2url(path)


def url2pathname(url):
    lower_url = url.lower()
    if any((lower_url.startswith(x) for x in PASSTHROUGH_SCHEMES)):
        logging.debug("!!!DEBUG LOGGING!!! IS PASSTHROUGH SCHEME pathname.url2pathname({})".format(lower_url))
        return url
    if is_file_url(url):
        logging.debug("!!!DEBUG LOGGING!!! IS_FILE_URL pathname.url2pathname({})".format(lower_url))
        return urllib.request.url2pathname(url[len(FILE_SCHEME):])
    return url
