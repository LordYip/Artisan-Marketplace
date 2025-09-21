import firebase_admin
from firebase_admin import credentials, firestore, storage
import os

FIREBASE_KEY_PATH = os.path.join(os.path.dirname(__file__), "firebase_service_account.json")

# ✅ Use correct bucket name from env
FIREBASE_STORAGE_BUCKET = os.getenv("FIREBASE_STORAGE_BUCKET", "artisan-marketplace-ai-b31cf.firebasestorage.app")

# Initialize Firebase only if service account file exists
db = None
bucket = None

if os.path.exists(FIREBASE_KEY_PATH) and not firebase_admin._apps:
    try:
        cred = credentials.Certificate(FIREBASE_KEY_PATH)
        firebase_admin.initialize_app(cred, {
            "storageBucket": FIREBASE_STORAGE_BUCKET
        })
        db = firestore.client()
        bucket = storage.bucket()
        print("✅ Firebase initialized successfully")
    except Exception as e:
        print(f"⚠️ Firebase initialization failed: {e}")
        print("📝 Backend will run with limited functionality (no Firestore/Storage)")
else:
    print(f"⚠️ Firebase service account not found at: {FIREBASE_KEY_PATH}")
    print("📝 Backend will run with limited functionality (no Firestore/Storage)")
    print("📝 For full functionality, add firebase_service_account.json to backend folder")
