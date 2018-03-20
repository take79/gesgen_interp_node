ARRAY=(1093 1107 1112 1159 1168 1147 1109 1096 1119 1139)

for i in ${ARRAY[@]};
do
  cp data/original/gesture${i}_rot.bvh ../gesgen_enquette_app/public/data/nil/.
  echo cp nil ${i}
done
