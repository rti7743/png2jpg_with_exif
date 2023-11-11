# png2jpg_with_exif
Convert png to jpg. Keep metadata as exif data.

This code converts png to jpg. Keep metadata as exif data.
For example, you can take a large number of erotic images you have created with stable diffsion and turn them into jpgs while keeping the prompts and other metadata.

Running it like this will convert all pngs under the current directory to jpg.
```
find . -name "*.png" -exec python png2jpg_with_exif.py \{\} \;

find . -name "*.png" -print0 | xargs -0 rm
```

The most important feature is to convert the png metadata to jpg exif and maintain it.
I created this because there was no tool that did this for me.



pngをjpgに変換する。メタデータをexifデータとして保ったままで。
たとえば、stable diffsionで作った大量のエロ画像をプロンプトなどのメタデータを保ったままjpgにすることができます。

こんな風に実行すると、カレントディレクトリ以下にあるpngをすべてjpgに変換します。
```
find . -name "*.png" -exec python png2jpg_with_exif.py \{\} \;

find . -name "*.png" -print0 | xargs -0 rm
```

pngのメタデータをjpgのexifに変換して維持するのが最大の特徴です。
これをやってくれるツールがなかったので作成しました。

