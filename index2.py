def deci_to_bin(n):
     r = 0 
     i = 0
     s = 0
     while(n):
          r = n % 2
          n = n // 2
          s += r * 10 ** i
          i += 1
     print(s)
def bin_to_deci(n):
     r = 0
     s = 0
     i = 0
     while(n):
          r = n % 10
          n = n // 10
          s += r * 2 ** i
          i += 1
     print(s)

print("hey dear user")
while(True):

     print("if you want convert decimal to binary please enter 1")
     print("if you want convert binary to decimal please enter 2")
     a = input()
     print("please enter you number:")
     n = int(input())
     if a == "1":
          deci_to_bin(n)
     elif a == "2":
          bin_to_deci(n)
     print("do you want to countineu? if yes enter y if not enter n:")
     b = input()
     if b == "y":
          continue
     else:
          break



