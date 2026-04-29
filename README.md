# 🔗 Streamlit QR Code Generator

A simple and interactive **QR Code Generator Web App** built using **Streamlit**. Generate QR codes instantly from any text or URL and download them as PNG images.

---

## 🚀 Live Demo

👉 https://apzbjfvdtffqfdp2rptzao.streamlit.app/

---

## 🚀 Features

* ⚡ Instant QR code generation
* 🔗 Supports URLs and plain text
* 📥 Download as PNG
* 🎨 Clean and interactive UI
* 🧠 Beginner-friendly

---

## 🛠️ Tech Stack

* Python
* Streamlit
* qrcode
* Pillow (PIL)

---

## 📦 Installation

### 1. Clone Repository

```bash
git clone https://github.com/Mafi-Jangra/Scan-Me-App.git
cd streamlit-qr-generator
```

### 2. Install Dependencies

```bash
pip install streamlit qrcode[pil] pillow
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 💻 Usage

1. Enter a URL or text
2. QR code will be generated instantly
3. Preview will appear on screen
4. Click **Download QR Code** to save it

---



---

## ⚙️ Configuration

You can customize QR code settings inside the code:

* `version=1` → controls size
* `error_correction=ERROR_CORRECT_L`
* `box_size=10` → pixel size
* `border=4` → margin
* `fill_color="black"`
* `back_color="white"`

---


## 📄 License

This project is licensed under the MIT License.

---