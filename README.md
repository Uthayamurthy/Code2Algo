# Code2Algo
An AI Powered Tool to generate Algorithm and Flowchart from your source code !

> ⚠️ Warning : The output of this tool could be inaccurate or wrong. This tool is meant to provide a quick draft for you to work further on. Use it at your own risk !!

## Supported Platforms:
- Any Linux Distro (Tested On : Ubuntu 24.04)
- Windows 11

## Installation Instructions

### Linux
- Download the latest binary release from the releases page or [click here](https://github.com/Uthayamurthy/Code2Algo/releases/download/V0.1/code2algo-V0.1-Linux-X86_64.zip) to download directly
- Extract the zip file
```
unzip code2algo-V0.1-Linux-X86_64.zip 
```
- Run the file !
```
./code2algo
```

### Windows 11

- Downlaod the latest binary release from the releases page or [click here](https://github.com/Uthayamurthy/Code2Algo/releases/download/V0.1/code2algo-V0.1-Windows-X86_64.zip) to dowload directly
- Extract the zip file
- Run the code2algo.exe file

## First Time Setup
#### Note: You need a Gemini API Key to use code2algo 

- Go to [Google AI Studio](https://aistudio.google.com/), SignIN with your google account and obtain a free Gemini Api Key
- Paste this key when you start code2algo for the first time. This key will be automatically saved and used from the next run

## Demo
#### Demo Video
[![Code2Algo Demo Video](https://img.youtube.com/vi/fqsvnz2BExI/0.jpg)](https://www.youtube.com/watch?v=fqsvnz2BExI)
#### Here is a flowchart of code2algo, generated by itself:
![Demo Image](assets/self-flowchart.png?raw=true)

### Here is the algorithm of code2algo, generated by itself:
```
1. START
2. DISPLAY the application's header, subheader, author, and license information.
3. IF the file 'api_key.txt' does not exist:
    - INPUT: Gemini API key from the user.
    - Save the API key to 'api_key.txt'.
   ELSE:
    - Read the API key from 'api_key.txt'.
    - DISPLAY "Using Existing Gemini API Keys".
4. Initialize the Gemini client with the API key.
5. INPUT: Programming language of the source code (Python or C).
6. INPUT: Path and name of the source code file.
7. IF the source code file does not exist:
    - DISPLAY "File not found :(".
    - END.
8. DISPLAY "Here is your code:".
9. Read the source code from the file.
10. DISPLAY the source code with syntax highlighting.
11. INPUT: Choice to generate Flowchart (F) or Algorithm (A).
12. IF choice is "F":
    - Call generate_flowchart(source code, programming language).
   ELSE IF choice is "A":
    - Call generate_algorithm(source code, programming language).
   ELSE:
    - DISPLAY "Invalid choice !".
    - END.

Algorithm for generate_flowchart(code, language):
    1. INPUT: Output filename for the flowchart image.
    2. Initialize a progress indicator.
    3. START Live display with the progress indicator.
    4. TRY:
        - Define system instructions for flowchart generation, including the output filename and language.
        - Generate content using the Gemini client with the system instructions and source code.
        - Extract the code from the response.
        - IF execution of the extracted code fails:
            - Update progress indicator to "Failed!".
            - DISPLAY "Execution failed".
            - SET success to False.
           ELSE:
            - Update progress indicator to "Done!".
            - DISPLAY "Your flowchart has been generated !".
            - SET success to True.
       EXCEPT:
        - SET success to False.
        - Update progress indicator to "Failed!".
        - DISPLAY the error message.
    5. STOP Live display.
    6. IF success is True:
        - DISPLAY "Saved to [output filename].png".

Algorithm for generate_algorithm(code, language):
    1. INPUT: Output filename for the algorithm text file.
    2. Initialize a progress indicator.
    3. START Live display with the progress indicator.
    4. TRY:
        - Define system instructions for algorithm generation, including the language.
        - Generate content using the Gemini client with the system instructions and source code.
        - Extract the generated algorithm from the response.
        - Write the algorithm to a text file named [output filename].txt.
        - Update progress indicator to "Done!".
        - DISPLAY "Your Algorithm has been generated !".
        - SET success to True.
       EXCEPT:
        - Update progress indicator to "Failed!".
        - DISPLAY the error message.
        - SET success to False.
    5. STOP Live display.
    6. IF success is True:
        - DISPLAY "Saved to [output filename].txt".
    7. END
```

**What more would you ask for ?**