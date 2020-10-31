#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, time

fd = os.open('/Users/qs/Downloads/sendMail.jpg', os.O_RDWR)
info = os.fstat(fd)

localtime = time.asctime(time.localtime(info.st_mtime))
pasttime = time.time() - info.st_mtime
print "最后修改时间", pasttime, "秒"