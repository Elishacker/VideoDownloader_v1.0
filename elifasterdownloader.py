#!/usr/bin/env python3
import sys
import yt_dlp

def main():
    if len(sys.argv) < 2:
        print("Usage: elifasterdownloader <YouTube URL>")
        sys.exit(1)

    video_url = sys.argv[1]

    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print("✅ Download complete!")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
