ARRAY=(1093 1107 1112 1159 1168 1147 1109 1096 1119 1139)

for i in ${ARRAY[@]};
do
  #cp data/$1/predicted/gesture${i}_sma5.txt ../gesgen_enquette_app/public/data/predicted/gesture${i}_pos.txt
  cp data/$1/predicted/gesture${i}_euro_sma5.txt ../gesgen_enquette_app/public/data/predicted/gesture${i}_pos.txt
  echo cp pred ${i}
done
