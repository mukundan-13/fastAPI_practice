from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr

conf = ConnectionConfig(
    MAIL_USERNAME="mukundan386@gmail.com",
    MAIL_PASSWORD="xioi lxfw kixu yvpf",
    MAIL_FROM="mukundan386@gmail.com",
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

async def sendEmail(email: EmailStr):
    message = MessageSchema(
        subject="Hi",
        recipients=[email],
        body="Hi! Thanks for registering",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
