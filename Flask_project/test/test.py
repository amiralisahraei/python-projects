import requests


try:

    resp = requests.post(
        "http://localhost:5000/predict", files={"file": open("my_one.png", "rb")}
    )

    # print the actual json data
    print(resp.text)


except Exception as e:

    print("There is an error regarding seding request: ", e)
