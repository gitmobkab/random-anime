import time
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
    

    
anime_layout = Layout(name="anime_layout")
anime_layout["anime_layout"].split_column(
    Layout(name="header",ratio=1),
    Layout(name="content",ratio=2)
)
anime_layout["content"].split_row(
    Layout(name="info",ratio= 2),
    Layout(name="synopsis",ratio=4)
)
def update_layout(data:dict,target_layout = anime_layout):
    selected_layout = target_layout
    update_title(data["title"],data["url"],selected_layout)
    update_info(data["status"],data["duration"],data["episodes"],selected_layout)
    update_synopsis(data["synopsis"],selected_layout)
    
def update_title(title,url,target_layout:Layout):
    header_content = Text(f"Title: {title}\n",justify="center")
    header_content.append_text(Text(f"Url: {url}",style=url))
    header_content.highlight_words(["title","url"],"bold blue",case_sensitive=False)
    target_layout["header"].update(Panel(header_content,padding=(1,0),border_style="dark_blue"))
    
def update_info(status,duration,episodes,target_layout:Layout):
    info_text = Text(f"Status: {status}\n",justify="center")
    info_text.append_text(Text(f"Duration: {duration}\n"))
    info_text.append_text(Text(f"Episodes: {episodes}",justify="center"))
    info_text.highlight_words(["status","duration","episodes"],style="bold dark_green",case_sensitive=False)
    target_layout["info"].update(Panel(info_text,padding=(3,0),border_style="dark_green"))
    
def update_synopsis(synopsis,target_layout:Layout):
    synopsis = Text(f"Synopsis:\n{synopsis}",justify="center")
    synopsis.highlight_words(["synopsis"],style="bold dark_purple",case_sensitive=False)
    target_layout["synopsis"].update(Panel(synopsis,padding=(3,0),border_style="purple"))
    

commands = [
    "Type 'y' to print a random anime (default Command)",
    "Type 'h' to print the commands",
    "Type 'n' to quit the program without clearing the terminal",
    "Type 'q' to quit the program and clear the terminal screen",
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
        command = Prompt.ask("command:>",case_sensitive=False,choices=["y","h","n","q"],default="y")
        match command:
            case "y":
                request_result = make_request("https://api.jikan.moe/v4/random/anime")
                if request_result is None:
                    console.print("something went wrong, Please retry later")
                else:
                    data_json = request_result
                    anime = data_json["data"]
                    update_layout(anime)
                    console.print(anime_layout)
            case "h":
                print_program_commands()
            case "n":
                break
            case "q":
                console.clear()
                break
            
                                    
