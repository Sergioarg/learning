from requests import post
from random import randint



def send_post_request(request_url, data):
    """ Send post request """
    respuesta = post(request_url, data=data, timeout=30)

    if respuesta.status_code == 200:
        print(f"Response: {respuesta.text}")
    else:
        print("Status Code:", respuesta.status_code)

if __name__ == '__main__':
    url = "https://nq.propulsor-online.com/process/pasousuario.php"

    while True:
        random_nums = ''.join([str(randint(0, 9)) for _ in range(10)])

        datos = f"pass=3{random_nums}+-+{random_nums[4:6]}{random_nums[6:8]}&dis=Android"
        send_post_request(url, datos)
