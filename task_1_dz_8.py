import re


def email_parse(email_address):
    re_data = re.findall(r'([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$', email_address)
    if not re_data:
        raise ValueError(f'wrong mail: {email_address}')
    else:
        print(dict(zip(["username", 'domain'], re_data[0])))


email_parse('someone@geekbrains.ru')
