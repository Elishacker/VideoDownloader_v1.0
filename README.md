# VideoDownloader_v1.0
Elifaster Downloader is a powerful and lightweight media downloader that lets you download videos from YouTube, Facebook, Instagram, TikTok, Threads, X (formerly Twitter), and many other platforms using just a media link.

## 📥 Installation Guide

You can install **Elifaster Downloader** by cloning this repository and setting it up for global use:

---

### Step 1: Clone the Repository

```bash
HTTPS ==> git clone https://github.com/Elishacker/VideoDownloader_v1.0.git
SSH  ===> git@github.com:Elishacker/VideoDownloader_v1.0.git
cd VideoDownloader_v1.0

### Step 2: Make the Script Executable

chmod +x elifasterdownloader.py

###Step 3: Move to a Global Path

To use the downloader from anywhere in your terminal, move it to /usr/local/bin:

sudo mv elifasterdownloader /usr/local/bin/

### Step 4: Install yt-dlp (if not installed)
Option A: Install via package manager (Debian/Ubuntu)

sudo apt install yt-dlp

Usage::

Once installed, run the script globally:

elifasterdownloader <video-link>

Example:

elifasterdownloader https://youtu.be/X5t8rA8ik2k


Note: If you want to uninstall it, simply run:

sudo rm /usr/local/bin/elifasterdownloader

