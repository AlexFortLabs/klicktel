from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import openpyxl

#Config.set('kivy', 'keyboard_mode', 'systemanddock')

class MyGridLayout():



    def press(self):
        name = self.name.text
        #exceldata = self.exceldata.text
        book = openpyxl.open('PassTel.xlsx')
        #book = openpyxl.open(
        #    "\\\\DESVR-IT01\\edv\\01---Avaya\\Passwoerter_Telefone_und_Benutzer_Funke Kunststoffe GmbH_ProKund.xlsx",
        #    read_only=True)

        sheet = book.worksheets[1]

        suche_nach = self.name.text
        gefunden = False

        # for row in range(1, 10):
        for row in range(1, sheet.max_row + 1):  # jetzt aber alle Reien, mit +1 auch die letzte Reie
            ns_rufnummer = sheet[row][2].value
            # print(ns_rufnummer)
            if ns_rufnummer == suche_nach:
                apparat = sheet[row][4].value
                namesatz = sheet[row][6].value
                ns_pw = sheet[row][15].value
                app_pw = sheet[row][16].value
                voic_pw = sheet[row][17].value
                admin_pw = sheet[row][18].value
                #self.exceldata.text = 'NS: ' + ns_rufnummer + '\nApparatetyp: ' + apparat + '\nAnwender: ' + namesatz + '\n\nNebenstellen-PW: ' + ns_pw + '\nVoice-PW: ' + voic_pw + '\nAdmin-PW: ' + admin_pw
                #self.exceldata.text = 'Apparatetyp: ' + apparat + '\nAnwender: ' + namesatz + '\n\nNebenstellen-PW: ' + ns_pw + '\nVoice-PW: ' + voic_pw + '\nAdmin-PW: ' + admin_pw
                if apparat:
                    self.apparat.text = apparat
                if namesatz:
                    self.namesatz.text = namesatz
                if ns_pw:
                    self.ns_pw.text = ns_pw
                if app_pw:
                    self.app_pw.text = app_pw
                if voic_pw:
                    self.voic_pw.text = voic_pw
                if admin_pw:
                    self.admin_pw.text = admin_pw
                # messagebox.showinfo("Gefunden!", ns_rufnummer + '\n' + admin_pw)
                # print(admin_pw)
                gefunden = True
                break

        #self.name.text = ""
        if not gefunden:
            self.apparat.text = 'Keine Daten zu ' + suche_nach
            self.namesatz.text = ''
            self.ns_pw.text = ''
            self.app_pw.text = ''
            self.voic_pw.text = ''
            self.admin_pw.text = ''

class KlickTelDECT(App):
    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.window.add_widget(Image(source="images/avaya9611.jpg"))

        # label widget
        self.greeting = Label(
            text="What's your name?",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
            text="GREET",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        #self.button.bind(on_press=self.press)
        self.button.bind(on_press=self.calback)
        self.window.add_widget(self.button)

        #self.theme_cls.theme_style = "Light"  #"Dark"
        #self.theme_cls.primary_palette = "BlueGray"
        return self.window

    def press(self):
        name = self.name.text
        #exceldata = self.exceldata.text
        book = openpyxl.open('PassTel.xlsx')
        #book = openpyxl.open(
        #    "\\\\DESVR-IT01\\edv\\01---Avaya\\Passwoerter_Telefone_und_Benutzer_Funke Kunststoffe GmbH_ProKund.xlsx",
        #    read_only=True)

        sheet = book.worksheets[1]

        suche_nach = self.name.text
        gefunden = False

        # for row in range(1, 10):
        for row in range(1, sheet.max_row + 1):  # jetzt aber alle Reien, mit +1 auch die letzte Reie
            ns_rufnummer = sheet[row][2].value
            # print(ns_rufnummer)
            if ns_rufnummer == suche_nach:
                apparat = sheet[row][4].value
                namesatz = sheet[row][6].value
                ns_pw = sheet[row][15].value
                app_pw = sheet[row][16].value
                voic_pw = sheet[row][17].value
                admin_pw = sheet[row][18].value
                #self.exceldata.text = 'NS: ' + ns_rufnummer + '\nApparatetyp: ' + apparat + '\nAnwender: ' + namesatz + '\n\nNebenstellen-PW: ' + ns_pw + '\nVoice-PW: ' + voic_pw + '\nAdmin-PW: ' + admin_pw
                #self.exceldata.text = 'Apparatetyp: ' + apparat + '\nAnwender: ' + namesatz + '\n\nNebenstellen-PW: ' + ns_pw + '\nVoice-PW: ' + voic_pw + '\nAdmin-PW: ' + admin_pw
                if apparat:
                    self.apparat.text = apparat
                if namesatz:
                    self.namesatz.text = namesatz
                if ns_pw:
                    self.ns_pw.text = ns_pw
                if app_pw:
                    self.app_pw.text = app_pw
                if voic_pw:
                    self.voic_pw.text = voic_pw
                if admin_pw:
                    self.admin_pw.text = admin_pw
                # messagebox.showinfo("Gefunden!", ns_rufnummer + '\n' + admin_pw)
                # print(admin_pw)
                gefunden = True
                break

        #self.name.text = ""
        if not gefunden:
            self.apparat.text = 'Keine Daten zu ' + suche_nach
            self.namesatz.text = ''
            self.ns_pw.text = ''
            self.app_pw.text = ''
            self.voic_pw.text = ''
            self.admin_pw.text = ''

    def calback(self, instance):
        self.greeting.text = "Password: " + self.user.text + "\n Pass: " + "Info!"

if __name__ == '__main__':
    KlickTelDECT().run()
