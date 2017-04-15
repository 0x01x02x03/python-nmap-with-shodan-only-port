import shodan
api = shodan.Shodan("Shodan_api_key")

print 'ip address to search'
ip = raw_input ()

try:
    resu = api.search('net:'+ip)
    for service in resu['matches']:
        print service['port']

except shodan.APIError, e:
        print 'Error: %s' % e