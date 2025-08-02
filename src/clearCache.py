import os
import shutil
def clear_cache():
    for root, dirs, _ in os.walk('.'):
        for d in dirs:
            if d == '__pycache__':
                shutil.rmtree(os.path.join(root, d), ignore_errors=True)