import os
import sys

import maya.cmds as mel
import maya.mel as evalMel
import maya.utils as utils
import re as re

version = sys.version
version26 = '2.6'
version27 = '2.7'
version26 = re.compile(version26)
version27 = re.compile(version27)
version26Check = re.findall(version26,version)
version27Check = re.findall(version27,version)

if version26Check != []:
	import auxilium_UI_python2_6 as auxilium_UI_python2_6
if version27Check != []:
	import auxilium_UI_python2_7 as auxilium_UI_python2_7

def create_auxilium_shelf():

	evalMel.eval('if (`shelfLayout -exists AuxiliumShelf `) deleteUI AuxiliumShelf;')
	evalMel.eval('global string $gShelfTopLevel;')
	evalMel.eval('global string $scriptsShelf;')
	evalMel.eval('$scriptsShelf = `shelfLayout -p $gShelfTopLevel AuxiliumShelf`;')
	if version26Check != []:
		evalMel.eval('shelfButton -parent $scriptsShelf -enableCommandRepeat 1 -enable 1 -width 32 -height 32 -manage 1 -visible 1 -preventOverride 0 -annotation "Auxilium: Maya Lighting and Rendering Tool" -enableBackground 0 -align "center" -label "Auxilium" -labelOffset 0 -font "plainLabelFont" -overlayLabelColor 0.8 0.8 0.8 -overlayLabelBackColor 0 0 0 0.25 -image "a_icon.png" -image1 "a_icon.png" -style "iconOnly" -marginWidth 1 -marginHeight 1 -sourceType "python" -command ("auxilium_UI_python2_6.Auxilium()") -commandRepeatable 1;') 
	if version27Check != []:
		evalMel.eval('shelfButton -parent $scriptsShelf -enableCommandRepeat 1 -enable 1 -width 32 -height 32 -manage 1 -visible 1 -preventOverride 0 -annotation "Auxilium: Maya Lighting and Rendering Tool" -enableBackground 0 -align "center" -label "Auxilium" -labelOffset 0 -font "plainLabelFont" -overlayLabelColor 0.8 0.8 0.8 -overlayLabelBackColor 0 0 0 0.25 -image "a_icon.png" -image1 "a_icon.png" -style "iconOnly" -marginWidth 1 -marginHeight 1 -sourceType "python" -command ("auxilium_UI_python2_7.Auxilium()") -commandRepeatable 1;') 		

utils.executeDeferred( create_auxilium_shelf )


