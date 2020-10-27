import itertools


courses = zip(main_courses, price_main_courses)


desserts_all = zip(desserts, price_desserts)


drinks_all = zip(drinks, price_drinks)


for i in itertools.product(courses, desserts_all, drinks_all):
    if i[0][1] + i[1][1] + i[2][1] <= 30:
        print(i[0][0], i[1][0], i[2][0], i[0][1] + i[1][1] + i[2][1])
