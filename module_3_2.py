def send_email(message, recipient,sender = "dmitry.shel@gmail.com"):
    if ("@" and (".com" or ".ru" or ".net")) not in (recipient or sender) or ("@" or (".com" or ".ru" or ".net")) not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "dmitry.shel@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "dmitry.shel@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("message" , "Diana2006@gmail.com")
send_email("messege","vova88446@gmail.com","@.com")
send_email("message","kyzia@.co")
send_email("message" , "dmitry.shel@gmail.com")