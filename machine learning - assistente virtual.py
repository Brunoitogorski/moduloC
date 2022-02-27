import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
sys.platform


audio = sr.Recognizer()
maquina = pyttsx3.init()

maquina.say('Trabalho de Conclusão de Curso Bruno Ito Gorski')
maquina.say('Orientação Professor Marco Paulo Soares Gomes')
maquina.say('Olá eu sou a Monalisa, sua assistente Virtual')
maquina.say('Muito obrigado aos professores e a PUC Minas')
maquina.runAndWait()


try:
    with sr.Microphone() as source:
        print('Ouvindo')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'Ramona' in comando:
            print(comando)    
            
except:
    print ('microfone não está ok')
    