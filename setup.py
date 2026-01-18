# setup.py
import subprocess
import sys

def install_packages():
    packages = [
        'streamlit==1.28.1',
        'folium==0.14.0',
        'streamlit-folium==0.15.1',
        'plotly==5.17.0',
        'googlemaps==4.10.0',
        'polyline==2.0.2',
        'pandas==2.1.4'
    ]
    
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_packages()
    print("All packages installed successfully!")