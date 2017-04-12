from urllib2 import Request, urlopen, URLError

# Make a request on a URL
# Can include a list data to query URL
# Can include a list header
# Example of url : https://api.github.com/search/repositories
# Example of data : { "q" : "string to search" }
# Example of header : { "Accept": "application/vnd.github.v3+json" }
def request(url, data, header):
    if data:
        uri = "?"
        # Parse the array data to add url queries
        for key, value in data.iteritems():
            uri += key + "=" + value + "&"
        # Delete the last letter of the uri which is "&"
        uri = uri[:-1]
        # Concat the uri to the complete url to request
        url += uri
    try:
        req = Request(url)
        # Add a list of headers (if exist) to the request
        if header:
            for key, value in header.iteritems():
                req.add_header(key, value)
        return urlopen(req)
    except Exception as e:
        xbmc.log(msg=e.message, level=xbmc.LOGERROR)
        raise Exception('Error on request')

# Download a file from url
def download(path, url):
    f = open(path,'wb')
    f.write(urlopen(url).read())
    f.close()