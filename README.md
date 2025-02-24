# Instagram Reel Bot

A Python bot to automatically post reels on Instagram, using the [Instagrapi](https://github.com/adw0rd/instagrapi) library. The bot is designed to run daily via GitHub Actions, posting a video reel with a scheduled caption.

## 🛠️ Features

- Automatic Instagram login with session persistence
- Daily posting of video reels with a dynamic counter in the caption
- GitHub Actions integration for automated scheduling
- Simple configuration via environment variables

## 📂 Project Structure

```
├── main.py               # Main script to post reels
├── session.json          # Stores Instagram session data
├── counter.txt           # Keeps track of the daily counter
├── reel.mp4              # Video file to be posted
├── reel.mp4.jpg          # Thumbnail image for the reel
├── requirements.txt      # List of dependencies
├── .github/
│   └── workflows/
│       └── post_reel.yml # GitHub Actions workflow
└── .env                  # Environment variables
```

## 🧩 Installation

1. **Clone the repository:**
```sh
git clone https://github.com/BezerraC/insta-post.git
cd insta-post
```

2. **Create a virtual environment (optional but recommended):**
```sh
python -m venv venv
source venv/bin/activate
```

3. **Install the dependencies:**
```sh
pip install -r requirements.txt
```

4. **Set up environment variables:**
Create a `.env` file with your Instagram credentials:

```
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
```

## 🏃‍♂️ Usage

### Locally:

Run the script manually:
```sh
python main.py
```

The bot will:
- Log in to Instagram (or load a saved session)
- Post the reel video with the defined caption
- Update the counter for the next post

### Via GitHub Actions:

The project comes with a pre-configured workflow:

`.github/workflows/post_reel.yml`

It runs every day at **17:00 (BRT)** (20:00 UTC):
```yaml
on:
  schedule:
    - cron: "0 20 * * *"
```

To activate the workflow:

1. Commit and push your changes to GitHub.
2. Go to your repository → **Settings** → **Secrets and variables** → **Actions**.
3. Add the following secrets:
   - `IG_USERNAME`: Your Instagram username
   - `IG_PASSWORD`: Your Instagram password

## 🚩 Handling Instagram Challenges
If Instagram triggers a challenge (like email verification), you'll need to manually resolve it. For a more automated approach, you might want to implement an email API to fetch and handle the verification code.

## 📘 Notes
- Make sure your account is secure and doesn’t get blocked for suspicious activity.
- Avoid violating Instagram’s terms of service by spamming or over-posting.

## 📄 License
This project is licensed under the MIT License.

## 🙌 Contributing
Feel free to open issues or submit pull requests!

---

Enjoy your automated Instagram posting bot! 🚀

