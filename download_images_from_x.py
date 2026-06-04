import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# اسم المستخدم
USERNAME = "LegacySiu"

# عدد الصور اللي تبي تنزلهم
MAX_IMAGES = 50

# مجلد الحفظ
SAVE_FOLDER = "downloaded_images"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# إعدادات كروم
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# افتح الصفحة
url = f"https://x.com/{USERNAME}"
driver.get(url)

# انتظر تحميل الصفحة
time.sleep(5)

image_urls = set()

# سكرول لجمع الصور
while len(image_urls) < MAX_IMAGES:
    images = driver.find_elements(By.TAG_NAME, "img")

    for img in images:
        src = img.get_attribute("src")

        if src and "pbs.twimg.com/media" in src:
            # أعلى جودة ممكنة
            src = src.split("&")[0]
            src = src.replace("name=small", "name=large")
            image_urls.add(src)

    # سكرول لتحت
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    print(f"Collected: {len(image_urls)}")

driver.quit()

# تنزيل الصور
for idx, img_url in enumerate(image_urls):
    try:
        response = requests.get(img_url, timeout=10)

        if response.status_code == 200:
            file_path = os.path.join(SAVE_FOLDER, f"image_{idx+1}.jpg")

            with open(file_path, "wb") as f:
                f.write(response.content)

            print(f"Downloaded: {file_path}")

    except Exception as e:
        print(f"Error downloading image: {e}")

print("Done!")