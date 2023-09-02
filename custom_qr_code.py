import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=8)
qr.add_data('''Hello there,

I hope you're having a great day! 🌟

Thank you for scanning this custom QR code. I'm a developer passionate about technology and innovation.

If you have any questions, want to chat tech, or just say hello, you can reach me at sharmeensheikh09@gmail.com.

Looking forward to connecting with you!

Best regards,
Sharmeen Sheikh''')
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="yellow")
img.save("custom_qr_code.png")