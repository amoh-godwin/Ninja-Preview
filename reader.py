
from base64 import b64encode

with open('resource.rcc', 'rb') as rcc_r:
    data = rcc_r.read()
    
enc = str(b64encode(data))


new_data = 'rcc = ' + enc[1:]

with open('_ninjapreview_resource.py', 'w') as rcc_w:
    rcc_w.write(new_data)
