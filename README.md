auxilium
========

Basic Description (more Information available within the PDF after download!)

Auxilium is simple to install there are three scripts that allow Auxilium to function, 2 of which are the same just compiled for different versions of python (2.6 and 2.7) but don't worry all the heavy lifting of which script to run and the install of Auxilium are handled with the third script a simple userSetup.py that creates a shelf (called Auxilium shelf) and generates the icon used to run the script! 

This script offers all the features below, and visible in the demo video! If this seems like something interesting please give it a try! Let me know of any issues you encounter, or features you wish to see added by either replying on the creative crash link below, or send me an email at ross.macaluso@gmail.com!

Auxilium is a tool built for Maya that currently supports both Mental Ray and Vray

*This is more than just your standard light editing tool, it also has quite a few unique features;
*dock-able on both left and right, or floating expandable horizontally and vertically to maximize screen space
*batch light renaming
*batch light prefix adding/changing
*batch utility creation (file nodes, set range, gamma correct)
*batch vray geometry shape attr adding/removing/editing 
*light creation (directional,point,spot,area(mental ray) vrayRect,vrayDome,vrayIES,vraySphere(vray)
*user input values for light creation are retained until UI is closed, allowing multiple light types to be created with the same values
*visual light linking, textual light linking
*spreadsheet for quick editing of grouped, or multiple lights
*visual outliner that sorts lights by light-type and adds controls for each light, supports grouped lights and multi selection
*visual outliner contains light soloing, duplicating,deleting and selection for easy movement, and light editing
*visual outliner has optimized HDRI, light texture adding (creates file node,2dplacement) when useHDRI(dome light) or useRect(vrayRect light) are enabled, if disabled (deletes both file and 2dplacement to clean up scene)

and many more features! 

Currently some bugs many exist so please report them if possible, by either commenting here or sending a short email to ross.macaluso@gmail.com

Maya Rendering and Lighting Tool: Update Log


NEW VERSION 1.0.6:

-added light render element, for vray
-fixed many small issues
-added compiled versions for python 2.6 and 2.7, userSetup.py auto selected the correct compiled version
-cleaned up look-thru script so that it more accurately finds the correct camera after looking through a light
 

NEW VERSION 1.0.7:

-added area light shape for mental ray
-fixed issue where decay rate in mental ray wasn't being set correctly
-fixed if a group was created, and a light of the same name was created the name would be a duplicate
-fixed set focus issue on light outliner not allowing user to delete light, or group when UI was first created
-added more controls for displacement (none,shift,continuity,displacement type) 

NEW VERSION 1.0.8:

-bug fixes, general script clean up 
-added a demo video!  