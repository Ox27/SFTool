# SFTool
_**Experimental**_ string finder tool for hacked client developers with a self destruct method

Download [Latest](https://github.com/Ox27/SFTool/releases/latest)

---

Instructions to using (More in-depth than the instructions in the program)

1.	Launch Minecraft on a version that your client injects into
	* As this was tested with Vape, I am using Forge 11.15.1.1722 for Minecraft 1.8.9 
  ![](https://i.imgur.com/E0cU7ll.png)\
  
2.	Once Minecraft fully loads, start up a world or join a server but get everything loaded and move around a bit

3.	Open up [Process Hacker 2](https://sourceforge.net/projects/processhacker/files/latest/download) and search for `Minecraft` 

  ![](https://i.imgur.com/uoEFSrF.png)
  
4.	Right click on `javaw.exe` and click `Properties` 

  ![](https://i.imgur.com/M93boSd.png)
  ![](https://i.imgur.com/Pk0SJWe.png)
  
5.	Click on `Memory` and **uncheck** `Hide free regions` then click `Strings...` 

  ![](https://i.imgur.com/p7eZK5e.png)
  
6.	Change `Minimum length` to 4 and **check** Image and Mapped and click OK  

  ![](https://i.imgur.com/qLZXAa9.png)
  
7.	Don't change anything and just click `Save...` and save the file to `C:\Path\To\SFTool\clean\` where `Path\To\SFTool\` is the SFTool directory (Wherever you downloaded it.)

8.  Close out of the String Results window and inject your client into MC.

9.  Click the `Refresh` button in the javaw.exe Properties window and click `Strings...`

  ![](https://i.imgur.com/p7eZK5e.png)
  
10. Save the file again, to `C:\Path\To\SFTool\client\` where `Path\To\SFTool\` is the SFTool directory

11. Completely close out of minecraft, even the launcher.

12. Repeat the above steps just don't overwrite the string files you've saved and make sure you save it to the right directory.

13. The program is setup to automatically detect files in these two directories and load them up with some sanity checks to make sure they're proper PH2 files and that they have instance counterparts.

14. Once you have at least 3 files in each category (though the more the better and more acturate), click `Start the comparison`

  ![](https://i.imgur.com/WWzMOxr.png)
  
15. I dunno, patch the strings? I don't work on ghost clients I'm just bored. Do whatever you do when someone finds potential strings

---

Some things to note:
  * I don't completely know how any of this works. As I've stated, I don't work on ghost clients and I don't work for any server that SS's so I can't make claims that "This is a 100% method!" and "This is the best way to find \<Insert client name\>!" This works off of what little knowledge I have of how to find clients and memory strings.
  * This only works with the default Minecraft launcher as of right now due to instance Temp file locations. The program checks for this line `C:\Users\{USER}\AppData\Local\Temp\d867-8eb7-04f5-0x27\OpenAL64.dll` and uses this `d867-8eb7-04f5-0x27` as part of the file checking process to make sure it's testing two of the same Minecraft instance.
  * This is still in Alpha as of writing this. If there's something you'd like to see/something that doesn't work, [create an issue](https://github.com/Ox27/SFTool/issues/new)
  
