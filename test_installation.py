import sys
import importlib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_imports():
    try:
        logger.info("Testing package imports...")
        required_packages = [
            'pandas',
            'numpy',
            'scikit-learn',
            'streamlit',
            'plotly',
            'seaborn',
            'matplotlib',
            'xgboost',
            'lightgbm',
            'catboost',
            'prophet',
            'shap',
            'lime',
            'optuna',
        ]
        missing_packages = []
        for package in required_packages:
            try:
                importlib.import_module(package)
                logger.info(f"✅ {package} is installed")
            except ImportError:
                missing_packages.append(package)
                logger.warning(f"❌ {package} is NOT installed")
        if missing_packages:
            print("\nMissing packages:")
            for package in missing_packages:
                print(f"- {package}")
            print("\nPlease install missing packages using:")
            print("pip install " + " ".join(missing_packages))
        else:
            print("\n✅ All required packages are installed!")
    except Exception as e:
        print(f"Error in test_imports: {str(e)}")

if __name__ == "__main__":
    test_imports() 