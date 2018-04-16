#!/bin/sh

wget https://www.destroyallsoftware.com/screencasts/catalog

cat catalog | grep 'href="/screencasts/catalog/' | awk -F \" '{ print "https://www.destroyallsoftware.com"$2 }' > page-urls.txt

mkdir pages
cd pages

wget -i ../page-urls.txt

grep 'resolution == "1080p"' -A1 * | grep source | awk -F \" '{ print $2 }' > ../video-urls.txt

cd ..

mkdir videos
cd videos

wget -i ../video-urls.txt

for F in ./* ; do
    VIDEO_NAME=`expr "$F" : "\(.*\.mp4\)"`

    mv $F $VIDEO_NAME
done
