from bard_api import summarizer

input_text = '''
En un día soleado, John fue al parque a jugar béisbol con sus amigos. Golpeó un jonrón y todos aplaudieron.
'''
 
# Resume el texto de entrada con Bard-API
summary = summarizer.summarize(input_text)
 
print(summary)
# Output: "John golpeó un jonrón mientras jugaba a béisbol con amigos en el parque."