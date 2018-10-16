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
    onematrix = nm.ones((6,1), dtype=nm.float)
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
    r2 = r_s_s/(n-3)
    print("\n MSE = \n", r2)
    var_bet = r2 * x_trans_x_inverse
    print("\n Varience of beta = \n", var_bet)
def main():
    y = nm.array([20, 30, 40, 50, 60, 70])
    x1 = nm.array([1, 2, 3, 4, 5, 6])
    x2 = nm.array([1, 4, 9, 16, 25, 36])
    xmatrix = nm.zeros((6, 3), dtype=nm.float)
    xmatrix[:, 0] = 1
    xmatrix[:, 1] = x1
    xmatrix[:, 2] = x2
    print("\n X-Matrix = \n", xmatrix)
    ymatrix = nm.zeros((6, 1), dtype=nm.float)
    ymatrix[:, 0] = y
    print("\n Y-Matrix = \n", ymatrix)
    n = nm.size(y)
    coefficient(xmatrix, ymatrix, n)

main()

