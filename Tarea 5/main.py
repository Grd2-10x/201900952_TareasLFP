




def determinar(self):
 estad =0
 for i in range(0,len(self)):
         pas =self[i]
         if estad == 0:
             if str.isalpha(pas ) == True:
                 estad =2

             elif pas == '_' :

                 estad = 1

             else:
                 print("-------------Cadena incorrecta-------------")

         elif estad == 2:

            if str.isalpha(pas )==True:
                estad =2
            elif str.isdigit(pas )==True:
                estad =4

            else:
                print("-------------Cadena incorrecta-------------")
         elif estad == 1:

             if pas == '_' :

                 estad = 1


             elif str.isalpha(pas )==True:
                 estad = 3

             else:
                 print("-------------Cadena incorrecta-------------")
         elif estad == 3:
             if str.isalpha(pas) == True:
                 estad = 3


             elif str.isdigit(pas) == True:
                 estad = 4

             else:
                 print("-------------Cadena incorrecta-------------")

         else:
             print("-------------Cadena incorrecta-------------")
 if estad == 4:
     print("+++++++++++++Cadena aceptada+++++++++++++++")





cad1 = "3servidor"
cad2 = "__servidor1"
determinar(cad1)
determinar(cad2)

