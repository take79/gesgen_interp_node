# gesgen_keras_helpers

gesgen_kerasで使用したスクリプト達  

* filters/  
  使用した移動平均フィルタとone euroフィルタ  

* sh/  
  主にQOL用のsh(一斉にフィルタを適用するなど)  

* calc_{hoge}.py  
  計算用スクリプト  

* create_counter_balance.rb  
  実験で使うカウンターバランス用のtxtを生成する

* del_vel_from_txt_.py  
  pos+velが並んでいるtxtファイルからvel部分を削除しposのみにする  

* fix_position.py  
  deprecated

* flip_ges_pos.py  
  ジェスチャデータの体の向き（前後）を反転させる  

* rot_to_pos.py  
  bvhファイル（回転角）をtxtファイル（座標or座標+α）に変換する  
  
