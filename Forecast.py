from xml.parsers.expat import ParserCreate
from urllib import request

def fetch_xmldata(url):
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
                   Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        return f.read().decode()

class DefaultSaxHandler(object):
    def __init__(self):
        self.city = ''
        self.forecast = []

    def start_element(self, name, attrs):
        #print('sax:start_element: %s, atts: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.city = attrs['city']
        if name == 'yweather:forecast':
            self.forecast.append({'date':attrs['date'],
                                  'text':attrs['text'],
                                  'high':round((int(attrs['high']) - 32) / 1.8),
                                  'low' :round((int(attrs['low']) - 32) / 1.8)})

    def end_element(self, name):
        #print('sax:end_element: %s' % name)
        pass

    def char_data(self, text):
        #print('sax:char_data: %s' % text)
        pass

def handler_xmldata(xmldata):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xmldata)
    return {'city':handler.city, "forecast":handler.forecast}
if __name__ == '__main__':
    '''
    BeiJing weather A week
    '''
    URL = r'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather' \
          r'.forecast%20where%20woeid%20%3D%202151330&format=xml'
    xml = fetch_xmldata(URL)
    result= handler_xmldata(xml.encode('utf-8'))
    print(result)