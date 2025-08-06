monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}

unique_visitors = monday_visitors.union(tuesday_visitors, wednesday_visitors)

returning_on_tuesday = tuesday_visitors - monday_visitors

new_visitors_each_day = {
    "Monday": len(monday_visitors - tuesday_visitors - wednesday_visitors),
    "Tuesday": len(tuesday_visitors - monday_visitors - wednesday_visitors),
    "Wednesday": len(wednesday_visitors - monday_visitors - tuesday_visitors),
}   

loyal_visitors = monday_visitors.intersection(tuesday_visitors).intersection(wednesday_visitors)

daily_visitor_overlap = {
    "Monday-Tuesday": len(monday_visitors.intersection(tuesday_visitors)),
    "Monday-Wednesday": len(monday_visitors.intersection(wednesday_visitors)),
    "Tuesday-Wednesday": len(tuesday_visitors.intersection(wednesday_visitors)),
}   

print("Unique visitors across all days:", unique_visitors)
print("New visitors each day:", new_visitors_each_day)
print("Loyal visitors (all three days):", loyal_visitors)
print("Daily visitor overlap:", daily_visitor_overlap)