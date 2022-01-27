# overlayRestrict
 Displays a semi-transparent overlay on a computer screen with an optional message and keyboard hook
 The message argument supports newlines using \n as well as other escaped characters
 
### Dependancies
[wxPython](https://pypi.org/project/wxPython/)

[keyboard](https://pypi.org/project/keyboard/)

```bash
# You can install the dependancies by running the command below after cloning the repo
pip install -r requirements.txt
```

### How to use
```
usage: overlayRestrict.py [-h] [-a ALPHA] [-b] [-c COLOUR] [--hide] [-q QUITMESSAGE] [-t TEXTCOLOUR] message

Display an opaque overlay on a user's PC

positional arguments:
  message               The message to display on the overlay

optional arguments:
  -h, --help            show this help message and exit
  -a ALPHA, --alpha ALPHA
                        The alpha of the message (0-255, 255 is solid) (default: 150)
  -b, --blockKeyboard   Block keyboard input (cannot block CTRL+ALT+DEL as it is an OS-level shortcut, however, this
                        blocks just about everything else)
  -c COLOUR, --colour COLOUR
                        The colour of the background of the message (default: #0000FF)
  --hide                Hide the "powered by" message added to the end of a message
  -q QUITMESSAGE, --quitMessage QUITMESSAGE
                        The message displayed (under the overlay message) when the user tries to quit the message app
                        (default "\n\n\nDid you really think that was going to work???"
  -t TEXTCOLOUR, --textColour TEXTCOLOUR
                        The colour of the text in the message (default: #000000)
```

### Examples
```bash
overlayRestrict.py "Hello World!" # Displays Hello World! on a semi-transparent blue overlay on a user's PC
overlayRestrict.py "Hello World!" -t #FFFFFF # Displays a WHITE message on a semi-transparent blue overlay on a user's PC
```
