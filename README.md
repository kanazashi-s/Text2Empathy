Text2Empathy
====

テキストファイルを指定すると、そのテキストファイルの内容から感情分析を行います。  
[Google-Cloud-Natural-Language-APIのサンプルコード analyze.py](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/language/api)を使用しています。  

## Description
[Cloud Natural Language API ドキュメント](https://cloud.google.com/natural-language/docs/)


## Demo
メモ帳上に表示されているテキストファイルを読み込み、感情分析を行っています。  
magnitudeは常に正の値をとり、感情の強さを表していますが、テキストの長さにも依存します。  
scoreは-1から1の値をとり、-1に近いほど負の感情、1に近いほど正の感情を表します。  
![result](https://github.com/zashio/Text2Empathy/blob/master/Text2EmpathyDemo.gif)  
  

## Requirement
- Python3.6.6  
- Jupyterで実行する場合、Anaconda3  


## Usage

### Google Cloud Platformを利用するために
[Google Cloud Platformの簡単スタートアップガイド](http://goo.gl/ua5fQw)の、サービス共通編(P9-P20)を終え、プロジェクトを作成してください。

### ソースコードのコピー
- コンソールを開き、任意の場所で以下を実行し、全てのファイルをダウンロードしてください。  
`git clone https://github.com/zacceydesuyo/Text2Empathy.git`  
- Text2Empathyフォルダ内に移動し、コンソール上で以下を実行し、必要なライブラリをインストールしてください。  
`pip install -r requirements.txt`   

### 認証について  
ソースコード中の、
`os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "C:***/***/***.json"`  
を、訂正する必要があります。  
[認証の概要](https://cloud.google.com/docs/authentication/getting-started)中の、「サービスアカウントを作成する」を実行し、認証用jsonファイルを入手してください。  
<div align="center">
<img src=https://github.com/zashio/Text2Empathy/blob/master/CreateServiceAccountKey.png "GetJson">
</div>
  
「作成」を押してダウンロードされたjsonファイルを、任意の場所に保存して  
`os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "C:***/***/***.json"`  
中の`***/***/***`にその場所へのパスを記載してください。  
これは、環境変数に書き込んでおくのがスマートではありますが、このようにソースコード中で指定することもできます。  
  
### .ipynbを使う場合
- 任意の環境(デモGifではJupyterLab)で"Text2Empathy_note.ipynb"を開き、  
`os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "C:***/***/***.json"`  
を訂正したのち、上から実行してください。  
- このとき、`result = analyze_sentiment(mail_contents, get_native_encoding_type())`中の、`sentiment`を、`entities`もしくは`syntax`に変更することができます。  
- `entities`に変更すると、テキスト内に既知のエンティティ(著名人・ランドマークなどの固有名詞)が含まれているか分析し、そのエンティティに関する情報を返します。  
- `syntax`に変更すると、テキストに対し構文分析を行います。詳細については[形態論と依存関係ツリー](https://cloud.google.com/natural-language/docs/morphology)を参照ください。  
  
### .pyを使う場合
- 任意のエディタで"Text2Empathy.py"を開き、以下を訂正してください。  
`os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "C:***/***/***.json"`  
- コマンドライン上で、以下を実行してください。
`python Text2Empathy.py sentiment ***.txt`
- このとき、コマンド`sentiment`を、`entities`もしくは`syntax`に変更することができます。  
- `entities`に変更すると、テキスト内に既知のエンティティ(著名人・ランドマークなどの固有名詞)が含まれているか分析し、そのエンティティに関する情報を返します。  
- `syntax`に変更すると、テキストに対し構文分析を行います。詳細については[形態論と依存関係ツリー](https://cloud.google.com/natural-language/docs/morphology)を参照ください。  

## Install
必要なライブラリは、'requirements.txt'に記述してあります。  
そのため、以下のコマンドをText2Empathyフォルダ内で実行していただくことにより、必要なライブラリがすべてインストールされます。  
`pip install -r requirements.txt`  
※Anaconda環境にてPythonのインストールを行った場合は、pipコマンドとcondaコマンドを併用してのインストールはおやめください。


## Contribution  
お待ちしております。  
フォークして、新しいブランチを作ってそこに変更点をプッシュしておいてください。  
プルリクエストもお願いします。  

## Licence  
This source is licensed under the Apache License, Version2.0

## Author
zashio
