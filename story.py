import random
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    pass
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['ate a burger from his freind', 'found a secret key', 'solved a mistery', 'wrote a book']
how = ['he was caught by the police', 'the police chased him', 'he never came back, and no one ever heard about him']
last = ['after this incident people just heard about him in 1950', 'after this incident no one went to the place where he went']
last1 = ['when there was a myth going on in the country that the place is haunted so some ghost busters tried to go inside but never came back', 'after all this the ghost busters went inside and a saw something really mysterious thing, and they left their jobs']
last2 = ['The End']
a = random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) +"." + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened) + ' after that ' + random.choice(how) + '. ' + random.choice(last) + ', ' + random.choice(last1) + '. ' + random.choice(last2)
print(a)
speak(a)


