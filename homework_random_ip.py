#!/usr/bin/python3.8
# -*- coding=utf-8 -*-
#本脚本有Bob Wang测试编写

import random
section1 = random.randint(1, 255)
section2 = random.randint(0, 255)
section3 = random.randint(0, 255)
section4 = random.randint(0, 254)

random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
print(random_ip)


if __name__ == '__main__':

    pass
