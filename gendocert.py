#!/usr/bin/env python

import sys
from reportlab.pdfgen import canvas

OUTPUTFILE = 'certificate.pdf'


def draw_pdf(sparklydevop):
    certimage = './devops.cert.png'

    # TODO make this a function of image size
    c = canvas.Canvas(OUTPUTFILE, pagesize=(1147, 1608))
    c.drawImage(certimage, 1, 1)
    c.setFont("Helvetica", 72)
    # TODO: calculate X for string based on length of username
    c.drawString(375, 1175, sparklydevop)
    c.showPage()
    c.save()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: gendocert.py "Firstname Lastname"'
        sys.exit(1)
    else:
        # TODO if this is run as a CGI need to sanitize input
        draw_pdf(sys.argv[1])
