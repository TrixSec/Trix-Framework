import json
import os
import subprocess
import time
import requests
from colorama import init, Fore, Style
from termcolor import colored 

init()

FRAMEWORK_VERSION = "2.0.0"
AUTHOR = "Trix Cyrus"
COPYRIGHT = "Copyright © 2024 Trixsec Org"

def check_for_updates():
    response = requests.get("https://raw.githubusercontent.com/TrixSec/Trix-Framework/refs/heads/main/VERSION")
    if response.status_code == 200:
        latest_version = response.text.strip()

        if FRAMEWORK_VERSION != latest_version:
            print(colored(f"[•] New version available: {latest_version}. Updating...", 'yellow'))
            os.system('git reset --hard HEAD')
            os.system('git pull')
            with open('VERSION', 'w') as version_file:
                version_file.write(latest_version)
            print(colored("[•] Update completed. Please rerun Framework.", 'green'))
            exit()

        print(colored(f"[•] You are using the latest version: {latest_version}.", 'green'))
    else:
        print(colored("[×] Error fetching the latest version. Please check your internet connection.", 'red'))

def display_banner():
    banner = r"""


╔════╦═══╦══╦═╗╔═╗─╔═══╦═══╦═══╦═╗╔═╦═══╦╗╔╗╔╦═══╦═══╦╗╔═╗
║╔╗╔╗║╔═╗╠╣╠╩╗╚╝╔╝─║╔══╣╔═╗║╔═╗║║╚╝║║╔══╣║║║║║╔═╗║╔═╗║║║╔╝
╚╝║║╚╣╚═╝║║║─╚╗╔╝──║╚══╣╚═╝║║─║║╔╗╔╗║╚══╣║║║║║║─║║╚═╝║╚╝╝
──║║─║╔╗╔╝║║─╔╝╚╦══╣╔══╣╔╗╔╣╚═╝║║║║║║╔══╣╚╝╚╝║║─║║╔╗╔╣╔╗║
──║║─║║║╚╦╣╠╦╝╔╗╚╦═╣║──║║║╚╣╔═╗║║║║║║╚══╬╗╔╗╔╣╚═╝║║║╚╣║║╚╗
──╚╝─╚╝╚═╩══╩═╝╚═╝─╚╝──╚╝╚═╩╝─╚╩╝╚╝╚╩═══╝╚╝╚╝╚═══╩╝╚═╩╝╚═╝ Fastest And Optimised CLI Tool Factory v2.0.0
    
    """
    print(colored(banner, 'cyan'))
    print(colored(f"Framework Version: {FRAMEWORK_VERSION}", 'yellow'))
    print(colored(f"Made by {AUTHOR}", 'yellow'))
    print(colored(COPYRIGHT, 'yellow'))
    print("")


def load_tools(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def clone_repo(tool):
    repo_url = tool.get('repo') or tool.get('url')
    if not repo_url:
        print(Fore.RED + f"No repository URL found for {tool['name']}. Skipping..." + Style.RESET_ALL)
        return

    target_dir = os.path.expanduser(f"~/{tool['name']}")
    subprocess.run(["git", "clone", repo_url, target_dir])

def print_category(category, index):
    print(Fore.GREEN + f"{index + 1}. {category}" + Style.RESET_ALL)

def print_tool(tool, index):
    print(Fore.YELLOW + f"{index + 1}. {tool['name']}: {tool['description']}" + Style.RESET_ALL)

def main():
    display_banner()
    check_for_updates()
    tools = load_tools('tools.json')
    categories = list(tools.keys())
    current_category = None

    while True:        
        if current_category is None:
            print(Fore.BLUE + "Categories:" + Style.RESET_ALL)
            for idx, category in enumerate(categories):
                print_category(category, idx)
            print(Fore.RED + "e/E) Exit" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + f"Tools in {categories[current_category]}:" + Style.RESET_ALL)
            for idx, tool in enumerate(tools[categories[current_category]]):
                print_tool(tool, idx)
            print(Fore.RED + "b) Back" + Style.RESET_ALL)
            print(Fore.RED + "e/E) Exit" + Style.RESET_ALL)
        
        user_input = input(Fore.CYAN + "Select an option: " + Style.RESET_ALL).strip().lower()
        
        if user_input == 'e':
            print(Fore.MAGENTA + "Exiting the tool. Goodbye!" + Style.RESET_ALL)
            break
        elif user_input == 'b' and current_category is not None:
            current_category = None
        elif current_category is None and user_input.isdigit() and 1 <= int(user_input) <= len(categories):
            current_category = int(user_input) - 1
        elif current_category is not None and user_input.isdigit() and 1 <= int(user_input) <= len(tools[categories[current_category]]):
            tool_index = int(user_input) - 1
            tool = tools[categories[current_category]][tool_index]
            clone_repo(tool)
            print(Fore.MAGENTA + f"Cloned {tool['name']} to ~/{tool['name']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)
        
        time.sleep(1)  

if __name__ == "__main__":
    main()
