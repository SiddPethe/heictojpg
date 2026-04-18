ea# HEIC to JPG Converter
Python Script converts HEIC Images to JPG Format. EXIF Metadata is preserved.

## Description
* Enter the file path where the HEIC files are stored.
* A new folder named "ConvertedFiles" is created in the folder containig HEIC Files. If Folder already exists, it needs to be deleted for new conversion to take place.
* Conversion quality is defaulted to 95.

## Usage
:warning: Perfom actions on Windows only
* Install dev dependency "Pyinstaller" in venv via 
```pipenv install --dev pyinstaller```
* Run pyinstaller to make a .exe file in folder (portable version)
```pyinstaller --onedir --name heic2jpg app.py```
* Portable version found in folder dist/heic2jpg -> move folder heic2jpg where required.

## Packages required.
* colorama
* pillow
* pillow_heif
* tqdm
* pyinstaller (dev) -> to create .exe

## Licence
MIT Free to use as you please. Open source.