# ffmpeg-notes
Notes on using ffmpeg

## Install
Mac
```
brew install ffmpeg
```

## Make a video play twice as fast
```
ffmpeg -i input.mkv -filter:v "setpts=0.5*PTS" output.mkv
```
