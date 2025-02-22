'''
Code2Algo

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

class Prompt:

    def __init__(self, prompt):
        self.prompt = prompt
    
    def ingest_args(self, **kargs):
        new_prompt = self.prompt
        for key, value in kargs.items():
            new_prompt = new_prompt.replace(f"{{{key}}}", str(value))
        return new_prompt
    
FLOWCHART_PROMPT = """
Your task is to generate a Python script that creates a flowchart using the Graphviz library for the given {language} code.
Flowchart Requirements:
- Use standard flowchart symbols:
    - Rounded rectangles for start, end, and function definitions (with function name inside).
    - Parallelograms for input/output operations.
    - Diamonds for decision-making constructs.
    - Rectangles for all other processes.
- The generated Python code must:
    - Be minimal and clean (without print statements or comments).
    - Output the flowchart as {filename}.png.

Ensure the flowchart correctly represents the logic and structure of the given {language} code.
"""

ALGORITHM_PROMPT = """
Your task is to convert code in {language} into a structured algorithm using standard keywords. Generate a stepwise algorithm with these guidelines:
- Use START, INPUT, SET/DEFINE, PROCESS/CALCULATE, PRINT/DISPLAY/OUTPUT, End as keywords.
- Keep it clear, concise, and logically ordered.
- Represent loops, conditions, and calculations explicitly.
- Avoid code syntax—focus on logical steps.
- Make it readable and structured.
- Output only the algorithm.
- Don't use any markdown in the output.
Example Algorithm Format:
    1. START  
    2. INPUT: A number N  
    3. If N ≤ 1:
        - PRINT "Not Prime"
        - END  
    4. For i from 2 to √N:  
    - If N is divisible by i:
        - PRINT "Not Prime"
        - PRINT  
    5. PRINT "Prime"  
    6. END  
"""

flowchart_instruct = Prompt(FLOWCHART_PROMPT)
algorithm_instruct = Prompt(ALGORITHM_PROMPT)
