import mss.tools
import os
from pyzbar.pyzbar import decode
from PIL import Image

# Take Screenshot for all monitors
with mss.mss() as sct:
    sct_img = sct.shot(mon=-1, output = 'tempQRss.png')
##########################################################################################


# Take Screenshot for monitor 1 only
# with mss.mss() as sct:
#     monitor_number = 1
#     mon = sct.monitors[monitor_number]

#     sct_img = sct.grab(mon)
#     mss.tools.to_png(sct_img.rgb, sct_img.size, output='qr.png')
##########################################################################################


# Read QR
qrData = decode(Image.open('tempQRss.png'))
qr = None
if len(qrData) > 0:
    qr = qrData[0].data.decode('utf-8')
    # Copy QR to Clipboard
    command = 'echo | set /p nul="' + qr + '"| clip'
    os.system(command)

# Delete Screenshot
# os.remove('tempQRss.png')