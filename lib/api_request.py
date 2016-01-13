from urllib2 import Request, urlopen, URLError
from lib.tools import errorMessage

# Make a request on a URL with a dictionnary of data
def request(url, data = {}):
    uri = url + "?"
    for key, value in data.iteritems():
        uri += key + "=" + value + "&"
    # Delete the last letter of the String
    uri = uri[:-1]

    try:
        return urlopen(Request(uri))
    except URLError, e:
        errorMessage()