#!/usr/bin/env python

import sys
from httplib import HTTPConnection
from urllib import urlencode
from urlparse import urljoin
from json import loads
from reportlab.pdfgen import canvas

OUTPUTFILE = 'certificate.pdf'

def get_brooklyn_integer():
    ''' Ask Brooklyn Integers for a single integer.
    
        Returns a tuple with number and integer permalink.
	From: https://github.com/migurski/ArtisinalInts/
    '''
    body = 'method=brooklyn.integers.create'
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    conn = HTTPConnection('api.brooklynintegers.com', 80)
    conn.request('POST', '/rest/', body, head)
    resp = conn.getresponse()
    
    if resp.status not in range(200, 299):
        raise Exception('Non-2XX response code from Brooklyn: %d' % resp.status)
    
    data = loads(resp.read())
    value = data['integer']
    return value

def draw_pdf(sparklydevop):
    certimage = './devops.cert.png'

    # TODO make this a function of image size
    width = 1116
    height = 1553

    # Times Roman better fits the other fonts on the template
    font_name = "Times-Roman"

    # TODO make font size a function of name length
    font_size = 72

    c = canvas.Canvas(OUTPUTFILE, pagesize=(width, height))
    c.setFont(font_name, font_size)

    # Print Name
    name_offset = c.stringWidth(sparklydevop)
    try:
        c.drawImage(certimage, 1, 1)
    except IOError:
        print "I/O error trying to open %s" % certimage
    else:
        c.drawString((width-name_offset)/2, height*3/4, sparklydevop)

    # Print Certificate Number
    cert_number = "Certificate No. " + str(get_brooklyn_integer())
    cert_offset = c.stringWidth(cert_number) 
    c.drawString((width-cert_offset)/2, height*3/4-font_size*2, cert_number)

    c.showPage()

    # TODO check for write permissions/failure
    try:
        c.save()
    except IOError:
        print "I/O error trying to save %s" % OUTPUTFILE

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: gendocert.py "Firstname Lastname"'
        sys.exit(1)
    else:
        # TODO if this is run as a CGI need to sanitize input
        draw_pdf(sys.argv[1])
