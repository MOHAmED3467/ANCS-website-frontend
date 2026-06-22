from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from pathlib import Path

output_pdf = Path('public/ANCS-website-screenshots.pdf')
hero_img = Path('src/assets/site-screenshot-hero.png')
preview_img = Path('src/assets/site-screenshot-preview.png')
full_img = Path('src/assets/site-screenshot-full.png')

c = canvas.Canvas(str(output_pdf), pagesize=A4)
width, height = A4

c.setFont('Helvetica-Bold', 24)
c.drawString(2*cm, height - 3*cm, 'ANCS Website Screenshots')
c.setFont('Helvetica', 14)
c.drawString(2*cm, height - 4.5*cm, 'Project website screenshots included as examples for the graduation book.')
c.setFont('Helvetica-Bold', 12)
c.drawString(2*cm, height - 6*cm, 'Website URL:')
c.setFillColorRGB(0, 0.2, 0.7)
c.drawString(4*cm, height - 6*cm, 'https://github.com/MOHAmED3467/ANCS-website-frontend')
c.setFillColorRGB(0, 0, 0)

c.setFont('Helvetica', 11)
c.drawString(2*cm, height - 7*cm, 'This document includes screenshot assets from the ANCS website to insert into your graduation book.')

c.showPage()

c.setFont('Helvetica-Bold', 18)
c.drawString(2*cm, height - 2.5*cm, 'Hero Section Screenshot')
if hero_img.exists():
    img = ImageReader(str(hero_img))
    iw, ih = img.getSize()
    max_w, max_h = width - 4*cm, height - 7*cm
    ratio = min(max_w / iw, max_h / ih)
    c.drawImage(img, 2*cm, height - 3*cm - ih*ratio, width=iw*ratio, height=ih*ratio)
else:
    c.setFont('Helvetica', 12)
    c.drawString(2*cm, height - 4*cm, 'Hero screenshot image not found.')

c.showPage()

c.setFont('Helvetica-Bold', 18)
c.drawString(2*cm, height - 2.5*cm, 'Preview Section Screenshot')
if preview_img.exists():
    img = ImageReader(str(preview_img))
    iw, ih = img.getSize()
    max_w, max_h = width - 4*cm, height - 7*cm
    ratio = min(max_w / iw, max_h / ih)
    c.drawImage(img, 2*cm, height - 3*cm - ih*ratio, width=iw*ratio, height=ih*ratio)
else:
    c.setFont('Helvetica', 12)
    c.drawString(2*cm, height - 4*cm, 'Preview screenshot image not found.')

c.showPage()

c.setFont('Helvetica-Bold', 18)
c.drawString(2*cm, height - 2.5*cm, 'Full Page Screenshot')
if full_img.exists():
    img = ImageReader(str(full_img))
    iw, ih = img.getSize()
    max_w, max_h = width - 4*cm, height - 7*cm
    ratio = min(max_w / iw, max_h / ih)
    c.drawImage(img, 2*cm, height - 3*cm - ih*ratio, width=iw*ratio, height=ih*ratio)
else:
    c.setFont('Helvetica', 12)
    c.drawString(2*cm, height - 4*cm, 'Full page screenshot image not found.')

c.save()
print('Created PDF:', output_pdf)