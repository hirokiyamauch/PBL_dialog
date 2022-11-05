# PBLでの対話作成手順

PBLサーバーにログインして以下を実行  
## 1.環境作成  
  ### 1.1  Anacondaの導入  
  仮想環境の作成を行う。  
参考記事 : [UbuntuにAnacondaをインストールしたときの手順と備忘録](https://qiita.com/yamagarsan/items/d9864fd01f3f4cca2938)  
  ```
  cd
  mkdir download
  cd download
  ##anaconda download##
  wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
  bash ./Anaconda3-2020.02-Linux-x86_64.sh
  ```
  bashrc内部にexport PATH=~/anaconda3/bin:$PATHを追記して、anacondaを起動できるようにする  
  ```
  cd
  vim ~/.bashrc
  
  ##bashrcの内部でexport PATH=~/anaconda3/bin:$PATHを参考記事を見ながら記入##
  ##bashrcを閉じた後以下を実行##
  
  source ~/.bashrc
  conda create -n [仮想環境名] python=3.8
  ```
  Dir構造のイメージ
  ```
  |—anaconda3 
  |—download  
    ❘—Anaconda3-2020.02-Linux-x86_64.sh  
  ```
  ### 1.2 必要なパッケージのインストール  
  ```
  cd
  ##作業用のDirを作成##
  mkdir pbl 
  cd pbl
  mkdir download  
  cd download  
  ##対話の教科書に載っているgithubを保存しておくhttps://github.com/dsbook/dsbook##
  git clone https://github.com/dsbook/dsbook.git  
  
  ##インストールできない警告が出るが無視でOK##
  pip3 install mecab-python3==0.996.5
  pip install torch==1.4.0+cu92 torchvision==0.5.0+cu92 torchaudio==0.4.0 torchtext==0.5.0 -f https://download.pytorch.org/whl/torch_stable.html
  pip install spacy==2.2.2 panel==0.6.4 fbprophet==0.5 holoviews==1.12.4 configargparse
  pip3 install OpenNMT-py==1.0.0
  git clone https://github.com/OpenNMT/OpenNMT-py.git -b 1.0.0
  cd OpenNMT-py
  pip install -r requirements.opt.txt
  ```
  Dir構造のイメージ
  ```
  |—anaconda3 
  |—download  
  |  ❘—Anaconda3-2020.02-Linux-x86_64.sh  
  |—pbl
     ❘—download
        ❘—dsbook
        ❘—OpenNMT-py
  ```
## 2.Twitterデータから学習
  ### 2.1 学習用データの準備
  収集したTwitterのデータtweet_pairs.txtをdataというdirに入れる
  ```
  cd
  cd pbl
  mkdir data
  mkdir data/orig
  ##データの保存場所によって真ん中の指定場所を変える##
  mv tweet_pairs.txt data/orig/
  
  mkdir code
  cd code
  git clone 
  ```
  作業用Dir内の構造イメージ
  ```
  pbl  
   |—download  
   |  |—dsbook  
   |  |—OpenNMT-py  
   |—data  
   |  |—orig  
   |  |  |—tweet_pairs.txt  
   |  |—OpenNMT-py  
   |—code  
      |—python  
      | |—generate_data_for_opennmt.py  
      | |—generativesystem.py         
      |—makedata.sh  
      |—preprocess.sh  
      |—train.sh  
      |—translate.sh        
  ```
  ### 2.2 学習用データ作成
  tweet_pairs.txtから学習用データを作成(train:全体からdevとtestを引いた数 dev:2000 test:2000)
  data/OpneNMTが作成されてその中に分割されたデータが保存される  
  ```
  cd
  cd pbl/code
  bash makedata.sh
  ```
  作業用Dir内の構造イメージ
  ```
  pbl  
   |—download  
   |—data  
   |  |—orig  
   |  |  |—tweet_pairs.txt  
   |  |—OpenNMT  
   |     |—dev.src
   |     |—dev.tgt
   |     |—test.src
   |     |—test.tgt
   |     |—train.src
   |     |—train.tgt
   |—code  
      |—python        
      |—makedata.sh  
      |—preprocess.sh  
      |—train.sh  
      |—translate.sh        
  ```
  
3.データの前処理
OpneNMTで使えるようにデータの前処理を行う
data-binが作成されてその中に前処理済みデータが保存される  
  ```
  cd
  cd pbl/code
  bash preprocess.sh
  ```
  作業用Dir内の構造イメージ
  ```
  pbl  
   |—download  
   |—data  
   |  |—orig  
   |  |—OpenNMT-py  
   |—data-bin
   |  |—dlg.train.0.pt        
   |  |—dlg.valid.0.pt
   |  |—dlg.vocab.pt
   |—code  
      |—python        
      |—makedata.sh  
      |—preprocess.sh  
      |—train.sh  
      |—translate.sh        
  ```
4.学習
OpneNMTで学習
modelが作成されてその中にモデルが保存される  
  ```
  cd
  cd pbl/code
  bash preprocess.sh
  ```
  作業用Dir内の構造イメージ
  ```
  pbl  
   |—download  
   |—data  
   |  |—orig  
   |  |—OpenNMT-py  
   |—data-bin
   |—model
   |  |—dlg_model_step_50000.pt
   |  |—dlg_model_step_100000.pt
   |—code  
      |—python        
      |—makedata.sh  
      |—preprocess.sh  
      |—train.sh  
      |—translate.sh        
  ```
5.モデルの評価
 testデータからOpnenmtのtranslateで文を生成
 resultが作成されてその中に結果が保存される 
  ```
  cd
  cd pbl/code
  bash translate.sh  
  ```
  作業用Dir内の構造イメージ
  ```
  pbl  
   |—download  
   |—data  
   |  |—orig  
   |  |—OpenNMT-py  
   |—data-bin
   |—model
   |— result
   |  |— pred.txt
   |—code  
      |—python        
      |—makedata.sh  
      |—preprocess.sh  
      |—train.sh  
      |—translate.sh        
  ```
