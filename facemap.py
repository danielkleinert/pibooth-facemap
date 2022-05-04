import io
from io import BytesIO

import requests

TOKEN = "dUB1Yng1FKeaimyJCcyVsIIYXP42mUssxvLee"

COMMON_HEADERS = {
    "Accept": "application/json",
    "X-Client-Os": "apple",
    "X-Facelab-Clientversion": "2.1.12",
    "X-Facelab-Token": TOKEN,
    "X-Client-Ad-Id": "",
    "Accept-Language": "en-DE",
    "X-Facelab-Platform": "ios",
    "Accept-Encoding": "gzip",
    "User-Agent": "lyrebird",
}


def age_image(input_file):
    return download_image(upload_image(input_file))


def upload_image(file: BytesIO) -> str:
    response = requests.post(
        url="https://facelab.lyrebirdstudio.net/v3/",
        headers=COMMON_HEADERS,
        files={
            "image": file,
            "X-Package-Name": "com.lyrebirdstudio.facelab",
        },
        #proxies={"https": "https://localhost:8080"}
    )
    raise_on_error('upload', response)
    return response.json()['data']['photo_key']


def download_image(photo_key: str) -> BytesIO:
    response = requests.get(
        url="https://facelab.lyrebirdstudio.net/v3/{}/old".format(photo_key),
        params={
            "no-resize": "true",
        },
        headers={
            **COMMON_HEADERS,
            "X-Package-Name": "com.lyrebirdstudio.facelab",
        },
        #proxies={"https": "https://localhost:8080"}
    )
    raise_on_error('download', response)
    jpg_file = io.BytesIO(response.content)
    jpg_file.name = "capture.jpg"
    return jpg_file


def raise_on_error(request_identifier, response):
    if not response.ok:
        raise RuntimeError("{} error: HTTP {} {}".format(request_identifier, response.status_code, response.reason))
    # alternative error detection for problem below
    if response.status_code == 213:
        raise RuntimeError("{} error: token expired".format(request_identifier))
    # broken, for what ever reason requests sets the body to ''
    # if response.headers.get('content-type') == "application/json":
    #     error = response.json()['error']
    #     if error:
    #         raise RuntimeError("{} error: {}".format(request_identifier, error))


if __name__ == '__main__':
    with open("example/input.jpeg", "rb") as picture_file:
        filtered_image = age_image(picture_file)
        with open("example/output.jpeg", "wb") as picture_file:
            picture_file.write(filtered_image.read())

