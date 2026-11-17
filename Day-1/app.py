def cal_weekly_hours(wk_hours):
    if wk_hours<0 or wk_hours>24*7:
        raise ValueError("Week hours should not be 0 or exceed 24x7")
    return wk_hours

def cal_plan(wh,th):

    if th>7 or th<1:
        raise ValueError("Study days exceeding days in a week ")
    if wh<1 or wh>24*7:
        raise ValueError("Weekly hours are not vaild")
    result=wh/th
    return round(result,2)
def main():
    print("-----------COMEACK PLANNER----------")
    name=input("Enter your name\n").strip()
    if not name:
        name="Developer"

    week_hours=cal_weekly_hours(float(input("Enter a target total hours in a week you will study ")))
    while True:
        try:
            target_hours=int(input("Enter a days you will study (1-7)"))
            planner=cal_plan(week_hours,target_hours)
            break
        except ValueError as error1 :
            print(error1)
        except Exception as e:
            print(e)
    print(f"Hi! {name} Your planner is ready")
    print(f"Total hours {week_hours}")
    print(f"Avg hours per day {planner}")
    print("----- Dont loose the hope god is with you -----------------")

if __name__ == "__main__":
    main()
