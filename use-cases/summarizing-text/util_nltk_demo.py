from util_nltk import *
# text = "This is a sample text. It has multiple sentences. The text is used to demonstrate how to summarize text using code."
text = "Detective Jack Harris has been on the force for over 20 years, but the thrill of the chase has long since dissipated. He’s seen it all, and the monotony of solving murders a day in and day out has left him feeling jaded and disconnected from the world around him.That all changes when a string of murders rocks the city’s music scene. Jazz musicians, all of whom had performed the standard “Autumn Leaves” in the days leading up to their deaths, are turning up dead in mysterious circumstances. At first, the murders seem unrelated, but as Harris delves deeper into the case, he begins to notice a pattern. The killer is clearly targeting jazz musicians and seems to have a deep understanding of the music and the people who play it. As Harris investigates, he finds himself drawn into the vibrant jazz community, and begins to understand the passion and creativity that drives the musicians to perform. But the closer he gets to the killer, the more dangerous the case becomes. The killer is clever and elusive, always one step ahead of Harris. The murders continue to pile up, and Harris is under pressure to solve the case before the killer strikes again. But as the body count rises, Harris realizes that this case is personal to him. He begins to see the victims not just as victims but as human beings with passions and dreams, just like him. He becomes determined to catch the killer and bring an end to the terror. Finally, after months of following leads and chasing dead ends, Harris receives a tip that leads him to the killer’s lair. In a tense showdown, Harris confronts the killer, who turns out to be a former jazz musician turned bitter and resentful after years of struggling to make a living in the cut-throat music industry. With the killer in custody, Harris finally feels a sense of closure and satisfaction. But the case has taken its toll on him, and Harris begins to question whether he can ever truly be satisfied with his job and whether he can continue to be a detective. As he looks out over the city, he wonders if there will always be another case, another killer, waiting to claim their next victim."

n = 50

print(summarize(text, n))