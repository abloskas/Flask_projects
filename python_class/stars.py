# # part1
# def draw_stars(list):
#     for i in range(len(list)):
#         print '*'*list[i]
# draw_stars([4, 6, 1, 3, 5, 7, 25])    

# part2

def draw_stars_2(lst):
    for i in lst:
        if isinstance(i, int):
            print "*" * i      
        else:
			print (i[0]*len(i)).lower()

        
draw_stars_2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]) 
        