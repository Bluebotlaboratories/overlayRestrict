###
# Copyright Bluebotlaboratories
# bluebotlaboratories.com
#
# wxOverlay
#
# Program that displays overlay on user's PC
# Customizable message using command arguments
###

import wx
import keyboard
import argparse


parser = argparse.ArgumentParser(description="Display a semi-transparent overlay on a user's PC")
parser.add_argument('message', type=str, help='The message to display on the overlay')
parser.add_argument('-a', '--alpha', default=150, type=int, help='The alpha of the message (0-255, 255 is solid) (default: 150)')
parser.add_argument('-b', '--blockKeyboard', action="store_true", help='Block keyboard input (cannot block CTRL+ALT+DEL as it is an OS-level shortcut, however, this blocks just about everything else)')
parser.add_argument('-c', '--colour', type=str, default="#0000FF", help='The colour of the background of the message (default: #0000FF)')
parser.add_argument('--hide', action="store_true", help='Hide the "powered by" message added to the end of a message')
parser.add_argument('-q', '--quitMessage', type=str, default="\n\n\nDid you really think that was going to work???", help='The message displayed (under the overlay message) when the user tries to quit the message app (default "\\n\\n\\nDid you really think that was going to work???"')
parser.add_argument('-t', '--textColour', type=str, default="#000000", help='The colour of the text in the message (default: #000000)')

args = parser.parse_args()

addedMessage = "\n\n\n\nPowered By:\nBluebotlaboratories\nwxOverlay"
processedMessage = str(eval("\"" + args.message.replace("\"", "\\\"") + "\""))

class alphaFrame(wx.Frame):
    def __init__(self):
        # Initialise frame
        wx.Frame.__init__(self, None, title=processedMessage, style=wx.CLIP_CHILDREN|wx.MAXIMIZE|wx.STAY_ON_TOP)
        

        # Create sizer to center message
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create message
        self.SetForegroundColour(wx.Colour(args.textColour))
        if (args.hide):
            self.message = wx.StaticText(self, -1, processedMessage, (25, 25), style=wx.ALIGN_CENTRE_HORIZONTAL)
        else:
            self.message = wx.StaticText(self, -1, processedMessage + addedMessage, (25, 25), style=wx.ALIGN_CENTRE_HORIZONTAL)
            
        self.message.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL))

        # Add and center message in sizer
        self.sizer.Add(self.message, proportion=10, border=0, flag=wx.ALIGN_CENTER)
        self.SetSizer(self.sizer)

        # Set background colour
        self.SetBackgroundColour(wx.Colour(args.colour))
        
        # Set transparency
        self.SetTransparent(args.alpha)

        # Set fullscreen
        self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)

        # Bind window close event
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, evt):
        if (args.hide):
            self.message.SetLabel(str(processedMessage + args.quitMessage))
        else:
            self.message.SetLabel(str(processedMessage + args.quitMessage + addedMessage))
            
        self.sizer.Layout()
        #self.Destroy()


def kbCallback(event):
    print("[KEYPRESS]\t", event.name)

keyboard.hook(kbCallback, suppress=args.blockKeyboard)


class MyApp(wx.App):
    def OnInit(self):

        #------------

        frame = alphaFrame()
        frame.Show()

        return True

#---------------------------------------------------------------------------

app = MyApp(redirect=False)
app.MainLoop()
