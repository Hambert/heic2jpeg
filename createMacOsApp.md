# MacOS App

https://py2app.readthedocs.io/en/latest/tutorial.html

## Install

pip install -U py2app


Erstell eine setup.py Datei:

	py2applet --make-setup MyApplication.py


## Development

App erstellen:
	python setup.py py2app -A

Runing app
	./dist/MyApplication.app/Contents/MacOS/MyApplication


## Deployment

Fertige App erstellen

python setup.py py2app

for using PIL I must add the flag --packages=PIL 


## Icon hinzufügen
Für Apple wird ein .icns Bild benötigt
Converter für PNGs
https://cloudconvert.com/png-to-icns

Im setup.py hinzufügen:
	OPTIONS = {
	    'iconfile':'appIcon.icns',
	    'plist': {'CFBundleShortVersionString':'0.1.0',}
	}