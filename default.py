# import the kodi python modules we are going to use
# see the kodi api docs to find out what functionality each module provides
import xbmc
import xbmcaddon
import sys
import xbmcgui
import json

def debug(msg, *args):
    try:
        txt=u''
        msg=unicode(msg)
        for arg in args:
            if type(arg) == int:
                arg = unicode(arg)
            if type(arg) == list:
                arg = unicode(arg)
            txt = txt + u"/" + arg
        if txt == u'':
            xbmc.log(u"OPENWIN: {0}".format(msg).encode('ascii','xmlcharrefreplace'), xbmc.LOGDEBUG)
        else:
            xbmc.log(u"OPENWIN: {0}#{1}#".format(msg, txt).encode('ascii','xmlcharrefreplace'), xbmc.LOGDEBUG)
    except:
        print "OPENWIN: Error in Debugoutput"
        print msg
        print args
               
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
