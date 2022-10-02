from fastapi import FastAPI, HTTPException, status
from services import send_message
from models import Mail
from validators import validate_send_mail_request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post('/send-mail', status_code=status.HTTP_201_CREATED)
def send_mail(mail:Mail):
    try:
        validate_send_mail_request(mail)
        send_message(mail)
        return {
            'mail':mail.subject,
            'to':mail.address
        }
    except HTTPException as http_exception:
        raise http_exception
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)