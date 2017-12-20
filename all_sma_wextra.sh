#ARRAY=(1093 1107 1112 1159 1168 1147 1109 1096 1119 1139)
for i in $(seq 1093 1182);
do
  python sma.py data/$1/predicted/gesture${i}.txt $2 1
done
