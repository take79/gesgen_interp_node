#ARRAY=(1093 1107 1112 1159 1168 1147 1109 1096 1119 1139)
for i in $(seq 1093 1182);
do
  #python rot_to_pos.py data/original/gesture${i}_rot.bvh data/original/gesture${i}_pos.txt
  python rot_to_pos.py data/data/predicted/gesture${i}_rot.bvh data/data/predicted/gesture${i}_pos.txt
done
