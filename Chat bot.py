import pyttsx3
engine=pyttsx3.init()
# saved list of questions as a package and imported it.
import libpac
# Hello to start chat
engine.setProperty('rate',150)

print("Welcome to amazon chat services".center(150,'*'))
engine.say(libpac.dict[input("say hello and start your chat: ")])
engine.runAndWait()
print(libpac.dict["hello"])
# Collecting name
name=input("enter your name: ")
engine.say("hello , mister " +name+" How may i help you today? ")
engine.runAndWait()
print("hello , mister" +name+" How may i help you today? ")
engine.say("Please select any one of the option from below : ")
engine.runAndWait()
print("Please select any one of the option from below : ")
# function to get list of question
def qa():
    for i in libpac.question:
        print(i)
    mo=input("Enter your option: ")
    # for mobile number register
    if mo=="2":
        engine.say(libpac.dict[mo])
        engine.runAndWait()
        print(input("Please type your new mobile number: "))
        engine.say("Your new mobile number has been successfully registered")
        engine.runAndWait()
        print("Your new mobile number has been successfully registered")
        r=(input("Do you want to continue (yes / no) : "))
        if r=="yes":
            qa()
        else:
            engine.say("Thank you for choosing us , have a nice day ahead")
            engine.runAndWait()
            print("Thank you for choosing us , have a nice day ahead")
    # for other options    
    else:    
        engine.say(libpac.dict[mo])
        engine.runAndWait()
        print(libpac.dict[mo])
        r=(input("Is there anything else to help you with (yes / no) : "))
        if r=="yes":
            qa()
        else:
            engine.say("Thank you for choosing us , have a nice day ahead")
            engine.runAndWait()
            print("Thank you for choosing us , have a nice day ahead")
qa()






    


    




    



      
