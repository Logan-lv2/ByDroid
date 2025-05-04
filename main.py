import os
import PyPDF2
from gtts import gTTS
from playsound import playsound

def pdf_to_audio(pdf_path, output_audio="output.mp3", lang="fr"):
    # Intro de Bydroid
    intro = "Bonjour je suis Bydroid, une création de Emmanuel. Comme les deux sont flemmards, ils m'ont conçu pour lire leurs cours à leur place. Donc toi aussi, fais de même, mais ne les suis pas, sinon tu deviendras comme Ezekiel. Bon maintenant, relax et écoute ce que contient le document."
    
    tts_intro = gTTS(text=intro, lang=lang, slow=False)
    tts_intro.save("intro.mp3")
    
    # Lecture du PDF
    pdf_text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            pdf_text += page.extract_text() + "\n"
    
    tts_pdf = gTTS(text=pdf_text, lang=lang, slow=False)
    tts_pdf.save(output_audio)
    
    # Jouer les audios
    playsound("intro.mp3")
    playsound(output_audio)
    
    # Nettoyage (optionnel)
    os.remove("intro.mp3")
    os.remove(output_audio)

# Chemin dynamique
dossier_cours = os.path.join(os.path.dirname(__file__), "cours")
pdf_path = os.path.join(dossier_cours, "Cours_De_Développement_Web_Partie_1_(instituts)_114406_033521.pdf")  # ← Change le nom ici

# Exécution
if os.path.exists(pdf_path):
    pdf_to_audio(pdf_path)
else:
    print(f"Erreur : Le fichier {pdf_path} n'existe pas.")