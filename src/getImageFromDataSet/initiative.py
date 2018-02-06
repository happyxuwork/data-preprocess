# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import passive
import sys
sys.path.append('E:/programdate/python-all-in-for-happyxuwork/cyclegan-1')
import yes as mm


def fun1():
    print("i am fun1")
def main():
    for i in range(100):
        for j in range(100):
            print("i am the main belong to initiative")


if __name__ == "__main__":
    main()
    passive.main()
    mm.main()