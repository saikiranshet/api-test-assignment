import requests


class APICaller:
    def __init__(self, base_url, headers) -> None:
        self.base_url = base_url
        self.headers = headers

    def get(
        self,
        url_offest,
        err_key: str = "message",
        error: str = "Failed to make GET request",
    ):
        url = f"{self.base_url}{url_offest}"
        response = requests.get(url, headers=self.headers)
        res = response.json()
        if response.status_code >= 400:
            message = res.get(err_key, error)
            raise Exception(message)
        return res
