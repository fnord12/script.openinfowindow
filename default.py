import xbmc
import xbmcaddon
import sys
import xbmcgui
import json

def debug(msg, *args):
    try: 
        xbmc.log("OPENINFOWIN: " + (str(msg)))
     
        for arg in args:
            print(str(arg))
    except:
        print ("OPENINFOWIN: Error in Debugoutput")
        print (msg)
        print (args)
        
def getListItem(path):
    li = xbmcgui.ListItem("To Search")
    li.setPath(path)
    li.setInfo('video', {})
    displayVideoInfo(li)
    
def displayVideoInfo(li):
    xbmc.executebuiltin('ActivateWindow(12003)')
    dialog = xbmcgui.Dialog()
    dialog.info(li)
    xbmc.executebuiltin('SendClick(,5)')
    xbmc.executebuiltin('Control.SetFocus(5)')


if (__name__ == '__main__'):
    path = xbmc.getInfoLabel('Player.Filenameandpath')
    ID = xbmc.getInfoLabel('VideoPlayer.DBID')
    
    debug('path', path)
    if not path == '' and not ID == '':
        getListItem(path)
