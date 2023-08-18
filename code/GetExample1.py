import requests


url = 'https://64dd7529825d19d9bfb12c36.mockapi.io/cetAfter/1'


headers = {
    #if have ->
    # 'Authorization': token
}

cetAfter = {

}



print("Sorteio Inauguração De Angelina")


sorteio_response = input("Deseja participar do Sorteio?\r\n")

#Exemplo do Button como base do exemplo da Totvs em https://tdn.totvs.com/display/public/TVSCCLC/Comando+Exibir+Mensagem

match sorteio_response:
    case "0":
        print("Não desejo participar")

    case "1":
        print("Desejo participar do Sorteio")

        response = requests.get(url=url, json=cetAfter, headers=headers)

        if response.status_code >= 200 and response.status_code <= 299:
            print(response.status_code)
            print(response.reason)

            response_data = response.json()
            print(response_data)

        else:
            print(response.status_code)
            print(response.reason)
            print(response.text)






