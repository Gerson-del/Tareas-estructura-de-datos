from logging import exception

#Leer el archivo
def importCSV(filename, delimiter=","):
    dataframe = {}
    try:
        with open(filename, 'r') as file:
            headers = file.readline().strip().split(delimiter)
            for line in file:
                linedata = line.strip().split(delimiter)
                row = {}

                for x in range(len(headers)):
                    if x < len(linedata):
                        row[headers[x]] = linedata[x]
                    else:
                        row[headers[x]] = "null"

                # Use a combination of the first two elements to avoid overwriting
                key = f"{linedata[0]}_{linedata[1]}"
                dataframe[key] = row

    except FileNotFoundError:
        print(f"archiv {filename} no encontrado")
    except Exception as e:
        print(f"Un error a ocurrido: {e}")

    return dataframe

