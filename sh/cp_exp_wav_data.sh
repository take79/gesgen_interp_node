ARRAY=(1093 1107 1112 1159 1168 1147 1109 1096 1119 1139)

for i in ${ARRAY[@]};
do
  cp data/audios/audio${i}.wav ../gesgen_enquette_app/public/data/audios/.
  echo "cp" + ${i}
done
