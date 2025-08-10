import requests
from rich.rule import Rule
from rich.console import Console
from rich.layout import Layout 
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt

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
        target_attribute = None
    finally:
        return target_attribute
    
def update_layout_section(layout_name: Layout, section_name: str, output:str):
    renderable_output = Text(output,justify="center")
    renderable_output = Panel(renderable_output)
    layout_name[section_name].update(renderable_output)

commands = [
    "Type ':y' to print a random anime (default Command)"
    "Type ':h' to print the commands",
    "Type ':n' to quit the program without clearing the terminal",
    "Type ':q' to quit the program and clear the terminal screen",
]
def print_program_commands(commands_description :list = commands):
    for command in commands_description:
        console.print(command,justify="center")
if __name__ == "__main__":
    console = Console()
    console.rule("Anime Random !",characters="▓")
    console.print("Welcome to Anime Random !",justify="center")
    print_program_commands()
    while True:
        command = Prompt.ask("command:>",case_sensitive=False,choices=[":y",":h",":n",":q"],default=":y")
        if command == ":n":
            break
                