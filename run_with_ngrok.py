import os
import time
import threading
from pyngrok import ngrok

# 🔐 Set your ngrok authtoken
ngrok.set_auth_token("30EW9XTMsAssnSsGjPK9lhzGrDt_6zvGsL4VTqzz8HjacnEGq")

# 🔁 Function to run Streamlit app
def run():
    os.system("streamlit run app_final_complete.py")  # <-- Replace with your actual app filename

# 🔄 Start Streamlit in background thread
threading.Thread(target=run).start()

# 🕒 Wait for app to boot
time.sleep(5)

# 🌐 Create public tunnel to port 8501
public_url = ngrok.connect(8501)
print("🔗 Public Streamlit URL:", public_url)