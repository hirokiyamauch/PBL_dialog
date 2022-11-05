#LOAD_FILEとSAVE_DIRを指定#
LOAD_FILE="../../data/orig/tweet_pairs.txt"
SAVE_DIR="../../data/OpenNMT"

mkdir -p $SAVE_DIR
python python/generate_data_for_opennmt.py -lf $LOAD_FILE -sd $SAVE_DIR