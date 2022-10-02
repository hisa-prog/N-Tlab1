from models import Mail
from fastapi import HTTPException, status

AUDIO_FORMATS = ["3gp", "aa", "aac", "aax", "act", "aiff", "alac", "amr", "ape", "au"
        "awb", "dss", "dvf", "flac", "gsm", "iklax", "ivs", "m4a", "m4b", "m4p", "mmf",
        "mp3", "mpc", "msv", "nmf", "mogg", "oga", "ogg", "opus", "ra", "rm", "raw", "rf64",
        "sln", "tta", "voc", "vox", "wav", "wma", "wv", "webm", "8svx", "cda"
    ]

def validate_send_mail_request(mail:Mail):
    if mail.audio is not None and mail.audio_name is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Audio name cannot be empty")

    if mail.audio_name is not None and mail.audio_name.split('.')[-1] not in AUDIO_FORMATS:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong audio format")