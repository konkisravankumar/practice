# a = ("Good morning")
# print(a[0])
# print(a[3])
# print(a[10])
####List

# a = [1,2,3,4,5]
# b = ["sravan", "konki", "kumar", "pedda", "srunga"]
# c = []
# d = [13.5, 35, "sravan"]
# e = [23, [1,2,3], "konki"]
# print (type(a))
# print (type(b))
# print (type(c))
# print (type(d))
# print (type(e))

# a = ["sravan", 'kumar', "konki", "pedda", "chinna", "akka"]
# print (a[2])
# print(a[2:4])
# print(a[2:])
# print(a[:4])
# print(a[:])
# print(a[-2])
# print(len(a))
# a.extend(["jeju", "korea"])
# print(a)
# a.append("ram")
# print(a)
# a.insert(2, "dad")
# a.remove("ram")
# print(a.pop())
# print(a.index("konki"))
# print(a.count("konki"))
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

####Tuple
# a = (1,2,3,4,5)
# b = ("sravan", "konki", "kumar", "pedda", "srunga")
# c = ()
# d = (13.5, 35, "sravan")
# e = (23, (1,2,3), "konki")
# print (type(a))
# print (type(b))
# print (type(c))
# print (type(d))
# print (type(e))
# print(b, type(b))
# name1, name2, name3, name4, name5 = b
# print(name1)
# print(len(a))


#####Dictionary

# classroom = {"sravan":20, "konki":10, "kumar":5}
# print(classroom, type(classroom))
# b = {}
# print(b)
# print(classroom["sravan"])
# classroom["sravan"] =30
# print (classroom)
# classroom["ravan"] =30
# print (classroom)
# del(classroom["ravan"])
# # print (classroom.keys(), classroom.values(), classroom.items())
# k= classroom.keys()
# print (k)
# print ("sravan" in classroom.keys())
# print ("srava" in classroom.keys())
# print(30 in classroom.values())
# print(classroom.get("sravan", "No item"))

###set
# a = (1,2,3,4,5)
# b = ("sravan", "konki", "kumar", "pedda", "srunga")
# print(a, type(a))
# print(b, type(b))
# a = set(a)
# b = set(b)
# print(a, type(a))
# print(b, type(b))
# m = {1, 2, 3, 4}
# n = {1, 6, 7, 8}
# print(m.intersection(n))
# print(m.union(n))

#####range

# a = list(range(10))
# print(a, type(a))
#
# a = list(range(2, 8, 2))
# print(a, type(a))
#
# a = list(range(8, 2, -2))
# print(a, type(a))


####coverting datatypes
#
# a = ("sravan")
# a = list (a)
# a = tuple (a)
# a = set (a)
# a= [[1,2], [3,4]]
# print (a)

### Boolean numbers of data types

# a = []
# b = [1,2]
# print(bool(a))
# print (bool(b))

#### strings
# print ("iam sravan kumar")
# print ('iam sravan kumar')
# print ('''iam
# sravan
# kumar''')
# a = ("iam from india")
# print(a, type(a))
# print(a[4])
# print(a[7])
# print(a[-4])
# print(a[0:5])
# print(a[:6])
# print(a[9:])
# print(a[:])
# print(len(a))
# print(a.upper())
# print(a.split())
# print(a.split("i"))
a = ("i like coffe. i want to have a cup of coffee. you too?")
b = " "
c = "."
d = "sravan"
print(b.join(a))
print(c.join(a))
print(d.join(a))




