# 3_bell_timer

## 3_bell_timerとは What's 3_bell_timer

学術学会の口頭発表では，以下のようにベルを鳴らすことが多いでしょう．

- 1鈴，チーン * 1：発表者の持ち時間前の予告  
- 2鈴，チーン * 2：発表者の持ち時間の終了  
- 3鈴，チーン * 3：質疑応答の終了  

3_bell_timerは，そのためのベルを鳴らすためのアプリです．


In an oral presentation at an academic conference, the bell will often be rung as follows.

- 1 bell, tinkle * 1: Announcement before the time limit of the presenter's presentation  
- 2 bell, tink * 2: End of the presenter's time  
- 3 bell, tinkle * 3: End of Q&A session  

3_bell_timer is an application to ring a bell for this purpose.

The following sound effects are used for the bell.


なお，ベルの効果音は，以下を利用しています．

<a href="https://pocket-se.info/">ポケットサウンド/効果音素材</a>の
<a href="https://pocket-se.info/archives/603s/">【効果音】ベルスターの呼び鈴「チーン」</a>

## 使い方 How to use

- 3_bell_timer.exe と 3_bell_timer_bell.mp3 をダウンロードして，同じディレクトリに保存   
- 3_bell_timer.exe を起動   
- 時間設定
    - setting をクリックして，秒数を指定．四則演算が使えるので，8分の場合は 「8 * 60」とすると簡単．
    - 既定値は，10分，12分，14分30秒
- 開始：START
- 一時停止：STOP
- 再開：RESTART
- 発表終了：RESET
- 任意にベルを鳴らす：🔔

- Download 3_bell_timer.exe and 3_bell_timer_bell.mp3 and save them in the same directory   
- Start 3_bell_timer.exe   
- Set the time
    - Click on "setting" and specify the number of seconds. Arithmetic operations are available, it is easy to use "8 * 60" for the eighth minutes.   
    - Default values are 10 minutes, 12 minutes, 14 minutes and 30 seconds.   
- Start: START   
- Pause: STOP   
- Resume: RESTART   
- End of presentation: RESET   
- Ring the bell optionally: 🔔   

Translated with DeepL.com (free version)

### ベル音の変更 How to Change bell

使いたい音を 3_bell_timer_bell.mp3 として 3_bell_timer.exe と同じディレクトリに保存すると，その音声に変更できます．

Save the sound file as 3_bell_timer_bell.mp3 in the same directory as 3_bell_timer.exe.

## 類似アプリ Similar Apps

iosではプレゼンタイマーという便利なアプリがあります．

https://apps.apple.com/jp/app/id291171573

HTML版ではTime Keeperというものがあります．

https://github.com/maruta/timekeeper


There is a useful app called Presentation Timer on iOS.

https://apps.apple.com/jp/app/id291171573

There is an HTML version called Time Keeper.

https://github.com/maruta/timekeeper


## ソースコード Source code

3_bell_timer.py をご覧ください．

See 3_bell_timer.py

## Citation

Toshikazu Matsumura (2024) 3_bell_timer. Timer for accademic congress. https://github.com/matutosi/3_bell_timer/
