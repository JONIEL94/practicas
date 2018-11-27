#!/bin/bash

declare -i option=0
read -p "Seleccione una opcion (1,2 o 3 ) : " option

if ((option ==1))
then
		echo "Usted selecciono 1 "
elif((option ==2))
then
		echo "Usted selecciono 2 "
elif((option==3))
then
		echo "Usted selecciono 3 "
else 
		echo "Usted selecciono una opcion incorrecta ! "
		exit 1
fi
exit 0
