# VideoDownloader_v1.0
Elifaster Downloader is a CLI powerful and lightweight media downloader that lets you download videos from YouTube, Facebook, Instagram, TikTok, Threads, X (formerly Twitter), and many other platforms using just a media link.

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

sudo mv elifasterdownloader.py /usr/local/bin/elifasterdownloader

### Step 4: Install yt-dlp (if not installed)
Option A: Install via package manager (Debian/Ubuntu)

sudo apt install yt-dlp

Usage::

Once installed, run the script globally:

elifasterdownloader <video-link>

Example:

elifasterdownloader https://youtu.be/X5t8rA8ik2k
OR
elifasterdownloader "https://youtu.be/X5t8rA8ik2k"

Note: If you want to uninstall it, simply run:

sudo rm /usr/local/bin/elifasterdownloader

NOTES: 
USE QUOTE "" when the Url it has '&'
The & is interpreted by zsh as a background operator, which causes a syntax error unless escaped or quoted.


#################################################################################### **********##########################################################################

---

## 🪟 Windows Installation Guide

Follow these steps to install and run **Elifaster Downloader** on Windows.

---

### 🔧 Step 1: Install Python

Download and install Python from:  
https://www.python.org/downloads/

During installation, make sure to check:
- **“Add Python to PATH”**

---

### 🔧 Step 2: Install `yt-dlp`

Open **Command Prompt (cmd)** or **PowerShell** and run:

```bash
pip install yt-dlp

🔧 Step 3: Download the Script

    1. Go to the GitHub repo:
    https://github.com/Elishacker/VideoDownloader_v1.0

    2. Click the green “Code” button → Download ZIP.

    3. Extract the ZIP to a folder
    
🔧 Step 4: Rename and Create a Global Command (Optional)

   1. To run the script easily from any directory:

   2. Rename the script file to: elifasterdownloader.py
   
   3. Open a PowerShell window and add a system-wide alias:
   New-Alias -Name elifasterdownloader -Value "C \ElifasterDownloader\elifasterdownloader.py"
   
   To make it permanent, add that line to your PowerShell profile:

    notepad $PROFILE
    
    🚀 How to Use

     Now you can run:

elifasterdownloader <video-link>


Example:

elifasterdownloader https://youtu.be/X5t8rA8ik2k
OR
elifasterdownloader "https://youtu.be/X5t8rA8ik2k"

NOTES: 
USE QUOTE "" when the Url it has '&'
The & is interpreted by zsh as a background operator, which causes a syntax error unless escaped or quoted.





