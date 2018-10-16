import numpy as nm
from numpy import *
import math as mat
import pandas as pd
import scipy as stat

def coefficient(xmatrix , ymatrix , n):
    tran = nm.transpose(xmatrix)
    print("\n X' = \n", tran)
    x_tran_x = nm.matmul(tran , xmatrix)
    print("\n X'X = \n", x_tran_x)
    x_trans_x_inverse = nm.linalg.inv(x_tran_x)
    print("\n (X'X) inverse = \n", x_trans_x_inverse)
    x_trans_y = nm.matmul(tran, ymatrix)
    print("\n X'Y = \n", x_trans_y)
    bet_value = nm.matmul(x_trans_x_inverse, x_trans_y)
    print("\n beta-value = \n", bet_value)
    y_hat = nm.matmul(xmatrix, bet_value)
    print("\n Y^ = \n", y_hat)
    stp = (ymatrix - y_hat)
    stp_trans = nm.transpose(stp)
    r_s_s = nm.matmul(stp_trans, stp)
    print("\n Y-Y^ = \n", stp)
    print("\n RSS = \n", r_s_s)
    onematrix = nm.ones((10,1), dtype=nm.float)
    onematrix[: , 0] = 1
    one_trans = nm.transpose(onematrix)
    stp1 = (nm.matmul(one_trans, ymatrix))
    print("\n 1_Transpose * Y = \n", stp1)
    stp2 = stp1/n
    print("\n Mean of Y = \n", stp2)
    stp3 = (ymatrix - stp2)
    print("\n Y-Y_bar = \n", stp3)
    stp4 = nm.transpose(stp3)
    print("\n Transpose of (Y-Mean_Y) = \n", stp4)
    t_s_s = nm.matmul(stp4, stp3)
    print("\n TSS = \n", t_s_s)
    m_s_s = t_s_s - r_s_s
    print("\n MSS = \n", m_s_s)
    r2 = r_s_s/(n-2)
    print("\n MSE = \n", r2)
    var_bet = r2 * x_trans_x_inverse
    print("\n Varience of beta = \n", var_bet)
def main():
    y = nm.array([70, 65, 90, 95, 110, 115, 120, 140, 155, 150])
    x = nm.array([80, 100, 120, 140, 160, 180, 200, 220, 240, 260])
    xmatrix = nm.zeros((10, 2), dtype=nm.float)
    xmatrix[:, 0] = 1
    xmatrix[:, 1] = x
    print("\n X-Matrix = \n", xmatrix)
    ymatrix = nm.zeros((10, 1), dtype=nm.float)
    ymatrix[:, 0] = y
    print("\n Y-Matrix = \n", ymatrix)
    n = nm.size(y)
    coefficient(xmatrix, ymatrix, n)

main()

