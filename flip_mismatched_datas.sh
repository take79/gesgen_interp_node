ARRAY=(1093 1107 1112 1159 1168 1147 1109 1096 1119 1139)
for i in ${ARRAY[@]};
do
  python flip_ges_pos.py data/mismatched/gesture${i}_pos.txt
done
