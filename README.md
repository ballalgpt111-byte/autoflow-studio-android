# 📱 AutoFlow Studio - Android Version

## 🎯 Overview

AutoFlow Studio এর Android version - Video creation app for mobile devices.

---

## ✅ Features

- 📝 **Step 1:** Text to Speech
- 🎬 **Step 2:** Audio + Image Slideshow
- ⏱️ **Step 3:** Timer Video
- 🎥 **Step 4:** Final Video Join

---

## 🚀 Quick Start

### For Users (APK Installation):

1. Download APK from [Releases](../../releases)
2. Install on your Android phone
3. Open app and enjoy!

### For Developers (Build from Source):

#### Desktop Testing:
```bash
pip install -r requirements.txt
python main.py
```

#### Android Build (Manual):
```bash
pip install buildozer
buildozer android debug
```

#### Android Build (GitHub Actions):
1. Fork this repository
2. Push to main branch
3. GitHub Actions will automatically build APK
4. Download from Actions artifacts or Releases

---

## 📋 Requirements

### For Users:
- Android 5.0+ (API 21+)
- 100 MB free storage
- Internet connection (for license validation)

### For Developers:
- Python 3.8+
- Kivy 2.2.1
- KivyMD 1.1.1
- Buildozer (for Android build)

---

## 🔧 Development

### Project Structure:
```
android-app/
├── main.py                 # Main application
├── buildozer.spec         # Build configuration
├── requirements.txt       # Python dependencies
├── .github/
│   └── workflows/
│       └── build-android.yml  # GitHub Actions workflow
└── README.md
```

### Local Testing:
```bash
# Install dependencies
pip install -r requirements.txt

# Run on desktop
python main.py

# Build APK (Linux/Mac)
buildozer android debug

# Build APK (Windows - use WSL)
wsl
buildozer android debug
```

---

## 📱 Screenshots

(Coming soon...)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

Copyright © 2026 Big Total Apps

---

## 📞 Support

For issues and questions, please open an issue on GitHub.

---

## 🎉 Credits

- **Developer:** Big Total Apps
- **Framework:** Kivy + KivyMD
- **Build System:** Buildozer + GitHub Actions

---

**Made with ❤️ in Bangladesh**

