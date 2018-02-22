import os, sys, updatedgui, win32con

from win32gui import MessageBox
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QListWidget, QFileDialog
from PyQt4.QtCore import QThread, QTimer
from threading import Thread
from collections import defaultdict

class scompThread(QThread):
  def __init__(self,scomp):
    QThread.__init__(self)
    self.scomp=scomp
  def __del__(self):
    self.wait()
  def run(self):
    self.scomp()
    while True:
      pass

class refreshThread(QThread):
  def __init__(self,ref):
    QThread.__init__(self)
    self.ref=ref
  def __del__(self):
    self.wait()
  def run(self):
    self.ref()
    while True:
      pass

class StringFinder(QtGui.QMainWindow, updatedgui.Ui_StringFinder):
  def __init__(self, parent = None):
    super(StringFinder, self).__init__()
    self.ref = refreshThread(self.refreshFiles)
    self.setupUi(self)
    self.instr.clicked.connect(self.openInstr)
    self.startComp.clicked.connect(self.startThread)
    self.destroyed.connect(self.closeEvent)
    self.lastNames = {}
    self.final = None
    self.ref.start()
    self.timer = QTimer()
    self.timer.timeout.connect(self.checkDone)
    self.timer.start(200)

  def checkDone(self):
    if self.final != None:
      for i in self.final:
        self.strOut.appendPlainText(i)
      num = len(self.final)
      if num == 1:
        sornot = ""
      else:
        sornot = "s"
      self.final = None
      self.setStatus("Done, found %d string%s"%(num,sornot))
    self.timer.start(200)

  def refreshFiles(self):
    while True:
      app.processEvents()
      fileNames = {}
      for i in os.listdir(os.getcwd()+"\\clean\\"):
        with open(os.getcwd()+"\\clean\\"+i,"rb") as f:
          if f.readline().find("Process Hacker 2")!=-1:
            null = [f.readline() for x in range(3)]
            key = f.readline().split("Temp\\")[1].split("\\")[0]
            fileNames[key] = [i]
      for i in os.listdir(os.getcwd()+"\\client\\"):
        with open(os.getcwd()+"\\client\\"+i,"rb") as f:
          if f.readline().find("Process Hacker 2")!=-1:
            null = [f.readline() for x in range(3)]
            key = f.readline().split("Temp\\")[1].split("\\")[0]
            if fileNames.has_key(key):
              fileNames[key] = fileNames[key]+[i]
      if self.lastNames != fileNames:
        self.CList.clear()
        self.DList.clear()
        for i in fileNames.keys():
          self.CList.addItem(os.getcwd()+"\\clean\\"+fileNames[i][0])
          self.DList.addItem(os.getcwd()+"\\client\\"+fileNames[i][1])
          self.lastNames = fileNames
  
  def sComp(self):
    self.final = self.getFinal(self.compLists())

  def startThread(self):
    self.sct=scompThread(self.sComp)
    self.sct.start()
      
  def openInstr(self):
    instr = '''
    Go check the GitHub for a better idea of what the fuck this does.
    
    1.  Launch Minecraft on a version that works for your client
    2.  Open a world and let things load
    3.  Open PH2 (Process hacker 2 you fucknut)
    4.  Search "Minecraft" and click on the "javaw.exe"
    5.  Press enter and click "Memory" in the top bar
    6.  Uncheck "Hide free regions" and click "Strings..."
    7.  Min. Length: 4, check "Image" and "Mapped"
    8.  Wait 7 years (Or until it loads. Which ever comes first)
    9.  Click "Save..." and go to:
        %s\\clean\\
        and save it under any name you wish, the program will find it.
    10. Inject your client
    11. Close out of the Results window and click "Refresh"
    12. Again, "Strings..." Min. Length: 4, check "Image" and "Mapped"
    13. Save it again, but instead to:
        %s\\client\\
        under any name
    14. Shutdown minecraft.
    15. Repeat step 1-14 a few times, just don't overwrite the string
        dump files and change something each times like add a new mod,
        remove mods, change video settings, change language, etc.
    16. Once you have at least 3 files in each "Instance" list in SFTool,
        click "Start the comparison" and wait for the status to say Done.

    Note: I do not claim this works every time.
          I do not claim this is a perfect science.
          I do not know everything there is to know about memory strings.
          The more dump files, the more accurate it will be.
          Only use the default minecraft launcher.
    '''%(os.getcwd(),os.getcwd())
    MessageBox(0,instr, "   Instructions",0)

  def compLists(self):
    strLists = []
    retList = []
    self.listCount = 1
    for clist in range(self.CList.count()):
      with open(self.CList.item(clist).text(),"rb") as f:
        if f.readline().find("Process Hacker 2")!=-1:
          null = [f.readline() for x in range(3)]
          ckey = f.readline().split("Temp\\")[1].split("\\")[0]
      for dlist in range(self.DList.count()):
        with open(self.DList.item(dlist).text(),"rb") as f:
          if f.readline().find("Process Hacker 2")!=-1:
            null = [f.readline() for x in range(3)]
            dkey = f.readline().split("Temp\\")[1].split("\\")[0]
        if ckey == dkey:
          strLists.append([self.parseFile(self.CList.item(clist).text()), self.parseFile(self.DList.item(dlist).text())])
    for i in strLists:
      self.setStatus("Comparing string list #%d"%self.listCount)
      self.listCount += 1
      a,b = i
      retList.append(list(set(b)-set(a)))
    return retList

  def getFinal(self, lists):
    passes = 1
    lnk = defaultdict(list)
    for x in lists:
      for z in x:
        lnk[passes-1].append(z)
      passes += 1
    a = list(lnk.values())
    return list(set(a[0]).intersection(*a[1:]))

  def parseFile(self,pth):
    self.setStatus("Parsing file %s to list"%pth)
    f = open(pth,"r")
    pstr = []
    nulled = [f.readline() for x in range(4)]
    while True:
      data = f.readline()
      if not data:
        break
      try:
        pstr.append(data.split("): ",1)[1].strip("\n"))
      except:
        pstr.append(data.strip("\n"))
    f.close()
    return pstr

  def setStatus(self,s):
    self.statOut.setText(s)

if __name__ == "__main__":
  if not os.path.exists(os.getcwd()+"\\clean\\"):
    if MessageBox(0,"Setup SFTool here?\n"+os.getcwd()+"\\", "First Run",win32con.MB_YESNO) == win32con.IDNO:
      sys.exit()
    os.mkdir(os.getcwd()+"\\clean\\")
    os.mkdir(os.getcwd()+"\\client\\")
  app = QtGui.QApplication(sys.argv)
  window = StringFinder()
  window.show()
  sys.exit(app.exec_())
