Open Info Window
======

### What is it?
A simple script that opens the Video Info screen (DialogVideoInfo.xml) when a video is playing.  I often watch a video and want to identify an actor.  This allows me to pull up the cast list.  I find it especially useful in PseudoTV where don't want to just stop the video.

### Setup
1. Install the add-on (obviously).
2. To use it, the script needs to be mapped to a key in your [keymap file](https://kodi.wiki/view/Keymap#Location_of_keymaps).  If you just want this for regular playing in Kodi, the key can go in the FullscreenVideo section.  Example:

```
<FullscreenVideo>
        <keyboard>
			#other stuff that may already be here...
			
			<c mod="ctrl">RunScript(script.openinfowindow)</c>  
		</keyboard>
</FullscreenVideo>
```

If you want to use it in PseudoTV, you (also) need to put it in the global section.

```
<Global>
        <keyboard>
			#other stuff that may already be here...
			
			<c mod="ctrl">RunScript(script.openinfowindow)</c>  
		</keyboard>
</Global>
```

3. The one thing about the Video Info screen is that it has the Play button, which you don't want to push while you're already playing a video (especially in PseudoTV).  To avoid that, you can find your DialogVideoInfo.xml and add the following to the Play button.

In Confluence, find this and add the visible line:

```
<control type="togglebutton" id="8">
	<description>Play/Browse to Episodes</description>
	<include>ButtonInfoDialogsCommonValues</include>
	<label>208</label>
	<alttexturefocus border="2">button-focusa.png</alttexturefocus>
	<alttexturenofocus border="2">button-nofocusa.png</alttexturenofocus>
	<altlabel>1024</altlabel>
	<usealttexture>String.IsEqual(ListItem.DBTYPE,tvshow)</usealttexture>
	<visible>!Player.HasVideo</visible>										<----- add this
</control>
```

In Estuary, find this and add the visible line:



```
<control type="togglebutton" id="8">
	<description>Play/Browse to Episodes</description>
	<include>ButtonInfoDialogsCommonValues</include>
	<label>208</label>
	<alttexturefocus border="2">button-focusa.png</alttexturefocus>
	<alttexturenofocus border="2">button-nofocusa.png</alttexturenofocus>
	<altlabel>1024</altlabel>
	<usealttexture>String.IsEqual(ListItem.DBTYPE,tvshow)</usealttexture>
	<visible>!Player.HasVideo</visible>										<----- add this
</control>
```

### Warnings
Only tested in Kodi 18 Leia.


