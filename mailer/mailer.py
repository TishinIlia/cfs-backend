from flask_mail import Message


def create_email(name, phone):
    mail_options = {
        "subject": "New website order",
        "sender": "cfs@gmail.com",
        "recipients": ["nenaviju4tverg@gmail.com"],
        "charset": "utf-8",
        "html": f"<span>New call request from <b> {name} </b> phone number is: <b> {phone} </b"
                f"><br> good luck and have a nice day, BOSS </span><br><br><img "
                f"src=\"https://i.ytimg.com/vi/cTptnkdFn6Q/hqdefault.jpg\" alt=\"BUSINESS SUCCESS\"> "
    }
    return Message(**mail_options)
