# 📱 AutoFlow Studio - GitHub Setup Guide (বাংলা)

## 🎯 এই Guide কি করবে:

এই guide follow করে আপনি:
1. ✅ GitHub এ account তৈরি করবেন
2. ✅ Code upload করবেন
3. ✅ Automatic APK build করবেন
4. ✅ APK download করবেন

**মোট সময়:** 15-20 minutes

---

## 📋 Step 1: GitHub Account তৈরি করুন

### 1.1 GitHub.com এ যান
```
https://github.com
```

### 1.2 Sign Up করুন
- Click করুন: "Sign up" button
- Email দিন: আপনার email address
- Password দিন: strong password
- Username দিন: যেকোনো unique name
- Verify করুন: email verification

### 1.3 Free Plan Select করুন
- "Free" plan select করুন
- কোন payment লাগবে না

---

## 📋 Step 2: New Repository তৈরি করুন

### 2.1 New Repository Button
- Click করুন: "+" icon (top right)
- Select করুন: "New repository"

### 2.2 Repository Details
```
Repository name: autoflow-studio-android
Description: AutoFlow Studio - Android Video Creation App
Visibility: Public (অথবা Private)
```

### 2.3 Initialize Repository
- ✅ Check করুন: "Add a README file"
- Click করুন: "Create repository"

---

## 📋 Step 3: Code Upload করুন

### 3.1 Upload Files
- Click করুন: "Add file" button
- Select করুন: "Upload files"

### 3.2 Files Select করুন
আপনার computer থেকে এই files upload করুন:
```
✅ main.py
✅ buildozer.spec
✅ requirements.txt
✅ .github/workflows/build-android.yml
```

**Note:** `.github` folder টা ঠিকভাবে upload করুন (folder structure maintain করে)

### 3.3 Commit Changes
- Scroll down করুন
- Write করুন: "Initial commit"
- Click করুন: "Commit changes"

---

## 📋 Step 4: GitHub Actions Enable করুন

### 4.1 Actions Tab
- Click করুন: "Actions" tab (top menu)
- যদি prompt আসে: "I understand my workflows, go ahead and enable them"

### 4.2 First Build Start করুন
- Automatic build শুরু হবে
- অথবা manually trigger করুন:
  - Click করুন: "Build Android APK" workflow
  - Click করুন: "Run workflow" button
  - Click করুন: "Run workflow" (green button)

---

## 📋 Step 5: Build Process Monitor করুন

### 5.1 Build Status দেখুন
- "Actions" tab এ থাকুন
- Latest workflow run click করুন
- Build progress দেখতে পারবেন

### 5.2 Build Time
```
⏱️ First build: 15-20 minutes
⏱️ Subsequent builds: 10-15 minutes (cached)
```

### 5.3 Build Steps
```
✅ Checkout code
✅ Setup Python
✅ Install dependencies
✅ Install system dependencies
✅ Build APK with Buildozer
✅ Upload APK
✅ Create Release
```

---

## 📋 Step 6: APK Download করুন

### 6.1 Build Complete হলে
- Build complete হলে green checkmark দেখাবে ✅
- Scroll down করুন "Artifacts" section এ

### 6.2 Download APK
- Click করুন: "AutoFlowStudio-APK"
- ZIP file download হবে
- Extract করুন ZIP file
- APK file পাবেন

### 6.3 Alternative: Release থেকে Download
- Click করুন: "Releases" (right sidebar)
- Latest release click করুন
- "Assets" section এ APK পাবেন
- Direct download করুন

---

## 📋 Step 7: APK Install করুন

### 7.1 Phone এ Transfer করুন
- USB cable দিয়ে phone connect করুন
- APK file copy করুন phone এ
- অথবা Google Drive/WhatsApp দিয়ে send করুন

### 7.2 Install করুন
- Phone এ APK file খুলুন
- "Install" button click করুন
- যদি warning আসে: "Install anyway" click করুন
- Installation complete!

### 7.3 Open App
- App drawer থেকে "AutoFlow Studio" খুলুন
- Enjoy! 🎉

---

## 🔄 Future Updates

### Code Update করার জন্য:

#### Method 1: Web Editor (সহজ)
```
1. GitHub.com এ যান
2. File click করুন (যেমন: main.py)
3. Edit icon (pencil) click করুন
4. Code change করুন
5. "Commit changes" click করুন
6. Automatic build হবে
7. New APK download করুন
```

#### Method 2: Upload New Files
```
1. "Add file" > "Upload files"
2. Updated files upload করুন
3. "Commit changes"
4. Automatic build হবে
```

---

## ⚠️ Troubleshooting

### Problem 1: Build Failed
**Solution:**
```
1. "Actions" tab এ যান
2. Failed build click করুন
3. Error message পড়ুন
4. Common fixes:
   - buildozer.spec file check করুন
   - requirements.txt check করুন
   - Retry build করুন
```

### Problem 2: APK Install হচ্ছে না
**Solution:**
```
1. Phone Settings > Security
2. "Unknown sources" enable করুন
3. অথবা "Install unknown apps" permission দিন
4. আবার install করার চেষ্টা করুন
```

### Problem 3: App Crash হচ্ছে
**Solution:**
```
1. Phone Settings > Apps > AutoFlow Studio
2. "Clear data" এবং "Clear cache"
3. Uninstall করুন
4. আবার install করুন
```

### Problem 4: Build খুব সময় নিচ্ছে
**Solution:**
```
- First build 15-20 minutes normal
- Subsequent builds faster (cached)
- Patience রাখুন ☕
```

---

## 💡 Tips & Tricks

### Tip 1: Build Notifications
```
1. GitHub Settings > Notifications
2. Email notifications enable করুন
3. Build complete হলে email পাবেন
```

### Tip 2: Multiple Versions
```
- প্রতিটি build একটা release তৈরি করে
- "Releases" page এ সব versions পাবেন
- পুরানো version download করতে পারবেন
```

### Tip 3: Private Repository
```
- যদি code private রাখতে চান
- Repository Settings > Danger Zone
- "Change visibility" > "Make private"
```

### Tip 4: Collaborators Add করুন
```
- Settings > Collaborators
- Email দিয়ে invite করুন
- Team member add করতে পারবেন
```

---

## 📊 GitHub Actions Limits

### Free Plan:
```
✅ 2000 minutes/month (build time)
✅ Unlimited public repositories
✅ Unlimited private repositories
✅ 500 MB storage
```

### Typical Usage:
```
- 1 build = 15-20 minutes
- 2000 minutes = ~100-130 builds/month
- More than enough! ✅
```

---

## 🎉 Success!

আপনি এখন:
- ✅ GitHub এ professional setup করেছেন
- ✅ Automatic APK build করতে পারবেন
- ✅ যেকোনো সময় update করতে পারবেন
- ✅ Free forever!

---

## 📞 Support

### যদি কোন সমস্যা হয়:
1. GitHub Issues page এ post করুন
2. Error message screenshot দিন
3. আমি help করব

### Useful Links:
- GitHub Docs: https://docs.github.com
- Buildozer Docs: https://buildozer.readthedocs.io
- Kivy Docs: https://kivy.org/doc/stable/

---

**Happy Building! 🚀**

