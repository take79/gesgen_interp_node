ARRAY=(1093 1107 1112 1159 1168 1147 1109 1096 1119 1139)

for i in ${ARRAY[@]};
do
  cp data/$1/gesture${i}_pos.txt ../gesgen_enquette_app/public/data/$1/.
  echo "cp" + ${i}
done
