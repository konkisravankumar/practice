# #### conditional statments (if,  else, elif)
# a = 5
# if a>0 and a>4:
#      print("it is positive")
#      print("it is larger than 4" )
# a = 5
# if a > 0 :
#     print("it is positive")
# else:
#     print("it is negative")


# num = 20/30
# if num > 0 :
#     print("%f num is postive number " %(num))
# else :
#     if num < 0:
#         print("%num is negative number" %(num))
#     else:
#         print ("%num is zero" %(num))


# num = -10
# if num > 0:
#     print("%f number is positive " %(num))
# elif num < 0:
#     print("%f number is negative" %(num))
# else :
#     print("%f is zero" %(num))

# you = "scissior"
# com = "Rock"
# if you == 'seissor' :
#     print ("you loose")
# elif you == "rock" :
#     print ("same")
# else:
#     print ("you win")

##### loop statements (while, for )

# num = 2
# while num <= 10 :
#     print ("%5d" %(num))
#     num += 1

# a = [13, 56, 87, 18]
# a = (4, 5, 7, 8)
# a = "UST!"
# # for i in a:
# #     print(i)

# a = [(12, 1), (30, 2), (20, 36)]
# for (i, j) in a :
#     print (i , j)

# market = {"oil":20, "rice": 30, "milk":50}
# for grocessry in market.keys ():
#     print ("%10s:%5d" %(grocessry, market[grocessry]))
#
# market = {"oil":20, "rice": 30, "milk":50}
# for keys, values in market.items ():
#     print ("%10s:%5d" %(keys, values))

# a = [True, False]
# for i in a:
#     for j in a :
#         results = i or j
#         print ("%5s and %5s = %5s" %(str(i), str(j), str(results)))

# a = [20, 30, 50, 69, 72, 83]
# for i in a:
#     if i>=10:
#         print (i)


for a in range(10):
    if a %2 ==0:
         continue
    print(a)
for a in range(10):
    if a %2 ==0:
         pass
    print(a)
for a in range(10):
    if a %2 ==0:
         break
    print(a)
















