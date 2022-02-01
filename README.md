# b64_encoder_decoder
Command line python app to encode/decode base64 strings.


## Installation

### Linux
1. Download the code.
2. nano ~/.bashrc
3. alias b64ed="python3 /path/to/project/main.py"
4. Save and exit

Now you can execute b64ed -h

### MacOS
1. Download the code.
2. nano ~/.zshrc
3. alias b64ed="python3 /path/to/project/main.py"
4. Save and exit

Now you can execute b64ed -h

## Usage
`base64ed [-f | -e | -d | -h | help | man] [stringFile]`
* -f -> Encode file in base64. If you use this option, it is recommended to use `pbcopy` due to large result:
  * `base64ed -f /path/to/file | pbcopy`: Encode file and copy it to clipboard.
* -e -> Encode string in base64.
* -d -> Decode base64 string.
* -h/help/man -> Print this help.
* stringFile -> String or path to encode/decode. Mandatory with -e/d/f options.

