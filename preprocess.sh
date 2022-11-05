LOAD_FILE="../../data/OpenNMT"
SAVE_FILE="../../data-bin/dlg"

mkdir -p ../../data-bin
python ../../download/OpenNMT-py/preprocess.py -train_src ${LOAD_FILE}/train.src -train_tgt ${LOAD_FILE}/train.tgt -valid_src ${LOAD_FILE}/dev.src -valid_tgt ${LOAD_FILE}/dev.tgt -save_data $SAVE_FILE