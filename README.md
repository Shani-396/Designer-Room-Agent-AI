# 🎨 Designer Room Agent AI

> **A smart, creative, and friendly AI assistant for interior design!**

---

🏡 **Designer Room Agent AI** uses Google's Gemini model to generate curated style suggestions for any room in your house, making home design fast, creative, and fun.

---

## ✨ Features

- 🛋️ **Personalized Design Ideas** – Get inspiring interior design ideas and practical tips tailored to your preferences.
- 🖼️ **Room-Specific Suggestions** – Generates 3–5 unique styles for any room type (bedroom, kitchen, etc.).
- 🤖 **Powered by AI** – Uses Google Gemini's generative AI for creative, diverse suggestions.
- 😊 **Always Friendly & Helpful** – Responses are pleasant, positive, and focused on interior design.

---

## 📦 Dependencies

- Python 3.8+
- **google-adk** (Agent infrastructure)
- **google-generativeai** (Gemini API)
- **python-dotenv**

Install all dependencies:
```bash
pip install -r requirements.txt
```

If `google-adk` is not available on PyPI, please ensure you have access to the package or follow your organization’s instructions for installation.

---

## 🚀 Quick Start

```python
from room_designer_agent.tools import get_room_design

result = get_room_design("living room")
if result["status"] == "success":
    print("Suggested styles:")
    for style in result["styles"]:
        print("-", style)
else:
    print("Error:", result["error_message"])
```

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shani-396/Designer-Room-Agent-AI.git
   cd Designer-Room-Agent-AI
   ```

2. **Install dependencies:**  
   (Requires Python 3.8+)
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google API Key:**  
   Create a `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

---

## 🗂️ Project Structure

| File/Folder                | Description                              |
|---------------------------|------------------------------------------|
| `room_designer_agent/`    | Main package directory                   |
| ├── `agent.py`            | AI agent logic and user interaction      |
| └── `tools.py`            | AI design suggestion tool (Gemini API)   |

---

## 💡 How It Works

1. **Listens to your design needs.**
2. **Uses AI to generate style ideas for any room.**
3. **Shares 3–5 unique styles with short descriptions.**
4. **Keeps the conversation friendly and focused.**

---

## 🧰 Technologies

- Python 🐍
- google-adk
- [Google Gemini AI](https://pypi.org/project/google-generativeai/)
- dotenv

---

## 👤 Author

- [Shani-396](https://github.com/Shani-396)

---

## ⚠️ License

*This project currently does not specify a license.*

---

## 🌟 Get Involved!

Feel free to open issues or submit pull requests if you want to contribute!  
Let’s design something amazing together! 🏠🎉
