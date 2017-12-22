#ARRAY=(1093 1107 1112 1159 1168 1147 1109 1096 1119 1139)
for i in $(seq 1093 1182);
do
  python bvh_reduce.py data/original/gesture${i}.bvh data/original/gesture${i}_rot.bvh
done
