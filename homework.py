class BMW():
    def average(self):
        print("The average cost of a BMW is 50 thousand dollars")
    def quality(self):
        print("Most BMW cars have decent quality")
class Ferrari():
    def average(self):
        print("The average cost of a Ferrari is 400 thousand dollars")
    def quality(self):
        print("Most Ferrari cars have amazing quality")
obj_BMW = BMW()
obj_Fer = Ferrari()
for car in (obj_Fer, obj_BMW):
    car.average()
    car.quality()