from tkinter import * #import du module tkinter
import webbrowser

def open_git():
    webbrowser.open_new("https://github.com/oxydis")

#crée sa première fenêtre
window = Tk()
#donner un titre à la fenêtre
window.title("Premier cours Tkinter")
#modifier les dimensions de la fenêtre
window.geometry("1200x760")
window.minsize(480, 360)
window.maxsize(1920, 1080)
#modifier l'icone de la fenêtre
window.iconbitmap("1280px-React.ico")
#modifier l'arrière plan de la fenêtre
window.config(background="#2b2b2b")

#crée la boite
frame = Frame(window, bg="#2b2b2b")

#ajouter un texte                                           #police et #taille en px #arrière plan #text
label_title = Label(frame, text="Bienvenue sur la fenêtre", font=("Courrier", 40), bg="#2b2b2b", fg='white')
label_title.pack()
#second texte
label_subtitle = Label(frame, text="Aujourd'hui on apprends Tkinter", font=("Courrier", 20), bg="#2b2b2b", fg='white')
label_subtitle.pack()

#ajouter un bouton
gb_button = Button(frame, text="Aller sur mon Github", bg="white", fg="#2b2b2b", command=open_git)
gb_button.pack(pady=25, fill=X)

frame.pack(expand=YES)

#afficher la fenêtre
window.mainloop()