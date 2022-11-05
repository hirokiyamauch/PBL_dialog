import MeCab
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-lf',  type=str, help='load file help')
parser.add_argument('-sd',  type=str, help='save file help')

opt = parser.parse_args()

DATA_NUM = sum([1 for _ in open(opt.lf)])
# データ数を設定
DEV_PAIR_NUM = 2000
TEST_PAIR_NUM = 2000
if DEV_PAIR_NUM + TEST_PAIR_NUM >= DATA_NUM:
    print("データ数が少ないです")
    exit()
TRAIN_PAIR_NUM = DATA_NUM-(DEV_PAIR_NUM+TEST_PAIR_NUM)
print("データ数:train ", TRAIN_PAIR_NUM, " ,dev ", DEV_PAIR_NUM , " ,test ", TEST_PAIR_NUM)

mecab = MeCab.Tagger ("-Owakati")
mecab.parse("")

source = []
target = []
with open(opt.lf) as f:
    for i, line in enumerate(f):
        line = line.strip()

        if "\t" in line:
            s = mecab.parse(line.rsplit("\t", 1)[0].replace("\t", " SEP "))
            t = mecab.parse(line.rsplit("\t", 1)[1])
            # 両方とも5単語以上のツイートリプライペアを使用
            if len(s) >= 5 and len(t) >= 5:
                source.append(s)
                target.append(t)
        # 設定したデータ数に達したら読み込みを終了
        if len(source) > DEV_PAIR_NUM + TEST_PAIR_NUM + TRAIN_PAIR_NUM:
            break

# 出力用のディレクトリを作成
os.makedirs(opt.sd, exist_ok=True)

# ファイル出力
with open(opt.sd + "/dev.src", "w") as f:
    for l in source[0:DEV_PAIR_NUM]:
        f.write(l)
with open(opt.sd + "/dev.tgt", "w") as f:
    for l in target[0:DEV_PAIR_NUM]:
        f.write(l)
with open(opt.sd + "/test.src", "w") as f:
    for l in source[DEV_PAIR_NUM:DEV_PAIR_NUM + TEST_PAIR_NUM]:
        f.write(l)
with open(opt.sd + "/test.tgt", "w") as f:
    for l in target[DEV_PAIR_NUM:DEV_PAIR_NUM + TEST_PAIR_NUM]:
        f.write(l)
with open(opt.sd + "/train.src", "w") as f:
    for l in source[DEV_PAIR_NUM + TEST_PAIR_NUM:DEV_PAIR_NUM + TEST_PAIR_NUM + TRAIN_PAIR_NUM]:
        f.write(l)
with open(opt.sd + "/train.tgt", "w") as f:
    for l in target[DEV_PAIR_NUM + TEST_PAIR_NUM:DEV_PAIR_NUM + TEST_PAIR_NUM + TRAIN_PAIR_NUM]:
        f.write(l)
