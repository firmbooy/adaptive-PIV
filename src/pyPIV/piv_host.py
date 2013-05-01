from __future__ import division

from PIL import Image
from display import parse_and_show
import subprocess
import time
import cPickle as pickle
import os
import sys
from config import frame_cols, frame_rows, get_px_ndx, source_pairs

image_dir = sys.argv[1]

os.system('killall bluectl')
#bsim_proc = subprocess.Popen(['./bsim_dut'], cwd='../scemi/fpga')
#time.sleep(1)
tb_proc = subprocess.Popen(['runtb', './tb'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd='../scemi/fpga')

for pair in source_pairs:
    imageA = Image.open(os.path.join(image_dir, pair[0])).convert("L")
    imageB = Image.open(os.path.join(image_dir, pair[1])).convert("L")
    for im in [imageA, imageB]:
        for pix in im.getdata():
            tb_proc.stdin.write(str(pix) + '\n')
            print pix
        tb_proc.stdin.write('.\n')

    for frame_row in range(frame_rows):
        for frame_col in range(frame_cols):
            pixel_ndx = get_px_ndx(frame_row, frame_col)
            tb_proc.stdin.write(str(pixel_ndx) + '\n')
    stdout, stderr = tb_proc.communicate('.\n')
    pickle.dump(stdout, open(os.path.join(image_dir, 'stdout.pck'), 'wb'))
    parse_and_show(stdout, image_dir)
