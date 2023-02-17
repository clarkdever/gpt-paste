# GPT Paste

## Problem
When you're using GPTChat to work on your code, it often loses state or has no ability to see the modifications you made in editor.

## Solution
This is a Python script that reads all .py files in the current directory (excluding the script file itself), concatenates their contents, and adds the name of each file as a comment at the beginning of each file's contents. The resulting output is then copied to the clipboard for pasting into GPTChat.

## Getting Started
These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites
This project requires Python 3 and the pyperclip package to be installed. If you don't already have Python 3 installed, you can download it from the official website. To install pyperclip, you can run the following command:

```bash
pip install pyperclip
```

### Installing
To get a local copy of this project, you can clone the repository using Git:

```bash
git clone https://github.com/clarkdever/gpt-paste.git
```
Alternatively, you can download the ZIP archive of the project and extract it to your desired directory.

### Usage
To use the script, simply navigate to the directory containing your .py files and run the script:


```bash
python gpt-paste.py
```
The script will concatenate the contents of all .py files in the directory (excluding the script file itself), add a comment indicating the name of each file, and copy the resulting output to the clipboard for pasting into GPTCHat.

## Contributing
If you have any suggestions or find any issues with the project, feel free to open an issue or submit a pull request. All contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Did you find this useful?
1. Add me on [linkedin](https://linkedin.com/in/clarkdever) or [twitter](https://www.twitter.com/clarkdever) and let me know
2. Star this library or share it on your socials

Happy Hacking!
