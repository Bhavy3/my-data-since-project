import os
import importlib
import traceback

PROMO_FEATURES = {
    'visual_dashboard': 'visual_dashboard',
    'model_compare_panel': 'model_compare_panel',
    'auto_model_selector': 'auto_model_selector',
    'data_cleaner': 'data_cleaner',
    'error_watchdog': 'error_watchdog',
}

ADDED_FEATURES = []

class PromoUpgradeError(Exception):
    pass

def feature_exists(feature_name):
    try:
        importlib.import_module(f'newai.{feature_name}')
        return True
    except ImportError:
        return False

def run_check():
    print("[PROMO UPGRADE] Scanning for missing features...")
    missing = []
    for key, module in PROMO_FEATURES.items():
        if not feature_exists(module):
            missing.append(module)
    if missing:
        print(f"[PROMO UPGRADE] Missing features: {missing}")
    else:
        print("[PROMO UPGRADE] All promo features already present.")
    return missing

def patch_features(missing):
    for module in missing:
        try:
            # Simulate adding a feature as a stub module
            with open(os.path.join(os.path.dirname(__file__), f"{module}.py"), 'w') as f:
                f.write(f"# Stub for {module}\n")
                f.write(f"def info():\n    return '{module} added by promo upgrade.'\n")
            ADDED_FEATURES.append(module)
            print(f"[PROMO UPGRADE] Added {module}.")
        except Exception as e:
            print(f"[PROMO UPGRADE] Failed to add {module}: {e}")
            raise PromoUpgradeError(f"Failed to add {module}")

def launch():
    print("[PROMO UPGRADE] Launching upgrade...")
    missing = run_check()
    if not missing:
        print("[PROMO UPGRADE] Nothing to do.")
        return
    try:
        patch_features(missing)
        print("[PROMO UPGRADE] Upgrade complete. All features added safely.")
    except PromoUpgradeError as e:
        print(f"[PROMO UPGRADE] Error: {e}")
        rollback()
        print("[PROMO UPGRADE] Rolled back changes.")

def rollback():
    print("[PROMO UPGRADE] Rolling back...")
    for module in ADDED_FEATURES:
        path = os.path.join(os.path.dirname(__file__), f"{module}.py")
        if os.path.exists(path):
            os.remove(path)
            print(f"[PROMO UPGRADE] Removed {module}.")
    ADDED_FEATURES.clear()
    print("[PROMO UPGRADE] Rollback complete.")

if __name__ == "__main__":
    import sys
    if '--rollback' in sys.argv:
        rollback()
    else:
        launch() 