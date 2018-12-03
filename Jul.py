#importere wxformbuilder
import wx
#importere vores wxformbuilder projekt
import gui

#her har vi vores quiz, med spørgsmål og til sidst svar
quiz = [['Hvad er 2 + 3?','7','9','5',3],
          ['Hvilket postnummer har Hillerød?','3460','3400','3500',2],
          ['Er Python sjovt?','Ja','Nej','lidt',1]]

#herunder har vi vores class kaldet "Quiz" som definere nogle funktioner vi selv laver
class Quiz(gui.Mainframe):
    def __init__(self, parent):
        gui.Mainframe.__init__(self, parent)
        #definere at ens point starter med 0
        self.point = 0
        self.quiznr = 0
        self.lavsp()

    #denne funktion også kaldet "lavsp" som står for "lav spørgsmål"
    def lavsp(self):
        #den starter med at indsætte vores point, som altid er 0 til at starte med - kan vi se i linje 15 (self.point = 0)
        self.pointtal.SetLabelText(str(self.point))
        #her sørger den for at "point" forbliver i venstre sider, og ikke hopper til højre
        self.Layout()
        #Dette er hvad mit program viser - starter med at printe spørgsmål 1, og derefter de 3 svarmuligheder
        self.spsm.SetLabelText(quiz[self.quiznr][0])
        self.button1.SetLabelText(quiz[self.quiznr][1])
        self.button2.SetLabelText(quiz[self.quiznr][2])
        self.button3.SetLabelText(quiz[self.quiznr][3])

        #nu printer den så ens point, hvis man svarer rigtigt så +1 men hvis man svarer forkert er det bare =1 (Altså det samme som før)
        print(self.point)
        self.quiznr += 1
        #her sørger den for at min quiz "looper" så den ikke forbliver på sidste spørgsmål
        if self.quiznr == len(quiz):
            #wx.MessageBox(message="Du fik "+ str(self.point)+ " point", style=wx.OK | wx.ICON_INFORMATION)
            self.quiznr = 0

    #Denne funktion er oppe i min menu, som hedder "Close" og gør at man kan lukke programmet
    def exit( self, event ):
        exit(0)

#Her har en tre funktioner, meget ens - men det er de forskellige svarmuligheder
    def btn1click(self, event):
        if quiz[self.quiznr-1][4]==1:
            #Hvis man svarer rigtigt, så får man 1+ point
            self.point += 1
        #her henter den min funktion lavsp (se linje 20)
        self.lavsp()

    def btn2click(self, event):
        if quiz[self.quiznr-1][4]==2:
            self.point += 1
        self.lavsp()

    def btn3click(self, event):
        if quiz[self.quiznr-1][4]==3:
            self.point += 1
        self.lavsp()


#mandatory in wx, create an app, False stands for not deteriction stdin/stdout refer manual for details (Fra din guide, forstår ikke helt hvad den gør)
app = wx.App(False)

#opretter et objekt til Quiz
frame = Quiz(None)

#viser opjektet
frame.Show()

#Starter applikationen
app.MainLoop()
