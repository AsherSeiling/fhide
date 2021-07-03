pyinstaller main.py --onefile
mv dist/main ./fhide
rm -rf /usr/local/bin/fhide
mv ./fhide /usr/local/bin/fhide
rm -rf ./build
rm -rf ./dist
rm -f main.spec