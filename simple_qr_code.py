import qrcode as qr
img = qr.make('''Hello there,

I hope you're having a great day! 🌟

Thank you for scanning this QR code. I'm a developer passionate about technology and innovation.

If you have any questions, want to chat tech, or just say hello, you can reach me at sharmeensheikh09@gmail.com.

Looking forward to connecting with you!

Best regards,
Sharmeen Sheikh
''') #text
# img = qr.make("https://github.com/") #link
img.save("qr_code.png")