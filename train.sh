#gpu_ranks gpu 番号指定(0,1) save_checkpoint_steps モデルの保存する間隔 train_steps　全体での学習step batch_size 一回の処理する量
#save_model モデルの保存場所 data preprocessで作成したdata-binの場所 
mkdir -p ../../model
python ../../download/OpenNMT-py/train.py -gpu_ranks 0 --save_checkpoint_steps 50000 --train_steps 100000 --batch_size 256 -save_model "../../model/dlg_model" -data ../../data-bin/dlg