
import openai
#dentro del fichero config tenemos la clave
import config
#le pasamos la clave a openai
openai.api_key=config.api_key
respuesta=openai.ChatCompletion.create(model='gpt-3.5-turbo',
                             messages=[{"role":"user","content":"¿chatGPT tiene algun coste o es gratuito"}])
print(respuesta)
#print(respuesta.choices[0].message.content)