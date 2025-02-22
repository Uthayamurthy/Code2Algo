'''
Code2Algo - An AI Powered Tool to generate Algorithm and Flowchart from your source code !

    Copyright (C) 2025  R Uthaya Murthy

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact Author : uthayamurthy2006@gmail.com
'''

from rich.console import Console
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TimeElapsedColumn, SpinnerColumn
from google import genai
from google.genai import types
from prompts import flowchart_instruct, algorithm_instruct
import re
import pyfiglet
import os

def exec_code(code: str):
    allowed_globals = {"graphviz": __import__("graphviz")}
    allowed_locals = {}
    try:
        exec(code, allowed_globals, allowed_locals)
        return True
    except Exception as e:
        console.print(f"[bold red]Execution failed: {e}")
        return False
    
def extract_code(text: str):
    pattern = r'^```(?:\w+)?\s*\n(.*?)(?=^```)```'
    result = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
    return result[0]

def generate_flowchart(code: str, language: str):
    output_filename = Prompt.ask("[bold blue]Enter the name of the output file (will be saved as png)")

    progress = Progress(
        SpinnerColumn(), 
        "[progress.description]{task.description}",
        BarColumn(),
        TimeElapsedColumn(),
    )

    task = progress.add_task("[bold]Generating Flowchart...", total=None)

    with Live(progress, console=console, refresh_per_second=10):
        try:
            sys_instruct = flowchart_instruct.ingest_args(filename=output_filename, language=language)

            response = gemini_client.models.generate_content(
                model="gemini-2.0-flash",
                config=types.GenerateContentConfig(
                    system_instruction=sys_instruct,
                    temperature=0.3),
                contents=[f'{code}']
            )
            output = response.text
            code = extract_code(output)

            if not exec_code(code):
                progress.update(task, description="[bold red]Failed! ❌[/bold red]")
                console.print("[bold red]❌ Execution failed")
            else:
                progress.update(task, description="[bold green]Done! ✅[/bold green]")
                console.print("[bold green]Your flowchart has been generated ![/bold green] ✅")
        except Exception as e:
            progress.update(task, description="[bold red]Failed! ❌[/bold red]")
            console.print(f"[bold red]Error: {e}")

    progress.stop()
    console.print(f"[bold green]Saved to {output_filename}.png 🎊🎊")

def generate_algorithm(code: str, language: str):
    output_filename = Prompt.ask("[bold blue]Enter the name of the output file name (will be saved as text file)")

    progress = Progress(
        SpinnerColumn(), 
        "[progress.description]{task.description}",
        BarColumn(),
        TimeElapsedColumn(),
    )

    task = progress.add_task("[bold]Generating Algorithm...", total=None)

    with Live(progress, console=console, refresh_per_second=10):
        try:
            sys_instruct = algorithm_instruct.ingest_args(language=language)
            response = gemini_client.models.generate_content(
                model="gemini-2.0-flash",
                config=types.GenerateContentConfig(
                    system_instruction=sys_instruct,
                    temperature=0.3),
                contents=[f'{code}']
            )
            output = response.text
            output = output.strip()
            
            with open(f'{output_filename}.txt', 'w') as file:
                file.write(output)

            progress.update(task, description="[bold green]Done! ✅[/bold green]")
            console.print("[bold green]Your Algorithm has been generated ![/bold green] ✅")

        except Exception as e:
            progress.update(task, description="[bold red]Failed! ❌[/bold red]")
            console.print(f"[bold red]Error: {e}")
    progress.stop()

    console.print(f"[bold green]Saved to {output_filename}.txt  🎊🎊")

console = Console()

head = pyfiglet.figlet_format("C2A", font="block")
subhead = pyfiglet.figlet_format("Code 2 Algo", font="bubble")
author = pyfiglet.figlet_format("Copyright (C) 2025 R Uthaya Murthy", font="digital")
license = Panel("[bold]License : [link=https://github.com/Uthayamurthy/Code2Algo/blob/main/LICENSE]GNU General Public License v3.0[/link][/bold]", expand=False)
console.print(f'[bold deep_sky_blue4]{head}')
console.print(f'[bold cyan3]{subhead}')
console.print(f'[bold cyan1]{author}')
console.print(license)

if not os.path.isfile('api_key.txt'):
    api_key = Prompt.ask("\n[bold blue]Enter your Gemini API key")
    with open('api_key.txt', 'w') as f:
        f.write(api_key)
else:
    with open('api_key.txt', 'r') as f:
        api_key = f.read()
    console.print(f'\n[bold green]Using Existing Gemini API Keys')

gemini_client = genai.Client(api_key=api_key)

language = Prompt.ask("\n[bold blue]Programming Language of your source code file", choices=["Python", "C"], default="C")
code_filepath = Prompt.ask("[bold blue]Enter the path and name of your source code file")

if not os.path.isfile(code_filepath):
    console.print(f'[bold red]File not found :(')
    exit()

console.print("\n[bold]Here is your code:\n")

with open(code_filepath, 'r') as f:
    code = f.read()
    console.print(Syntax(code, language.lower()))

choice = Prompt.ask("[bold blue]Do you want to generate a Flowchart or Algorithm?", choices=["F", "A"], default="F")

if choice == "F":
    generate_flowchart(code, language)
elif choice == "A":
    generate_algorithm(code, language)
else:
    console.print("[bold red]Invalid choice !")
    exit()