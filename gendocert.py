#!/usr/bin/env python

import sys
from reportlab.pdfgen import canvas

OUTPUTFILE = 'certificate.pdf'
# TODO if this is run as a CGI need to sanitize input
# TODO: calculate X for string based on length of username
NAME = sys.argv[1]

def draw_pdf(c):
    CERTIMAGE = './devops.cert.png'

    c.drawImage(CERTIMAGE, 1, 1)
    c.setFont("Helvetica", 72)
    c.drawString(375, 1175, NAME)



if __name__ == "__main__":
    # TODO make this a function of image size
    c = canvas.Canvas(OUTPUTFILE,pagesize=(1147,1608))
    draw_pdf(c)
    c.showPage()
    c.save()
