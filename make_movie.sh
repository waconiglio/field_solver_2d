#!/bin/bash
ffmpeg -y -framerate 10 -i %05d.png -c:v libx264 -pix_fmt yuv420p out.mp4
