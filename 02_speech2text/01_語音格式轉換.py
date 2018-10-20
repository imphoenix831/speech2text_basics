
# 記得要先轉換工作目錄喔
import moviepy.editor as mp

# 把影片轉成音檔
clip = mp.AudioFileClip("case2.mp3")
clip.write_audiofile("case2.wav",fps=48000, ffmpeg_params=["-ac", "1"]) # sample rate
