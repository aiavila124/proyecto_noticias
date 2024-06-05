import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_mail(email_destino, asunto, mensaje):
    # Datos del remitente
    email_origen = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = email_origen
    msg['To'] = email_destino
    msg['Subject'] = asunto

    # Agregar el cuerpo del mensaje
    # msg.attach(MIMEText(mensaje, 'plain'))
    msg.attach(MIMEText(mensaje, 'html'))

    # Para adjuntar archivos
    # with open('foto.png', 'rb') as f:
    #     img_data = f.read()
    #     image = MIMEImage(img_data, name='foto.png')
    #     msg.attach(image)

    # Configurar el servidor SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_origen, password)
        text = msg.as_string()
        server.sendmail(email_origen, email_destino, text)
        server.quit()
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error: {e}")

