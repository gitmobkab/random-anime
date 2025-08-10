import requests


def make_request(api_url:str) -> dict | None:
    request = requests.get(api_url)
    if request.status_code != 200:
        print(f"Request failed, api responded with status code: {request.status_code}")
        return
    else:
        data = request.json()
        return data
    
def data_unwrapper(data:dict, list_of_attributes: list[str]):
    target_attribute = data[list_of_attributes[0]]
    try:
        for attribute in list_of_attributes[1:]:
            target_attribute = target_attribute[attribute]
    except IndexError:
        print("Error: The list should at least contain 2 attributes")
        return
    