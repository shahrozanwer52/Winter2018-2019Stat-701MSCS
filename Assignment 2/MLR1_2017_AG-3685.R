x1 = c(100,200,300,400,500,600,700)
x2 = c(10,20,10,30,20,20,30)
y = c(40,50,50,70,65,65,80)
n = length(x1)
x1sum = 0
x2sum = 0
x1bar = 0
x2bar = 0
ybar = 0
ysum = 0
for(I in 1:n){
  x1sum = x1sum + x1[I]
  x2sum = x2sum + x2[I]
  ysum = ysum + y[I]
}
x1bar = x1sum/n
x2bar = x2sum/n
ybar = ysum/n
x12sum = 0
x22sum = 0
x1ysum = 0
x2ysum = 0
x1x2sum = 0
for(i in 1:n){
  x12sum = x12sum + ((x1[i] - x1bar) ^ 2)
  x22sum = x22sum + ((x2[i] - x2bar) ^ 2)
  x1ysum = x1ysum + ((x1[i] - x1bar) * (y[i] - ybar))
  x2ysum = x2ysum + ((x2[i] - x2bar) * (y[i] - ybar))
  x1x2sum = x1x2sum + ((x1[i] - x1bar) * (x2[i] - x2bar))
}
b1 = ((x22sum * x1ysum) - (x1x2sum * x2ysum)) / ((x12sum * x22sum) - (x1x2sum ^ 2))
b2 = ((x12sum * x2ysum) - (x1x2sum * x1ysum)) / ((x12sum * x22sum) - (x1x2sum ^ 2))
b0 = ybar - (b1 * x1bar) - (b2 * x2bar)
RSS = 0
for(I in 1:n){
  y_hat = b0 + (b1 * x1[I]) + (b2 * x2[I])
  RSS = RSS + (y[I] - y_hat) ^ 2
}
MSE = RSS/(n-3)
VB1 = MSE * (x22sum / ((x12sum * x22sum) - (x1x2sum ^ 2)))
VB2 = MSE * (x12sum / ((x12sum * x22sum) - (x1x2sum ^ 2)))
VB0 = MSE * (1/n + ((x1bar ^ 2 * x22sum) + (x2bar ^ 2 * x12sum) - (2 * x1bar * x2bar * x1x2sum)) / ((x12sum * x22sum) - (x1x2sum ^ 2)))
cat("\nb0 = " , b0)
cat("\nb1 = " , b1)
cat("\nb2 = " , b2)
cat("\nEquation: Y = " , b0, " + ",b1,"(X1) + ", b2 , "(X2)")
cat("\nMSE = " , MSE)
cat("\nV(B0) = " , VB0)
cat("\nV(B1) = " , VB1)
cat("\nV(B2) = " , VB2)