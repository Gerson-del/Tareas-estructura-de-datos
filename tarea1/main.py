from dataModule import importCSV
from logging import exception


data = importCSV('data.csv')
print(data)

#-Mostrar en pantalla la diferencia de seguidores(followers) en twitter entre el mes de enero y junio.

seguidores_enero = int(data["TWITTER_SEGUIDORES (FOLLOWERS)"]["ENERO"].replace(",", ""))
seguidores_junio = int(data["TWITTER_SEGUIDORES (FOLLOWERS)"]["JUNIO"].replace(",",""))

diferencia_twitter = abs(seguidores_junio - seguidores_enero)

print(f'la diferencia entre el mes de enero y junio es {diferencia_twitter}')


#-Permita calcular la diferencia de visualizaciones de youtube entre los meses seleccionados por teclado (enero a junio)
try:
  mes1 = input("Ingrese el primer mes: ").upper().strip()
  mes2 = input("Ingrese el segundo mes:").upper().strip()

  print(f"-------diferencia de visualizaciones entre el mes de {mes1} y {mes2}-------")

  month_youtube1 = int(data['YOUTUBE_VISUALIZACIONES'][mes1].replace(",", ""))
  month_youtube2 = int(data['YOUTUBE_VISUALIZACIONES'][mes2].replace(",", ""))

  diferencia_youtube = abs(month_youtube2 - month_youtube1)

  print(f"primer mes ({mes1.lower()}): {month_youtube1}")
  print(f"segundo mes ({mes2.lower()}): {month_youtube2}")
  print(f"diferencia de visualizaciones = {diferencia_youtube}")
except KeyError as e:
  print(f"key error : {e}")
except ValueError as e:
  print(f"value error: {e}")
except Exception as e:
  print(f"exception error {e}")


#Calcular el promedio de crecimiento de twitter y facebook entre los meses de enero a junio.


meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"] #creamos esta lista para poder acceder a los meses
NUM_MONTHS = 12

def obtener_promedio(data,redSocialConcepto,meses,NUM_MONTHS = 12):
  promedio_value = 0
  #utilizaremos un for loop para sumarle el crecimiento a la variable promedio y luego lo dividiremos entre el numero de meses
  for i in range(NUM_MONTHS):
    try:
      #Obtenermos el crecimeinto de la plataforma y lo convertimos a flotante
      value_str = data[redSocialConcepto][meses[i].upper()].replace(",","").replace("%","")
      value = float(value_str)

      promedio_value += value

    except KeyError as e:
      print(f"key error: {e}")
    except ValueError as e:
      print(f"value error: {e}")
    except exception as e:
      print(f"sucedio un error inesperado {e}")

  return promedio_value / NUM_MONTHS

#promedio de crecimiento twitter

prom_crecimiento_twitter = obtener_promedio(data,'TWITTER_CRECIMIENTO DE FOLLOWERS',meses)
print(f" promedio de crecimiento de twitter: {prom_crecimiento_twitter}")

#promedio de crecimiento facebook

prom_crecimiento_facebook = obtener_promedio(data,'FACEBOOK_CRECIMIENTO (seguidores)',meses)
print(f" promedio de crecimiento de facebook: {prom_crecimiento_facebook}")


#-calcular el promedio de “Me gusta” de Youtube, Twitter y Facebook.

#promedio de me gusta youtube
promedio_youtube_likes = obtener_promedio(data,'YOUTUBE_ME GUSTA',meses)
print(f" promedio de me gusta youtube: {promedio_youtube_likes}")

#promedio de me gusta twitter
promedio_twitter_likes = obtener_promedio(data,'TWITTER_ME GUSTA',meses)
print(f" promedio de me gusta twitter: {promedio_twitter_likes}")

#promedio de me gusta facebook
promedio_facebook_likes = obtener_promedio(data,'FACEBOOK_ME GUSTA EN PUBLICACIONES',meses)
print(f" promedio de me gusta facebook: {promedio_facebook_likes}")