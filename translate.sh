#model モデルの保存場所 src testデータの場所 output 出力ファイル
mkdir -p ../../result
python ../../download/OpenNMT-py/translate.py -model "../../model/dlg_model" -src ../../data/OpneNMT/test.src -output ../../result/pred.txt -replace_unk -verbose