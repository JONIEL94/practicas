#bin/bash
declare -i age=0
read -p "ingrese su edad: " age

if ((age>=18))
then
echo "Usted es mayor de edad"
fi

exit 0
