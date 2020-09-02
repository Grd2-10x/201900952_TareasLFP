import json
import webbrowser

lista = [
    {
        "nombre": "juancho",
        "edad": 18,
        "saldo": 200,
        "activo": False
    },
    {
        "nombre": "juanchito",
        "edad": 17,
        "saldo": 320,
        "activo": False
    }, {
        "nombre": "pablo",
        "edad": 28,
        "saldo": 2100,
        "activo": True
    }, {
        "nombre": "pedro",
        "edad": 19,
        "saldo": 1110,
        "activo": False
    }, {
        "nombre": "Auron",
        "edad": 20,
        "saldo": 1800,
        "activo": False
    }, {
        "nombre": "Aura",
        "edad": 18,
        "saldo": 190,
        "activo": False
    }, {
        "nombre": "Eugenio",
        "edad": 19,
        "saldo": 1345,
        "activo": True
    }, {
        "nombre": "German",
        "edad": 22,
        "saldo": 2019,
        "activo": False
    }, {
        "nombre": "mario",
        "edad": 18,
        "saldo": 990,
        "activo": False
    }, {
        "nombre": "grace",
        "edad": 25,
        "saldo": 2533,
        "activo": True
    }
]


def reportweb():
    GG=open('Tarea4.html','w')

    fase = """<html>
        <head> <meta charset="UTF-8"> <title>Reporte Web</title> </head>
        <body> <table> 
        <thead> <tr> <th>Num</th>
        <th>Nombre</th>  
        <th>Edad</th>
         <th>Saldo</th>  
        <th>Activo</th> </tr> </thead>
        <tbody> """
    GG.write(fase)

   lista_string = json.dumps(lista)
   valores = json.loads(lista_string)
   count = 0
   for a in lista:
      GG.write("<tr>")
      GG.write("<th>"+str(count+1)+"</th>")
      GG.write("<td>"+str(valores[count]["nombre"])+"</td>")
      GG.write("<td>"+str(valores[count]["edad"])+"</td>")
      GG.write("<td>" + str(valores[count]["saldo"])+"</td>")
      GG.write("<td>" + str(valores[count]["activo"])+"</td>")
      GG.write("</tr>")
      count = count+1
      GG.write("</tbody>")
      GG.write("</table>")
      GG.write("</body>")
      GG.write("</html>")
      GG.close()
      webbrowser.open_new_tab("Tarea4.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reportweb()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
